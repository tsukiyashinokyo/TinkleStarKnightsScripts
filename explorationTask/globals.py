from pathlib import Path
#默认设置字典
default_settings = {
    'explanation':'开荒库设置',
    'battle_sleep_time' : 3,#检测到战斗时的睡眠时间
    'loop_sleep_time' : 1 #每个小模块的睡眠时间
}

#gui显示字典
gui_settings = default_settings.copy()

#gui显示解说字典
explanation_dic = {
    'battle_sleep_time' : '检测到战斗时的睡眠时间',#检测到战斗时的睡眠时间
    'loop_sleep_time' : '每轮检测循环后的睡眠时间' #每轮检测循环后的睡眠时间
}


TARGET_PICTURE_FOLDER_PATH = Path(__file__).parent.parent / 'targetPictures' #目标图片所在文件夹
battle_sleep_time = 3 #检测到战斗时的睡眠时间
loop_sleep_time = 1 #每个小模块的睡眠时间
in_battle = False #是否处于战斗中