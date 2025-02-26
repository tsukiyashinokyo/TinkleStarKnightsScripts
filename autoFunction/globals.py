from pathlib import Path
import cv2


#默认配置字典
default_settings = {
    'explanation':'自动函数库设置',
    'adb_path':r'D:\mumu\MuMuPlayer-12.0\shell\adb.exe', #adb.exe所在目录
    'adb_port':16384, #adb端口号
    'default_threshold' : 0.9, #单匹配时的精度
    'default_multiple_matches_threshold' : 0.9, #多匹配时的精度
    'default_click_sleep' : 2, #点击间隔时间
    'default_max_offset' : 3, #点击等的最大偏移
    'default_duration' : 200, #滑动默认时间，单位毫秒
    'loop_sleep_time' : 0.5, #每个小模块的睡眠时间
    'default_energy_recovery_order' : -1, #恢复体力的磕药顺序，默认从后往前，改为0则从前往后(包括钻)
    'default_if_recover' : True, #是否自动回复体力
    'default_detect_sleep' : 0.1,# 探测图片间隔
    'default_error_times_limit' : 100, #没识别到图片多少次后退出脚本
    'default_swipe_sleep':1
}

#gui显示字典
gui_settings = default_settings

#gui解说字典
explanation_dic={
    'adb_path': 'adb.exe所在目录',  # adb.exe所在目录
    'adb_port': 'adb端口号',  # adb端口号
    'default_threshold': '单图匹配时的精度',  # 单匹配时的精度
    'default_multiple_matches_threshold': '多图匹配时的精度',  # 多匹配时的精度
    'default_click_sleep': '点击间隔时间',  # 点击间隔时间
    'default_max_offset': '点击位置的最大偏移,单位像素',  # 点击等的最大偏移
    'default_duration': '滑动操作默认时间，单位毫秒(其他时间单位都是秒)',  # 滑动默认时间，单位毫秒
    'loop_sleep_time': '每轮检测循环后的睡眠时间',  # 每轮检测循环后的睡眠时间
    'default_energy_recovery_order': '恢复体力的磕药顺序，默认从后往前，改为0则从前往后(包括钻)',  # 恢复体力的磕药顺序，默认从后往前，改为0则从前往后(包括钻)
    'default_if_recover': '是否自动回复体力(True/False)不区分大小写',  # 是否自动回复体力
    'default_detect_sleep': '探测图片间隔',  # 探测图片间隔
    'default_error_times_limit': '没识别到图片多少次后退出脚本',  # 没识别到图片多少次后退出脚本
    'default_swipe_sleep':'滑动后等待时间'
}


adb_path = Path(r'D:\mumu\MuMuPlayer-12.0\shell\adb.exe') #adb.exe所在目录
adb_port = '16384' #adb端口号
default_threshold = 0.9 #单匹配时的精度
default_multiple_matches_threshold = 0.9 #多匹配时的精度
default_cv2_method = cv2.TM_CCOEFF_NORMED #模板识别方法
default_click_sleep = 2 #点击间隔时间
default_max_offset = 3 #点击等的最大偏移
default_duration = 200 #滑动默认时间，单位毫秒
TARGET_PICTURE_FOLDER_PATH = Path(__file__).parent.parent / 'targetPictures' #目标图片所在文件夹
loop_sleep_time = 0.5 #每个小模块的睡眠时间
default_energy_recovery_order = -1 #恢复体力的磕药顺序，默认从后往前，改为0则从前往后(包括钻)
default_if_recover = True #是否自动回复体力
default_detect_sleep = 0.1# 探测图片间隔
default_error_times_limit = 100 #没识别到图片多少次后退出脚本
error_count = 0 #未识别到的图片的次数，随识别成功清零
auto_mode = False #自动战斗是否打开了的标识
default_swipe_sleep = 1 #滑动后睡眠时间