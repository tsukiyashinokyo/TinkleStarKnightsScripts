import time
from autoFunction import simple_function
from autoFunction import composite_function
from . import globals
from explorationTask.globals import loop_sleep_time
from explorationTask.main_quest import enter_the_mission_interface

#日常金币关
def routine_coin():
    #进入quest页面
    composite_function.enter_quest_interface()

    #进入金币关
    while True:
        simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'patrol.png')
        simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'coin_get.png')
        if simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'finished.png',single_match=False,click_number=0):
            break
        composite_function.error_occurrence()
        time.sleep(loop_sleep_time)

    #跳过
    composite_function.skip(globals.TARGET_PICTURE_FOLDER_PATH / 'coin_get.png')
    #返回主页
    composite_function.return_home()
    print('金币关已完成')
    return True

#日常经验关
def routine_exp():
    # 进入quest页面
    composite_function.enter_quest_interface()

    # 进入经验关
    while True:
        simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'patrol.png')
        simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'exp_get.png')
        if simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'finished.png',single_match=False,click_number=0):
            break
        composite_function.error_occurrence()
        time.sleep(loop_sleep_time)

    # 跳过
    composite_function.skip(globals.TARGET_PICTURE_FOLDER_PATH / 'exp_get.png')
    # 返回主页
    composite_function.return_home()
    print('经验关已完成')
    return True

#日常装备关
def routine_equipment():
    # 进入quest页面
    composite_function.enter_quest_interface()

    # 进入经验关
    while True:
        simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'cooperative_drill.png')
        simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'equipment.png')
        if simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'finished.png', single_match=False,click_number=0):
            break
        composite_function.error_occurrence()
        time.sleep(loop_sleep_time)

    # 跳过
    composite_function.skip(globals.TARGET_PICTURE_FOLDER_PATH / 'equipment.png')
    # 返回主页
    composite_function.return_home()
    print('装备关已完成')
    return True

#日常技能关
def routine_skill():
    # 进入quest页面
    composite_function.enter_quest_interface()

    # 进入技能关
    while True:
        simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'cooperative_drill.png')
        simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'skill.png')
        if simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'finished.png',single_match=False,click_number=0):
            break
        composite_function.error_occurrence()
        time.sleep(loop_sleep_time)

    # 跳过
    composite_function.skip(globals.TARGET_PICTURE_FOLDER_PATH / 'skill.png')
    # 返回主页
    composite_function.return_home()
    print('技能关已完成')
    return True

#日常材料关
def routine_material(element):

    # 进入quest页面
    composite_function.enter_quest_interface()

    #滑动方向标志，False向下，滑动关卡列表以找到对应属性
    turn_flag = False

    # 进入对应材料关
    while True:
        simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'cooperative_drill.png')
        simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'material.png')

        #滑动关卡列表以防找不到关卡
        if not turn_flag:
            simple_function.simple_swipe(globals.TARGET_PICTURE_FOLDER_PATH / 'thunder.png',x_offset=0,y_offset=100)
            turn_flag = True
        else:
            simple_function.simple_swipe(globals.TARGET_PICTURE_FOLDER_PATH / 'thunder.png',x_offset=0,y_offset=-100)
            turn_flag = False

        print(turn_flag)

        simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / globals.material_dic[element])

        if simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'finished.png',single_match=False,click_number=0):
            break
        composite_function.error_occurrence()
        time.sleep(loop_sleep_time)

    # 跳过
    composite_function.skip(globals.TARGET_PICTURE_FOLDER_PATH / 'material.png')
    # 返回主页
    composite_function.return_home()
    print('日常材料关已完成')
    return True

#日常主线关
def routine_main():
    #返回
    composite_function.return_home()
    #进入主线关
    enter_the_mission_interface('normal',exploration_flag=False)

    #点击最高关卡(如果本页没有就换页)
    while True:
        if simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'finished.png',single_match=False,click_number=0):
            pass
        else:
            success,_,_,_ = simple_function.simple_picture_detection(globals.TARGET_PICTURE_FOLDER_PATH / 'unfinished.png')
            if success:
                simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'left_arrow.png')

        success,_,_,_ = simple_function.simple_picture_detection(globals.TARGET_PICTURE_FOLDER_PATH / 'main_quest_skip_symbol.png')
        if success:
            break
        time.sleep(loop_sleep_time)

    #跳过
    composite_function.skip(globals.TARGET_PICTURE_FOLDER_PATH / 'main_quest_skip_symbol.png',False)
    #返回
    composite_function.return_home()
    print('日常主线关已结束')

#领取奖励
def get_reward():

    composite_function.return_home()

    #进入领奖界面
    while True:
        simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'check_mark.png')
        success, _, _, _ = simple_function.simple_picture_detection(
            globals.TARGET_PICTURE_FOLDER_PATH / 'daily.png')
        if success:
            break
        time.sleep(loop_sleep_time)

    #领奖
    success, _, _, _ = simple_function.simple_picture_detection(
        globals.TARGET_PICTURE_FOLDER_PATH / 'not_get_over.png')
    while success:
        simple_function.simple_click(globals.TARGET_PICTURE_FOLDER_PATH / 'all_get.png')
        composite_function.close_click()
        success, _, _, _ = simple_function.simple_picture_detection(
            globals.TARGET_PICTURE_FOLDER_PATH / 'not_get_over.png')

    composite_function.return_home()
    print('已成功领取奖励')
    return True


