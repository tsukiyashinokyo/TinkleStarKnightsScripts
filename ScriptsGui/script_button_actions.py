from explorationTask.main_quest import main_quest
from explorationTask.moon_tower import moon_tower
from routine.routine_mission import routine_coin
from routine.routine_mission import routine_exp
from routine.routine_mission import routine_skill
from routine.routine_mission import routine_material
from routine.routine_mission import get_reward
from routine.routine_mission import routine_equipment
from routine.routine_mission import routine_main
from explorationTask.common_exploration import *
import threading
from ScriptsGui.utils import *
from ScriptsGui import globals


def main_quest_button_action(str):
    if not globals.script_thread_flag:
        thread = threading.Thread(target=lambda :main_quest(quest_type=str))
        thread.start()
        show_dialog_success('主线开荒已启动')
        print('主线开荒已启动')
        return True
    else:
        show_dialog_fail('已经有脚本正在运行，无法多启动脚本')
        print('已经有脚本正在运行，无法多启动脚本')
        return False

def moon_tower_button_action():
    if not globals.script_thread_flag:
        thread = threading.Thread(target=moon_tower)
        thread.start()
        show_dialog_success('新月塔开荒已启动')
        print('新月塔开荒已启动')
        return True
    else:
        show_dialog_fail('已经有脚本正在运行，无法多启动脚本')
        print('已经有脚本正在运行，无法多启动脚本')
        return False

def routine_mission(intvar_list,element):
    globals.script_thread_flag = True
    for i in range(len(intvar_list)):
        intvar = intvar_list[i]
        if intvar.get():
            if i==0:
                routine_exp()
            elif i==1:
                routine_coin()
            elif i==2:
                routine_equipment()
            elif i==3:
                routine_skill()
            elif i==4:
                routine_material(element)
            elif i==5:
                routine_main()
            elif i==6:
                get_reward()
    globals.script_thread_flag = False
    return True

def routine_mission_thread(intvar_list,element):
    if not globals.script_thread_flag:
        thread = threading.Thread(target=lambda:routine_mission(intvar_list,element))
        thread.start()
        show_dialog_success('选中的日常任务已启动')
        print('选中的日常任务已启动')
        return True
    else:
        show_dialog_fail('已经有脚本正在运行，无法多启动脚本')
        print('已经有脚本正在运行，无法多启动脚本')
        return False

def exploration_tower():
    if not globals.script_thread_flag:
        thread = threading.Thread(target=common_tower)
        thread.start()
        show_dialog_success('塔型开荒已启动')
        print('塔型开荒已启动')
        return True
    else:
        show_dialog_fail('已经有脚本正在运行，无法多启动脚本')
        print('已经有脚本正在运行，无法多启动脚本')
        return False

def exploration_energy():
    if not globals.script_thread_flag:
        thread = threading.Thread(target=common_battle_loop)
        thread.start()
        show_dialog_success('体力型开荒已启动')
        print('体力型开荒已启动')
        return True
    else:
        show_dialog_fail('已经有脚本正在运行，无法多启动脚本')
        print('已经有脚本正在运行，无法多启动脚本')
        return False