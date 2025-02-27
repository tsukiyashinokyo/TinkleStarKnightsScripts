from autoFunction import simple_function
from autoFunction import composite_function
from . import globals
import time
import sys
from ScriptsGui import globals as gui_globals

#爬塔型战斗
def common_tower():
    gui_globals.script_thread_flag = True
    while True:

        if not globals.in_battle:  # 不在战斗时才选择战斗
            simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'battle_ready.png')
            simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'quest_mission_battle.png')

        success, _, _, _ = simple_function.simple_picture_detection(globals.TARGET_PICTURE_FOLDER_PATH / 'pause.png')
        if success:
            composite_function.auto_mode() #没有自动战斗的话启用自动战斗
            globals.in_battle = True  # 说明正在战斗
            time.sleep(globals.battle_sleep_time)

        # 战斗结束
        if globals.in_battle:  # 没在战斗时不检测战斗完成
            #战斗没完成确检测到了再战，说明输了
            success, _, _, _ = simple_function.simple_picture_detection(
                globals.TARGET_PICTURE_FOLDER_PATH / 'battle_ready.png')
            if success:
                gui_globals.script_thread_flag = False
                globals.in_battle = False
                print("打不过当前关卡！脚本已退出")
                sys.exit()

            simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'win.png')
            simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'tap_tsuki.png')

        # 不论如何都执行，以防虚点击导致卡死
        if simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'tsuki.png'):
            globals.in_battle = False  # 战斗结束

        composite_function.close_click() #点击关闭按钮,自带连接异常检测

        time.sleep(globals.loop_sleep_time)

#消耗体力类型的战斗
def common_battle_loop():
    gui_globals.script_thread_flag = True
    while True:

        if not globals.in_battle:  # 不在战斗时才选择关卡
            simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'unfinished.png')
            simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'quest_mission_battle.png')

        # 检测打架界面的暂停键，检测到说明进入了打架界面，休息两秒等战斗再检测
        success, _, _, _ = simple_function.simple_picture_detection(globals.TARGET_PICTURE_FOLDER_PATH / 'pause.png')
        if success:
            composite_function.auto_mode() #没有自动战斗的话启用自动战斗
            globals.in_battle = True  # 说明正在战斗
            time.sleep(globals.battle_sleep_time)

        # 战斗结束
        if globals.in_battle:  # 没在战斗时不检测战斗完成
            simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'win.png')
            simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'tap_tsuki.png')
            success,_,_,_ = simple_function.simple_picture_detection(globals.TARGET_PICTURE_FOLDER_PATH / 'finished.png')
            if success:
                gui_globals.script_thread_flag = False
                globals.in_battle = False
                print("打不过当前关卡！脚本已退出")
                sys.exit()


        # 不论如何都执行，以防虚点击导致卡死
        if simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'tsuki.png'):
            globals.in_battle = False  # 战斗结束

        composite_function.energy_recovery()  # 恢复体力

        #关闭购买广告并检查连接错误
        composite_function.close_click()
        time.sleep(globals.loop_sleep_time)
