import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ScriptsGui.script_button_actions import *
from . import  utils

def get_frame(notebook):

    frame = ttk.Frame(notebook)

    top_label1 = ttk.Label(frame, text="内容" ,anchor= CENTER,borderwidth=2, relief="solid")
    top_label2 = ttk.Label(frame, text='可选项' ,anchor= CENTER,borderwidth=2,relief="solid")
    top_label3 = ttk.Label(frame, text='开始按钮' ,anchor= CENTER,borderwidth=2,relief="solid")

    top_label1.grid(row=0, column=0,padx=1, pady=0, sticky=EW)
    top_label2.grid(row=0, column=1,padx=1, pady=0, sticky=EW)
    top_label3.grid(row=0, column=2,padx=1, pady=0, sticky=EW)

    main_quest_label = ttk.Label(frame,text='主线开荒',anchor= CENTER)
    main_quest_combobox = ttk.Combobox(
        master = frame,
        font = ('微软雅黑',12),
        values=['normal','hard'],
        justify = CENTER,
    )
    main_quest_combobox.current(0)
    main_quest_button = ttk.Button(frame,text='启动',command=lambda: main_quest_button_action(main_quest_combobox.get()))

    main_quest_label.grid(row=1, column=0,padx=10, pady=10, sticky=EW)
    main_quest_combobox.grid(row=1,column=1,padx=10, pady=10, sticky=EW)
    main_quest_button.grid(row=1,column=2,padx=10, pady=10, sticky=EW)

    moon_tower_label = ttk.Label(frame,text='新月塔开荒',anchor= CENTER)
    moon_tower_button = ttk.Button(frame,text='启动',command=moon_tower_button_action)

    moon_tower_label.grid(row=2, column=0,padx=10, pady=10, sticky=EW)
    moon_tower_button.grid(row=2, column=2,padx=10, pady=10, sticky=EW)

    exp_intvar = ttk.IntVar(frame,value=0)
    coin_intvar = ttk.IntVar(frame,value=0)
    equipment_intvar = ttk.IntVar(frame,value=0)
    skill_intvar = ttk.IntVar(frame,value=0)
    material_intvar = ttk.IntVar(frame,value=0)
    main_quest_intvar = ttk.IntVar(frame,value=0)
    get_reward_intvar = ttk.IntVar(frame,value=0)
    intvar_list = [exp_intvar,coin_intvar,equipment_intvar,skill_intvar,material_intvar,main_quest_intvar,get_reward_intvar]

    ttk.Checkbutton(frame,text='经验关',variable=exp_intvar,bootstyle="square-toggle").grid(row=3,column=0,padx=10, pady=10)
    ttk.Checkbutton(frame,text='金币关',variable=coin_intvar,bootstyle="square-toggle").grid(row=4,column=0,padx=10, pady=10)
    ttk.Checkbutton(frame,text='装备关',variable=equipment_intvar,bootstyle="square-toggle").grid(row=5,column=0,padx=10, pady=10)
    ttk.Checkbutton(frame,text='技能关',variable=skill_intvar,bootstyle="square-toggle").grid(row=6,column=0,padx=10, pady=10)
    ttk.Checkbutton(frame,text='材料关',variable=material_intvar,bootstyle="square-toggle").grid(row=7,column=0,padx=10, pady=10)
    ttk.Checkbutton(frame,text='主线任务',variable=main_quest_intvar,bootstyle="square-toggle").grid(row=9,column=0,padx=10, pady=10)
    ttk.Checkbutton(frame,text='领取奖励',variable=get_reward_intvar,bootstyle="square-toggle").grid(row=10,column=0,padx=10, pady=10)

    element_combobox = ttk.Combobox(
        master=frame,
        font=('微软雅黑', 12),
        values=['fire','water','thunder','light','dark'],
        justify=CENTER,
    )
    element_combobox.current(0)
    element_combobox.grid(row=7,column=1,padx=10, pady=10,sticky=EW)

    routine_button = ttk.Button(frame,text='启动',command=lambda :routine_mission_thread(intvar_list,element_combobox.get()))
    routine_button.grid(row=3,column=2,padx=10, pady=10,rowspan=6,sticky=NSEW)

    common_tower_label = ttk.Label(frame,text='通用塔型开荒',anchor= CENTER)
    common_tower_button = ttk.Button(frame,text='启动',command=exploration_tower)

    common_tower_label.grid(row=12, column=0,padx=10, pady=10, sticky=EW)
    common_tower_button.grid(row=12, column=2,padx=10, pady=10, sticky=EW)

    common_battle_label = ttk.Label(frame,text='通用体力型开荒',anchor= CENTER)
    common_battle_button = ttk.Button(frame,text='启动',command=exploration_energy)

    common_battle_label.grid(row=11, column=0,padx=10, pady=10, sticky=EW)
    common_battle_button.grid(row=11, column=2,padx=10, pady=10, sticky=EW)

    for i in range(3):
        frame.columnconfigure(i, weight=1)

    return frame
