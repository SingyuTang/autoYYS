import cv2,time,random,os, datetime
import os,sys,pyautogui, traceback
import numpy
import mss
from PIL import ImageGrab
import action
from MONITOR_SETTING import monitor
imgs = action.load_imgs()

########################################################
# 御魂魂土单人
def yuhundanren():
    global last_click
    times = 0
    thereshold = 100000
    run = True
    while run:  # 直到取消，或者出错
        if pyautogui.position()[0] >= pyautogui.size()[0] * 0.98:
            action.select_mode()
        # 体力不足
        if action.hyposthenia() == True:
            break
        print('魂土挑战中。。。')
        while times < thereshold:
            times = times + 1
            print('计数：', times)
            action.click_area_by_key('challenge')
            if action.check_target_exist('jixu') and times < thereshold:
                action.click_area_by_key('jixu')
                continue
            if times >= thereshold:
                run = False
        print('魂土副本完成')

########################################################
# 御魂痴之阵
def yuhun_chizhizhen():
    global last_click
    times = 0
    thereshold = 5000
    while True:  # 直到取消，或者出错
        if pyautogui.position()[0] >= pyautogui.size()[0] * 0.98:
            action.select_mode()
        # 体力不足
        if action.hyposthenia() == True:
            break
        print('御魂痴之阵挑战中。。。')
        while times < thereshold:
            times = times + 1
            print('挑战次数：', times)
            action.click_area_by_key('yuhun_chizhizhen')
            if action.check_target_exist('jixu') and times < thereshold:
                action.click_area_by_key('jixu')
                continue
            if times >= thereshold:
                run = False
        print('痴之阵副本完成')

########################################################
# 御灵
def yuling():
    global last_click
    times = 0
    thereshold = 5000
    while True:  # 直到取消，或者出错
        if pyautogui.position()[0] >= pyautogui.size()[0] * 0.98:
            action.select_mode()
        # 体力不足
        if action.hyposthenia() == True:
            break
        print('御灵挑战中。。。')
        while times < thereshold:
            times = times + 1
            print('挑战次数：', times)
            action.click_area_by_key('yuling_challenge1')
            if action.check_target_exist('yuling_continue2') and times < thereshold:
                action.click_area_by_key('yuling_continue2')
                continue
            if times >= thereshold:
                run = False
        print('御灵副本完成')

########################################################
# 探索单人
def explore_self():
    global last_click
    explore_times = 0
    thereshold = 5000
    count = 0
    run = True
    while run:  # 直到取消，或者出错
        if pyautogui.position()[0] >= pyautogui.size()[0] * 0.98:
            action.select_mode()
        # 体力不足
        if action.hyposthenia() == True:
            break
        # 进入困28
        action.click_area_by_key('c28')
        action.click_area_by_key('tansuo')
        victory_keys = ['explore_victory1','explore_victory2', 'explore_victory3', 'explore_victory4', 'explore_victory5']
        # 设定目标，开始查找
        # 进入后
        print(action.check_target_exist('jian'))
        if action.check_target_exist('jian'):
            print('正在地图中')
            # 向右走两步
            action.click_area_by_key('tuosuo_walk')
            time.sleep(random.uniform(2.5, 4.0))
            action.click_area_by_key('tuosuo_walk')
            isAriseBoss = False     #出现boss则为True
            while isAriseBoss == False:
                # 是否存在boss
                print(action.check_target_exist('boss'))
                if action.check_target_exist('boss') == False:
                    action.click_area_by_key('jian')
                    action.exit_explore_victory_interface(victory_keys)
                    count = count + 1
                    print('胜利次数：', count)
                    continue
                else:
                    action.click_area_by_key('boss')
                    action.exit_explore_victory_interface(victory_keys)
                    count = count + 1
                    print('胜利次数：', count)
                    isAriseBoss = True
                action.click_area_by_key('explore_exit2')
                if action.check_target_exist('exit_explore_popup'):
                    action.click_area_by_key('exit_explore_popup_ok')
                    continue
                else:
                    pass

            time.sleep(random.uniform(5.0, 7.0))
            explore_times = explore_times + 1
            print('探索次数：{}'.format(explore_times))
            if explore_times < thereshold:
                continue
            else:
                run = False
        else:
            print('jian格式不对，未进入探索...')
            run = False


########################################################
# 觉醒单人
def awakening():
    global last_click
    times = 0
    thereshold = 100000
    run = True
    while run:  # 直到取消，或者出错
        if pyautogui.position()[0] >= pyautogui.size()[0] * 0.98:
            action.select_mode()
        # 体力不足
        if action.hyposthenia() == True:
            break
        print('觉醒挑战中。。。')
        while times < thereshold:
            times = times + 1
            print('挑战次数：', times)
            action.click_area_by_key('awakening_challenge2')
            if action.check_target_exist('jixu') and times < thereshold:
                action.click_area_by_key('jixu')
                continue
            if times >= thereshold:
                run = False
    print('觉醒副本完成')