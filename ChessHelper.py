from Fen import get_fen
from CCBridgeSearch import paste_fen, search
import win32clipboard as wc
import win32con
import pyautogui
import tkinter as tk


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

    root = tk.Tk()
    root.geometry('300x100')
    root.title('ChessHelper')
    frame = tk.Frame(root, width=300, height = 100)
    
    frame.pack(expand=True)

    button = tk.Button(frame, 
                    text="加载索引",
                    command=load_index)
    button.pack(side=tk.LEFT)
    slogan = tk.Button(frame,
                    text="搜索",
                    command=do_search)
    slogan.pack(side=tk.LEFT)

    root.mainloop()
    