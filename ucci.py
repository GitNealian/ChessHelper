import subprocess
from typing import List, AnyStr, Callable, Any, Tuple
import re
import threading
import time

class Ucci:
    def __init__(self, engine_path: AnyStr, encoding: AnyStr = 'GBK'):
        self.engine_path = engine_path
        self.encoding = encoding
        self.p = None
        self._start()

    def _start(self):
        self.p = subprocess.Popen(self.engine_path, shell=True,
                                  stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        self._check_ucci()

    def _kill(self):
        if self.p is not None:
            subprocess.call(['taskkill', '/F', '/T', '/PID',  str(self.p.pid)])

    # TODO:
    # 使用新线程读取stdout，并使用信号与槽机制进行回调
    def run_command(self, cmd: AnyStr,
                    processor: Callable[[AnyStr], Tuple[bool, Any]] = None,
                    collector: Callable[[List[Any]], Any] = None,
                    timeout: int = 0):
        
        if self.p.poll() is not None:
            raise Exception('command \'' +
                            cmd+'\'is not performed: engine has exited')
        cmd += '\n'
        line_cnt = 0
        results = []
        self.p.stdin.write(cmd.encode())
        self.p.stdin.flush()
        if processor is not None:
            # 使用timer在一定时间后结束进程，防止readline阻塞
            timer = None
            if timeout != 0:
                timer = threading.Timer(timeout, self._kill)
                timer.start()
            while self.p.poll() == None:
                line_cnt += 1
                line = self.p.stdout.readline().decode(self.encoding)
                print(line)
                finished, rst = processor(line)
                if rst is not None:
                    results.append(rst)
                if finished:
                    break

            # 如果超时之前完成数据读取，则取消timer
            if timer is not None:
                timer.cancel()

            # 收集结果
            if collector is not None:
                return collector(results)
            else:
                return line_cnt
        return None

    def _check_ucci(self):
        # 设置timeout为0.5，测试结果表明，合法的引擎能正确返回，不合法的引擎如果带有界面
        # 则在未显示之间就会被结束
        rst = self.run_command('ucci',
                               lambda l: (True, True) if l.startswith(
                                   'ucciok') else (False, None),
                               collector=lambda l: len(l) > 0, timeout=0.5)
        if not rst:
            raise Exception('not a valid ucci engine: '+self.engine_path)
        # print('ucci engine started: '+self.engine_path)

    def quit(self):
        self.run_command('quit')
        self.p.wait()


_ucci = None


def start_engine(engine_path: AnyStr):
    global _ucci
    if _ucci is not None:
        _ucci.quit()
    _ucci = Ucci(engine_path=engine_path)


def _bestmove_catcher(line: AnyStr):
    if line.startswith('bestmove'):
        return (True, None)


def _last(rst: List[Any]):
    return rst[-1]


def valuate(fen: AnyStr, depth: int = 0, on_score: Callable[[int], None] = None):
    def _score_catcher(line: AnyStr):
        if _bestmove_catcher(line):
            return (True, None)
        if depth == 0:
            m = re.search(r'info depth [\d]{1,2} evaluation score ([-\d]+) pv', line)
            if m is not None and on_score is not None:
                on_score(int(m.group(1)))
            return (False, m.group(1) if m is not None else None)
        else:
            m = re.search(r'info depth [\d]{1,2} score ([-\d]+) pv', line)
            if m is not None and on_score is not None:
                on_score(int(m.group(1)))
            return (False, m.group(1) if m is not None else None)
    _ucci.run_command('position fen ' + fen)
    return _ucci.run_command('go depth ' + str(depth),
                             processor=_score_catcher, collector=_last)


def help(fen: AnyStr, depth: int = 10, on_move: Callable[[Tuple[int, int, AnyStr]], None] = None):
    assert(depth > 0)
    def _move_catcher(line: AnyStr):
        if _bestmove_catcher(line):
            return (True, None)
        else:
            m = re.search(
                r'info depth ([\d]{1,2}) score ([-\d]+) pv ([\w\d\s]+)\r\n', line)
            if m is not None:
                print((int(m.group(1)), int(m.group(2)), m.group(3)))
                if on_move is not None:
                    on_move((int(m.group(1)), int(m.group(2)), m.group(3)))
            return (False, (int(m.group(1)), int(m.group(2)), m.group(3)) if m is not None else None)

    _ucci.run_command('position fen ' + fen)
    return _ucci.run_command('go depth ' + str(depth),
                             processor=_move_catcher, collector=_last)

def quit_engine():
    global _ucci
    if _ucci is not None:
        _ucci.quit()
        _ucci = None

if __name__ == "__main__":
    engine_path = 'D:\\BaiduNetdiskDownload\\CCBridge30w\\CCBridge3\\engine\\binghe54\\Binghewusi.exe'
    start_engine(engine_path)
    print(valuate('r1bakab2/9/n1c1c1n2/p1p1p1R1p/9/C4r3/P3P1P1P/B1N1C1N2/9/1R1AKAB2 w - - 0 10'))
    help('2bakabn1/2r4cr/2n4R1/4p1p1p/p1p6/4P4/P1P3P1P/1C2B1N1C/4A4/RNBAK4 r - - 0 1', on_move=print)
    quit_engine()
