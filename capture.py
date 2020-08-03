import win32gui
import os
import pyautogui

handle = win32gui.FindWindow('QQChess', None)
left_offset = 74
top_offset = 200
grid_width = 67.5
left, top, right, bottom = win32gui.GetWindowRect(handle)

def get_region(x, y, width):
    return (x - width / 2, y - width / 2, width, width)

for i in range(10):
    for j in range(9):
        center_x = left + left_offset + grid_width * j
        center_y = top + top_offset + grid_width * i
        pyautogui.screenshot('./chesses/'+ str(i)+'_'+str(j) + '.jpg', region=get_region(center_x, center_y, 30))
