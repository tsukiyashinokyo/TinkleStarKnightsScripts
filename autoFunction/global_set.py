import json
from  pathlib import Path
from . import globals

settings = globals.default_settings

#json路径
setting_json_path = Path(__file__).parent.parent / 'jsonFolder'

#按照载入的设置字典设置
def autoFunction_global_set(settings_dic):
    globals.adb_path = Path(settings_dic['adb_path'])
    globals.adb_port = str(settings_dic['adb_port'])
    globals.default_threshold = float(settings_dic['default_threshold'])
    globals.default_multiple_matches_threshold = float(settings_dic['default_multiple_matches_threshold'])
    globals.default_click_sleep = float(settings_dic['default_click_sleep'])
    globals.default_max_offset = int(settings_dic['default_max_offset'])
    globals.default_duration = int(settings_dic['default_duration'])
    globals.loop_sleep_time = float(settings_dic['loop_sleep_time'])
    globals.default_energy_recovery_order = int(settings_dic['default_energy_recovery_order'])
    globals.default_if_recover = (settings_dic['default_if_recover'].lower() == 'true')
    globals.default_detect_sleep = float(settings_dic['default_detect_sleep'])
    globals.default_error_times_limit = int(settings_dic['default_error_times_limit'])
    globals.default_swipe_sleep = int(settings_dic['default_swipe_sleep'])
    globals.gui_settings = settings_dic


#载入json配置
def autoFunction_global_load():
    global settings
    try:
        if not setting_json_path.exists():
            setting_json_path.mkdir(parents=True, exist_ok=True)
        json_file_path = setting_json_path / 'autoFunction_setting.json'
        if json_file_path.exists():
            #json文件存在则载入json的配置
            with json_file_path.open('r') as json_file:
                settings = json.load(json_file)
                autoFunction_global_set(settings)
        else:
            #json文件不存在则以默认生成一份json文件
            with json_file_path.open('w') as json_file:
                json.dump(globals.default_settings, json_file, indent=4)
                autoFunction_global_set(settings)
    except Exception as e:
        print('错误！')
        print(e)

