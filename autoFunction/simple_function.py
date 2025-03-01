import subprocess
import sys

import cv2
from pathlib import Path
import random
from . import globals
import time
import numpy as np
import gc
#adb点击命令(无需关心)
def adb_click(x,y,sleeptime=globals.default_click_sleep,max_offset=globals.default_max_offset):

    adb_command_str = str(globals.adb_path) +' -s127.0.0.1:'+globals.adb_port

    random_x = x + random.randint(-max_offset, max_offset) #点击偏移
    random_y = y + random.randint(-max_offset, max_offset)

    command = f"{adb_command_str} shell input tap {random_x} {random_y}"

    subprocess.run(command, capture_output=True, text=True, shell=True, check=True)
    time.sleep(sleeptime)
    return True
# 截图(获取识别区域)
def simple_screen_shot():
    adb_command_str = f'"{str(globals.adb_path)}" -s 127.0.0.1:' + globals.adb_port
    # 获取截图并将其保存在内存中
    result = subprocess.run(f"{adb_command_str} exec-out screencap -p", capture_output=True, check=True)
    # 将截图数据加载到OpenCV中
    image_data = np.frombuffer(result.stdout, dtype=np.uint8)
    screenshot = cv2.imdecode(image_data, cv2.IMREAD_COLOR)
    return screenshot

# 在屏幕上检测图片
def simple_picture_detection(target_path, threshold=globals.default_threshold, cv_method=globals.default_cv2_method,
                              single_match=True, multiple_matches_threshold=globals.default_multiple_matches_threshold):
    time.sleep(globals.default_detect_sleep)
    screenshot = simple_screen_shot()  # 获取屏幕截图
    target_image = cv2.imread(target_path)  # 读取目标图片

    result = cv2.matchTemplate(screenshot, target_image, cv_method)  # 识别
    if single_match:  # 单匹配
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)  # 获取最小最大相似位置的起点和值
        if max_val >= threshold:
            print(f'成功识别到图像{target_path}')
            del screenshot  # 删除截图对象
            gc.collect()  # 强制进行垃圾回收
            globals.error_count = 0
            return True, max_loc, target_image.shape[1], target_image.shape[0]  # 返回位置，宽，高
        else:
            print(f'无法识别到图像{target_path}')
            del screenshot  # 删除截图对象
            gc.collect()  # 强制进行垃圾回收
            globals.error_count += 1
            if globals.error_count >= globals.default_error_times_limit:
                print('识别错误次数过多，脚本已退出')
                sys.exit(0)
            return False, None, None, None
    else:  # 多匹配
        locations = np.where(result >= multiple_matches_threshold)
        locs = tuple(zip(*locations[::-1]))  # 将([y_list][x_list])格式转化成((x1,y1),(x2,y2)......)格式
        if len(locs) > 0:
            print(f'成功识别到图像{target_path}')
            del screenshot  # 删除截图对象
            gc.collect()  # 强制进行垃圾回收
            globals.error_count = 0
            return True, locs, target_image.shape[1], target_image.shape[0]  # locs为所有匹配位置,格式为(x,y)的元组
        else:
            print(f'无法识别到图像{target_path}')
            del screenshot  # 删除截图对象
            gc.collect()  # 强制进行垃圾回收
            globals.error_count += 1
            if globals.error_count >= globals.default_error_times_limit:
                sys.exit(0)
                print('识别错误次数过多，脚本已退出')
            return False, None, None, None
#点击图片
def simple_click(target_path,  #目标图像路径
                 sleeptime=globals.default_click_sleep,  #点击间隔时间
                 threshold=globals.default_threshold,  #精度
                 cv_method=globals.default_cv2_method,#图像匹配方法
                 single_match = True, #是否单匹配（多匹配仍然是单点击）
                 click_number = -1, #点击第几个匹配到的图像,（-1为最后一个,0表示第一个，序号从0开始）,匹配到的图片顺序在界面从左到右,从上到下
                 multiple_matches_threshold = globals.default_multiple_matches_threshold,#多匹配时的匹配精度
                 x_offset=0,#图片中心x轴偏移
                 y_offset=0,):#图片中心y轴偏移

    if single_match:
        success,max_loc,width,height = simple_picture_detection(target_path=target_path, threshold=threshold, cv_method=cv_method)
    else:
        success,locs,width,height = simple_picture_detection(target_path=target_path, threshold=threshold, cv_method=cv_method,single_match=single_match,multiple_matches_threshold=multiple_matches_threshold)

    if success:
        if single_match:#单匹配时
            center_x = max_loc[0] + width // 2 +x_offset
            center_y = max_loc[1] + height // 2 +y_offset#这两条是设定点击点在图像中心,和点击点距离中心的偏移
            print(f'点击图像{target_path}')
        else:#多匹配时
            if click_number > len(locs):
                print(f'你所所选择的匹配图像点击序号越界!,当前只匹配到{len(locs)}个图像,序号为0-{len(locs)-1}')
                return False
            else:
                center_x = locs[click_number][0] + width // 2 +x_offset
                center_y = locs[click_number][1] + height // 2 +y_offset
                print(f'点击图像{target_path}的{"最后1" if click_number == -1 else "第" + str(click_number)}个匹配')
        return adb_click(center_x, center_y, sleeptime)
    else:
        print(f'无法点击到图像{target_path}')
        return False

#连接模拟器并检测是否连接成功
def adb_connection_and_check():
    adb_command_str = str(globals.adb_path) + ' -s 127.0.0.1:' + globals.adb_port
    print(f"执行的 ADB 命令地址：{adb_command_str}")
    subprocess.run(str(globals.adb_path) + ' connect 127.0.0.1:'+globals.adb_port
                   , capture_output=True, text=True, shell=True, check=True)
    result = subprocess.run(adb_command_str + ' get-state', capture_output=True, text=True)
    if "device" in result.stdout:
        print("设备已成功连接！")
    else:
        print("未检测到设备，请检查连接。")


#滑动
def adb_swipe(x1,y1,x2,y2,duration=globals.default_duration,max_offset=globals.default_max_offset,sleeptime = globals.default_swipe_sleep):
    adb_command_str = f'"{str(globals.adb_path)}" -s 127.0.0.1:{globals.adb_port}'

    #随机偏移
    random_r1 = random.randint(-max_offset, max_offset)
    random_r2 = random.randint(-max_offset, max_offset)

    command = f"{adb_command_str} shell input swipe {x1 + random_r1} {y1 + random_r2} {x2 + random_r1} {y2 - random_r2} {duration}"
    subprocess.run(command, capture_output=True, text=True, shell=True, check=True)

    time.sleep(sleeptime)
    return True
#根据图像位置滑动
def simple_swipe(target_path,x_offset,y_offset,duration=globals.default_duration,max_offset=globals.default_max_offset,sleeptime = globals.default_swipe_sleep):
    success,loc,width,height = simple_picture_detection(target_path=target_path)
    if success:
        x1 = loc[0] + width // 2
        y1 = loc[1] + height // 2
        adb_swipe(x1,y1,x1+x_offset,y1+y_offset,duration=duration,max_offset=max_offset,sleeptime = sleeptime)
        print(f'成功滑动')
        return True
    else:
        print(f'无法检测到图像{target_path}，以至于无法滑动')
        return False