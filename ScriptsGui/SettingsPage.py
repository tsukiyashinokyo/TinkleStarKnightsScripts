import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from . import  utils
from autoFunction import globals as auto_globals
from explorationTask import globals as exploration_globals
from autoFunction import global_set as auto_global_set
from explorationTask import global_set as exploration_global_set

def get_frame(notebook):

    frame = ttk.Frame(notebook)
    label_frame1 ,entries1 ,string_vars1  = utils.get_label_and_entry(frame,auto_globals.gui_settings,auto_globals.explanation_dic)
    label_frame1.pack(side = TOP,fill=BOTH, expand=True, padx=5, pady=5)

    change_button1 = ttk.Button(frame, text="修改自动函数库设置", command=lambda : utils.change_setting(entries1,string_vars1,str(1)))
    change_button1.pack(side = TOP,fill=BOTH, expand=True, padx=5, pady=5)

    label_frame2, entries2, string_vars2 = utils.get_label_and_entry(frame, exploration_globals.gui_settings,exploration_globals.explanation_dic)
    label_frame2.pack(side = TOP,fill=BOTH, expand=True, padx=5, pady=5)

    change_button2 = ttk.Button(frame, text="修改开荒库设置", command=lambda : utils.change_setting(entries2,string_vars2,str(2)))
    change_button2.pack(side = TOP,fill=BOTH, expand=True, padx=5, pady=5)

    return frame

