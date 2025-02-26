import json
from . import globals
from pathlib import Path


settings = globals.default_settings

#json路径
setting_json_path = Path(__file__).parent.parent / 'jsonFolder'

#按照载入的设置字典设置
def explorationTask_global_set(settings_dic):
    globals.battle_sleep_time = float(settings_dic['battle_sleep_time'])
    globals.loop_sleep_time = float(settings_dic['loop_sleep_time'])
    globals.gui_settings = settings_dic
#载入json配置
def explorationTask_global_load():
    global settings
    global default_settings
    try:
        if not setting_json_path.exists():
            setting_json_path.mkdir(parents=True, exist_ok=True)
        json_file_path = setting_json_path / 'explorationTask_setting.json'
        if json_file_path.exists():
            #json文件存在则载入json的配置
            with json_file_path.open('r') as json_file:
                settings = json.load(json_file)
                explorationTask_global_set(settings)
        else:
            #json文件不存在则以默认生成一份json文件
            with json_file_path.open('w') as json_file:
                json.dump(default_settings, json_file, indent=4)
                explorationTask_global_set(settings)
    except Exception as e:
        print(e)