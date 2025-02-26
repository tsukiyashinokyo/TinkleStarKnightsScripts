from autoFunction import simple_function
from autoFunction import composite_function
from . import globals
import time
import sys
from ScriptsGui import globals as gui_globals
from .common_exploration import common_tower

#进入新月塔模块
def enter_moon_tower():

    while(True):
        composite_function.error_occurrence()# 连接异常检测
        simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'quest.png')
        simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'feenis_tower.png')
        simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'moon_tower.png')
        success,_,_,_ = simple_function.simple_picture_detection(globals.TARGET_PICTURE_FOLDER_PATH / 'battle_ready.png')
        if success:
            return True
        time.sleep(globals.loop_sleep_time)


#新月塔开荒
def moon_tower():
    gui_globals.script_thread_flag = True #与gui页面相关，防止复数脚本启动
    # 返回主界面
    composite_function.return_home()
    # 进入新月塔
    enter_moon_tower()
    #战斗
    common_tower()

    gui_globals.script_thread_flag = False