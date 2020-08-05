from Fen import get_fen, red_side
from CCBridgeSearch import paste_fen, search, start_ccbridge
import win32clipboard as wc
import win32con
import pyautogui

import threading
import sys
from PySide2.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PySide2.QtCore import Signal
from ui_mainframe import Ui_MainFrame
from ucci import start_engine, quit_engine, help

chess_names = {'a': '士',
               'b': '象',
               'c': '炮',
               'n': '马',
               'p': '卒',
               'r': '车',
               'k': '将',
               'aa': '仕',
               'bb': '相',
               'cc': '炮',
               'nn': '马',
               'pp': '兵',
               'rr': '车',
               'kk': '帅'}
chinese_numbers = ['九', '八', '七', '六', '五',  '四', '三', '二', '一']
move_types = ['平', '进', '退']


def move_format(board_array, move):

    # move = list(move)
    start = [9 - (ord(move[1]) - ord('0')), ord(move[0])-ord('a')]
    end = [9 - (ord(move[3]) - ord('0')), ord(move[2])-ord('a')]

    name = chess_names[board_array[start[0]][start[1]]]
    move_type = ''
    # 在同一行行动称为'平'
    if start[0] == end[0]:
        move_type = move_types[0]
    # 我方棋子向上为'进',敌方棋子向下为'进'
    elif (start[0] > end[0] if (red_side(board_array) == (len(board_array[start[0]][start[1]]) == 2)) else start[0] < end[0]):
        move_type = move_types[1]
    else:
        move_type = move_types[2]
    pos = []
    # 我方
    if red_side(board_array) == (len(board_array[start[0]][start[1]]) == 2):

        if len(board_array[start[0]][start[1]]) == 2:
            pos = [chinese_numbers[start[1]], chinese_numbers[end[1]]]
        else:
            pos = [str(9 - (start[1] + 1)), str(9 - (end[1]+1))]
    # 敌方
    else:
        if len(board_array[start[0]][start[1]]) == 2:
            pos = [chinese_numbers.__reversed__()[start[1]],
                   chinese_numbers.__reversed__()[end[1]]]
        else:
            pos = [str(start[1]+1), str(end[1]+1)]
    # 修改棋盘
    tmp = board_array[start[0]][start[1]]
    board_array[start[0]][start[1]] = 0
    board_array[end[0]][end[1]] = tmp
    return name + pos[0] + move_type + (str(abs(start[0] - end[0])) if start[1] == end[1] else pos[1])
    # if start[0] == end[d]


class MainWindow(QWidget):
    text_updated = Signal(str)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainFrame()
        self.ui.setupUi(self)
        self.event_bind()

    def event_bind(self):
        self.ui.btnBrowseCCBridge.clicked.connect(self.on_btnBrowseCCBridge_clicked)
        self.ui.btnBrowseUcci.clicked.connect(self.on_btnBrowseUcci_clicked)
        self.ui.btnHelp.clicked.connect(self.on_btnHelp_clicked)
        self.text_updated.connect(self.update_text_browser)


    def on_btnBrowseCCBridge_clicked(self):
        ccbridge_path = QFileDialog.getOpenFileName(
            self, "打开象棋桥", "", "象棋桥 (*.exe)")
        print(ccbridge_path)
        if ccbridge_path is not None and ccbridge_path[0] != '':
            try:
                start_ccbridge(ccbridge_path[0])
                self.ui.leCCBridge.setText(ccbridge_path[0])
            except Exception as e:
                QMessageBox.critical(self, "", str(e))

    def update_text_browser(self, line):
        self.ui.tbHelp.append(line)

    def on_btnHelp_clicked(self):
        self.ui.tbHelp.setText('')

        def do_help():
            fen, board_array = get_fen()

            def append_move(move):
                board_copy = list(map(list, board_array))
                print(board_array)
                self.text_updated.emit('深度：'+str(move[0])+' 评分：'+str(move[1])+'\n' +
                                       ' '.join(list(map(lambda x: move_format(board_copy, x), str(move[2]).split(' ')))))
                # QApplication.processEvents()
            help(fen + ' r - - 0 1', depth=12, on_move=append_move)

        threading.Thread(target=do_help).start()

    def on_btnBrowseUcci_clicked(self):
        engine_path = QFileDialog.getOpenFileName(
            self, "加载UCCI引擎", "", "UCCI引擎 (*.exe)")
        if engine_path is not None and engine_path[0] != '':
            try:
                start_engine(engine_path[0])
                self.ui.leUcci.setText(engine_path[0])
            except Exception as e:
                QMessageBox.critical(self, "", str(e))

    def closeEvent(self, event):
        quit_engine()


def do_search():
    fen = get_fen()
    wc.OpenClipboard()
    wc.EmptyClipboard()
    wc.SetClipboardData(win32con.CF_UNICODETEXT, fen)
    wc.CloseClipboard()
    paste_fen()
    pyautogui.sleep(0.5)
    search()


def load_index():
    search()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
