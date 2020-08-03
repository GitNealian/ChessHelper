import subprocess
from typing import List, AnyStr, Callable, Any, Tuple
import re


class Ucci:
    def __init__(self, engine_path: AnyStr, encoding: AnyStr = 'GBK',
                 vdepth: int = 10, hdepth: int = 10):
        self.engine_path = engine_path
        self.encoding = encoding
        self.vdepth = vdepth
        self.hdepth = hdepth
        self.regex = re.compile(
            r'info depth [\d]{1,2} score ([\d]+) pv ([\w\d]+)')
        self.p = None
        self.restart()
    
    def restart(self):
        self.p = subprocess.Popen(self.engine_path, shell=True,
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        self.check_ucci()

    def _run_command(self, cmd: AnyStr,
                     processor: Callable[[AnyStr], Tuple[bool, Any]] = None,
                     collector: Callable[[List[Any]], Any] = None):
        cmd += '\n'
        line_cnt = 0
        results = []
        self.p.stdin.write(cmd.encode())
        self.p.stdin.flush()
        if processor is not None:
            while self.p.poll() == None:
                line_cnt += 1
                finished, rst = processor(
                    self.p.stdout.readline().decode(self.encoding))
                if rst is not None:
                    results.append(rst)
                if finished:
                    break
            if collector is not None:
                return collector(results)
            else:
                return line_cnt
        return None

    def bestmove_catcher(self, line):
        if line.startswith('bestmove'):
            return (True, None)

    def score_catcher(self, line):
        if self.bestmove_catcher(line):
            return (True, None)
        else:
            m = self.regex.search(line)
            return (False, m.group(1) if m is not None else None)

    def valuate(self, fen: AnyStr):
        def score_collector(scores):
            return scores[-1]
        self._run_command('position fen ' + fen)
        rst = self._run_command('go depth ' + str(self.vdepth), processor=self.score_catcher, collector=score_collector)
        return rst

    def check_ucci(self):
        rst = self._run_command('ucci',
                                lambda l: (True, True) if l.startswith('ucciok') else (False, None),
                                collector=lambda l: len(l) > 0)
        if not rst:
            raise Exception('ucci引擎不可用：'+self.engine_path)
    
    def quit(self):
        self._run_command('quit')
        self.p.wait()


if __name__ == "__main__":
    engine_path = 'D:\\BaiduNetdiskDownload\\CCBridge30w\\CCBridge3\\engine\\binghe54\\Binghewusi.exe'
    ucci = Ucci(engine_path)
    print(ucci.valuate(
        'r1bakab2/9/n1c1c1n2/p1p1p1R1p/9/C4r3/P3P1P1P/B1N1C1N2/9/1R1AKAB2 w - - 0 10'))
    ucci.quit()