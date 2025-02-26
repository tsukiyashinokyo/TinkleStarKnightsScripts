from . import globals
from . import simple_function
import time
import sys
from ScriptsGui import globals as gui_globals
#返回主界面
def return_home():
    while True:
        close_click()#防止公告挡住

        simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'go_back.png')
        simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'home_button.png')
        success,_,_,_, = simple_function.simple_picture_detection(globals.TARGET_PICTURE_FOLDER_PATH / 'home_success.png')
        if success:
            return True

        time.sleep(globals.loop_sleep_time)

#进入quest页面
def enter_quest_interface():
    #返回主页面
    return_home()
    while True:
        error_occurrence()  # Error出现检测，会导致线程停止
        simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'quest.png')
        #检测是否进入任务选择界面
        success,_,_,_ = simple_function.simple_picture_detection(globals.TARGET_PICTURE_FOLDER_PATH / 'orange_quest.png')
        if success:
            break
        time.sleep(globals.loop_sleep_time)
    return True

#参数是跳过后返回的页面标志图片
def skip(symbol_picture_path,max_clear=True):
    error_occurrence()
    # 跳过
    while True:
        skip_over_flag = False  # 是否已经逃过的标志
        simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'yellow_skip.png')
        if max_clear:#是否点击max（即扫荡所有次数）
            simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'yellow_max.png')
        if simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'certain.png'):
            skip_over_flag = True
        simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'tap_tsuki.png')
        success,_,_,_ = simple_function.simple_picture_detection(symbol_picture_path)
        if success and skip_over_flag:
            break
        close_click()#关闭广告，检测连接错误
        time.sleep(globals.loop_sleep_time)
    return True

#游戏出错检测（一般是连接断开之后）
def error_occurrence():
    success,_,_,_ =simple_function.simple_picture_detection(globals.TARGET_PICTURE_FOLDER_PATH / 'error.png',threshold=0.8)
    success2,_,_,_ =simple_function.simple_picture_detection(globals.TARGET_PICTURE_FOLDER_PATH / 'error2.png',threshold=0.8)
    if success or success2:
        print("游戏连接断开了，脚本已自动退出")
        gui_globals.script_thread_flag = False #表示脚本不在运行
        sys.exit()

#检测并关闭公告等
def close_click():
    error_occurrence()#连接异常检测
    simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'close.png')
    simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'guanggao.png')


#如果自动战斗没开，则打开自动战斗
def auto_mode():
    if globals.auto_mode:
        return True
    else:
        success,_,_,_ =simple_function.simple_picture_detection(globals.TARGET_PICTURE_FOLDER_PATH / 'blue_auto.png')
        while not success:
            simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'white_auto.png')
            error_occurrence()  #
            time.sleep(globals.loop_sleep_time)
            success, _, _, _ = simple_function.simple_picture_detection(globals.TARGET_PICTURE_FOLDER_PATH / 'blue_auto.png')
        globals.auto_mode = True
        return True

#是否恢复体力（默认从后往前吃,即先药后钻）
def energy_recovery(if_recover = globals.default_if_recover #是否恢复体力
                    ,order = globals.default_energy_recovery_order): #磕药顺序
    success,_,_,_ = simple_function.simple_picture_detection(globals.TARGET_PICTURE_FOLDER_PATH / 'energy_recovery.png')
    if success and if_recover:
        #多匹配,点击指定序号的匹配图像
        simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'use.png',
                                     single_match=False,
                                     click_number=order)
        simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'sure.png',)
        close_click()
    elif success and not if_recover:
        while success:#判断是否退出了吃药界面
            #关闭吃药界面
            close_click()
            success, _, _, _ = simple_function.simple_picture_detection(globals.TARGET_PICTURE_FOLDER_PATH / 'energy_recovery.png')

        #退出战斗确认界面
        simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'go_back.png')
        success,_,_,_ = simple_function.simple_picture_detection(globals.TARGET_PICTURE_FOLDER_PATH / 'home_button.png')
        if not success:
            simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'go_back.png')
        #返回主界面
        return_home()
        print('体力已经耗尽，脚本自动退出')
        gui_globals.script_thread_flag = False #表示脚本不在运行
        sys.exit()


