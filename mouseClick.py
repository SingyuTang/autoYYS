import time

import pyautogui

while True:
    x, y = pyautogui.position()
    time.sleep(1)
    print('X: %s, Y: %s' % (x, y))
    # (x,y):左上角(0, 0),右下角（1920,1080)    #width为x轴（向东变大），height为y轴（向南变大）

from PIL import ImageGrab

im = ImageGrab.grab()
width, height = im.size
# print(im,im.size)
# print("屏幕分辨率为 {}x{}".format(width, height))