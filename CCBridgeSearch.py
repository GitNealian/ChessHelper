import win32gui
import pyautogui

CCBridge_class_name = 'TCCBMainForm.UnicodeClass'
search_offset = (310, 350)
fen_offset = (310, 470)

def search():
    x, y = pyautogui.position()
    left, top, right, bottom = find_CCBridge()
    if right - left == 0:
        raise Exception('CCBridge window not found')
    pyautogui.click(left + search_offset[0], top + search_offset[1])
    pyautogui.moveTo(x,y)

def paste_fen():
    x, y = pyautogui.position()
    left, top, right, bottom = find_CCBridge()
    if right - left == 0:
        raise Exception('CCBridge window not found')
    pyautogui.click(left + fen_offset[0], top + fen_offset[1])
    pyautogui.moveTo(x,y)


def find_CCBridge():
    handle = win32gui.FindWindow(CCBridge_class_name, None)
    if handle != 0:
        return win32gui.GetWindowRect(handle)
    else:
        return (0, 0, 0, 0)


if __name__ == "__main__":
    paste_fen()
    pyautogui.sleep(0.5)
    search()