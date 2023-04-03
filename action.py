import cv2,time,random,os, datetime
import os,sys,pyautogui, traceback
import numpy
import mss
from PIL import ImageGrab

#检测系统
# print('操作系统:', sys.platform)
if sys.platform=='darwin':  #mac 系统
    scalar=True
else:
    scalar=False
#按【文件内容，匹配精度，名称】格式批量聚聚要查找的目标图片，精度统一为0.95，名称为文件名

def load_imgs():
    mubiao = {}
    if scalar:
        path = os.getcwd() + '/png'
    else:
        path = os.getcwd() + '/png'
    file_list = os.listdir(path)
    for file in file_list:
        name = file.split('.')[0]
        file_path = path + '/' + file
        a = [ cv2.imread(file_path) , 0.95, name]
        # print("\033[1;31;4mfilepath{}\033[0m".format(file_path))
        mubiao[name] = a

    return mubiao

global imgs
imgs = load_imgs()

def select_mode():
    print('pass')
    pass

def screenshot(monitor):
    '''
    根据monitor设置的范围进行，截图
    :param monitor: 截图范围，monitor = {"top": x0, "left": y0, "width": x1, "height": y1}
    :return:
    '''
    img = mss.mss().grab(monitor)
    im = numpy.array(img)
    mss.tools.to_png(img.rgb, img.size,9,'grab.png')
    # print('img:{};\nim:{}'.format(img,im))
    # print('grab.png')
    # 颜色空间转换，RGB->BGR
    screen = cv2.cvtColor(im, cv2.COLOR_BGRA2BGR)
    return screen

def locate(screen, target, show=bool(0), msg=bool(0)):
    '''
    在背景查找目标图片，并返回查找到的结果坐标列表
    :param screen: 背景截图
    :param target: 要找目标
    :param show:
    :param msg:
    :return:
    '''
    # 截屏起点
    a = 0
    loc_pos = []
    array, treshold, c_name = target[0], target[1], target[2]
    result = cv2.matchTemplate(screen, array, cv2.TM_CCOEFF_NORMED)
    location = numpy.where(result >= treshold)

    if msg:  # 显示正式寻找目标名称，调试时开启
        print(c_name, 'searching... ')

    h, w = array.shape[:-1]  # want.shape[:-1]

    n, ex, ey = 1, 0, 0
    for pt in zip(*location[::-1]):  # 其实这里经常是空的
        x, y = pt[0] + int(w / 2), pt[1] + int(h / 2)
        if (x - ex) + (y - ey) < 15:  # 去掉邻近重复的点
            continue
        ex, ey = x, y

        cv2.circle(screen, (x, y), 10, (0, 0, 255), 3)

        if msg:
            print(c_name, 'we find it !!! ,at', x, y)

        if scalar:
            x, y = int(x) + a, int(y)
        else:
            x, y = int(x) + a, int(y)

        loc_pos.append([x, y])

    if show:  # 在图上显示寻找的结果，调试时开启
        print('Debug: show action.locate')
        cv2.imshow('we get', screen)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    if len(loc_pos) == 0:
        # print(c_name,'not find')
        pass

    return loc_pos

def cheat(p, w, h):
    '''
    随机偏移坐标，防止游戏的外挂检测。p是，w、n是目标图像宽高，返回目标范围内的一个随机坐标

    :param p: 原坐标
    :param w: 目标图像宽
    :param h: 目标图像高
    :return: 目标范围内的一个随机坐标
    '''
    a,b = p
    w, h = int(w/3), int(h/3)
    c,d = random.randint(-w, w),random.randint(-h, h)
    e,f = a + c, b + d
    y = [e, f]
    return(y)

def grab_resolution():
    '''
    获取电脑分辨率
    :return:
    '''
    im = ImageGrab.grab()
    width, height = im.size
    return (width, height)

def click_area_by_key(img_key):
    '''
    根据imgs中的标识图片的key来进行鼠标操作，点击img_key对应的位置
    :param img_key:
    :return:
    '''
    comp_width, comp_height = grab_resolution()
    x0, y0 = (0, 0)
    x1, y1 = (comp_width, comp_height)
    monitor = {"top": x0, "left": y0, "width": x1, "height": y1}
    screen = screenshot(monitor)
    want = imgs[img_key]
    h, w, ___ = want[0].shape
    pts = locate(screen, want, 0)
    if not len(pts) == 0:
        offset_xy = cheat(pts[0], w, h)
        pyautogui.click(offset_xy)
    time.sleep(random.uniform(0.1, 2.0))

def exit_explore_victory_interface(victory_keys):
    '''
    退出探索击败野怪后的胜利界面
    :param victory_marker:
    :param victory_keys:退出需要点击的图片列表，多个图片任意点击一个,其中列表第一个作为判断胜利的标志图片
    :return:
    '''
    from MONITOR_SETTING import monitor
    screen = screenshot(monitor)
    want = imgs['explore_victory1']
    pts = locate(screen, want, 0)
    while len(pts) == 0:
        # print(pts)
        screen = screenshot(monitor)
        want = imgs[victory_keys[0]]
        pts = locate(screen, want, 0)
        if not len(pts) == 0:
            continue
    click_area_by_key(random.choice(victory_keys))
    time.sleep(random.uniform(0.1, 2.0))

def check_target_exist(name_in_imgs):
    '''
    判断某张图像是否存在在截图中，存在返回Ture
    :param name_in_imgs:
    :return: 存在返回Ture，否则返回False
    '''
    from MONITOR_SETTING import monitor
    screen = screenshot(monitor)
    want = imgs[name_in_imgs]
    pts = locate(screen, want, 0)
    if len(pts) == 0:
        return False
    else:
        return True

def hyposthenia():
    '''
    检查体力
    :return: 体力不足返回True，否则返回False
    '''
    from MONITOR_SETTING import monitor
    # 截屏
    screen = screenshot(monitor)

    # 体力不足
    want = imgs['notili']

    pts = locate(screen, want, 0)
    if not len(pts) == 0:
        print('体力不足 ')
        select_mode()
        return True
    else:
        return False
