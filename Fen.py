import os
import pyautogui
import multiprocessing
import win32gui
from PIL import Image

QQChess_class_name = 'QQChess'
left_offset = 74
top_offset = 200
grid_width = 67.5
chess_dir = './chesses/'
chess_width = 30


def find_QQChess():
    handle = win32gui.FindWindow(QQChess_class_name, None)
    if handle != 0:
        return win32gui.GetWindowRect(handle)
    else:
        return (0, 0, 0, 0)


def load_chesses(img_dir):
    global chesses
    chesses = []
    for f in os.listdir(img_dir):
        chesses.append((f.split('.')[0], Image.open(os.path.join(img_dir, f))))
        # chesses.append((f.split('.')[0], os.path.join(img_dir, f)))
    return chesses


# board_screenshot = None
def locate(chess_png):
    # global board_screenshot
    # if board_screenshot is None:
    #     left, top, right, bottom = find_QQChess()
    #     if right - left == 0:
    #         raise Exception('QQChess window not found')
    #     board_screenshot = pyautogui.screenshot(
    #         region=(left, top, right - left, bottom - top))
    found = list(pyautogui.locateAll(
        chess_png[1], board_screenshot, confidence=0.80))
    ret = []
    for f in found:
        if color_match(chess_png[0], f):
            f = pyautogui.center(f)
            grid = pix2grid(f)
            if grid != None:
                ret.append((chess_png[0], grid))
    return ret


def color_match(note, box):
    global board_screenshot
    color = 'r'
    for i in range(box.height):
        r, g, b = board_screenshot.getpixel(
            (box.left + box.width / 2, int(box.top + i)))
        if r < 0x40:
            color = 'b'
            break
    return (color == 'b' and len(note) == 1) or (color == 'r' and len(note) == 2)


def pix2grid(point):
    x = int((point.x - left_offset + chess_width / 2) / grid_width)
    y = int((point.y - top_offset + chess_width / 2) / grid_width)
    if 0 <= x < 9 and 0 <= y < 10:
        return (x, y)
    return None


def get_fen():
    global chesses
    global board_screenshot
    board_array = [[0 for i in range(9)] for i in range(10)]
    left, top, right, bottom = find_QQChess()
    if right - left == 0:
        raise Exception('QQChess window not found')
    board_screenshot = pyautogui.screenshot(
        region=(left, top, right - left, bottom - top))
    # cores = multiprocessing.cpu_count()
    # pool = multiprocessing.Pool(processes=cores)
    # for found in pool.imap_unordered(locate, chesses):
    for found in list(map(locate, chesses)):
        for f in found:
            board_array[f[1][1]][f[1][0]] = f[0]
    if not red_side(board_array):
        reverse_board_array(board_array)
    return (board_array_to_fen(board_array), board_array) + ' ' \
        + ('r' if red_side(board_array) else 'b') + ' - - 0 1'


def red_side(board_array):
    for i in range(7, 10):
        for j in range(3, 6):
            if board_array[i][j] == 'kk':
                return True
    return False


def reverse_board_array(board_array):
    for row in board_array:
        row.reverse()
    board_array.reverse()


def board_array_to_fen(board_array):
    fen = ''
    for row in board_array:
        cnt = 0
        for col in row:
            if col == 0:
                cnt += 1
                continue
            if cnt > 0:
                fen += str(cnt)
            cnt = 0
            if len(col) == 1:
                fen += col
            else:
                fen += col[0].upper()
        if cnt > 0:
            fen += str(cnt)
        fen += '/'
    fen = fen[:-1]
    return fen


load_chesses(chess_dir)
if __name__ == "__main__":
    print(get_fen()[0])
