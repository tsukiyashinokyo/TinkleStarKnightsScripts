from autoFunction import simple_function
from autoFunction import composite_function
from . import globals
import time
import sys
from ScriptsGui import globals as gui_globals
from .common_exploration import common_battle_loop

#进入任务页面模块
def enter_the_mission_interface(quest_type,exploration_flag = True):

    while True:
        composite_function.error_occurrence()  # Error出现检测，会导致线程停止

        simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'quest.png')
        simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'quest_mission.png')

        #检测是否进入任务选择界面
        success,_,_,_ = simple_function.simple_picture_detection(globals.TARGET_PICTURE_FOLDER_PATH / 'mission_interface.png')
        if success:
            break
        time.sleep(globals.loop_sleep_time)

    #难度选择
    while True:
        composite_function.error_occurrence()
        if quest_type == 'normal':
            success, _, _, _ = simple_function.simple_picture_detection(globals.TARGET_PICTURE_FOLDER_PATH / 'blue_normal.png')
            if success:
                break
            else:
                simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'white_normal.png')

        if quest_type == 'hard':
            success, _, _, _ = simple_function.simple_picture_detection(globals.TARGET_PICTURE_FOLDER_PATH / 'blue_hard.png')
            if success:
                break
            else:
                simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'white_hard.png')
        time.sleep(globals.loop_sleep_time)
    if exploration_flag:#开荒标志，false时不选择关卡，只是进入界面
        #找到能打的关卡为止
        quest_search()
#切换章节，找到能挑战的关卡为止
def quest_search():
    while True:
        composite_function.error_occurrence()
        success,_,_,_ = simple_function.simple_picture_detection(globals.TARGET_PICTURE_FOLDER_PATH / 'unfinished.png')
        if success:
            return True
        else:
            time.sleep(globals.loop_sleep_time)
            #再查找一次
            success, _, _, _ = simple_function.simple_picture_detection(globals.TARGET_PICTURE_FOLDER_PATH / 'unfinished.png')
            if not success:
                #还没找到就切换章节
                simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'left_arrow.png',threshold=0.8)
            else:
                return True
#关卡选择+战斗模块

#主线战斗！
def main_quest(quest_type):
    gui_globals.script_thread_flag = True
    #返回主界面
    composite_function.return_home()
    #进入任务页面
    enter_the_mission_interface(quest_type)
    #选择关卡并战斗
    common_battle_loop()

    gui_globals.script_thread_flag = False

