import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
from pathlib import Path
from ttkbootstrap.dialogs import Messagebox
import json

from autoFunction.global_set import autoFunction_global_set
from explorationTask.global_set import explorationTask_global_set

#序号对应的json名
order_dict={
    '1':'autoFunction_setting.json',
    '2':'explorationTask_setting.json',
}

def get_label_and_entry(master, setting_dic,explanation_dic):
    # 创建 LabelFrame，标题为 explanation 的值
    explanation = setting_dic.get("explanation", "未找到设置类别说明")
    label_frame = ttk.Labelframe(master, text=explanation, bootstyle="superhero")

    scrolled_frame = ScrolledFrame(label_frame,autohide=True)
    scrolled_frame.pack(fill=BOTH, expand=True ,padx=0, pady=0)

    # 遍历字典生成标签和输入框
    row = 0
    entries = {}  # 用于存储所有输入框的引用
    string_vars = {} #存储输入框绑定的字符串
    for key, value in setting_dic.items():
        if key == "explanation":
            continue

        # 创建标签
        label = ttk.Label(scrolled_frame, text=key, bootstyle="superhero")
        label.grid(row=row, column=0, padx=10, pady=10, sticky=EW)

        #创建解释标签
        value_label = ttk.Label(scrolled_frame, text=explanation_dic[key], bootstyle="superhero")
        value_label.grid(row=row, column=1, padx=10, pady=10, sticky=EW)

        # 创建输入框（ttkbootstrap 的 Entry 支持 bootstyle）
        string_var = ttk.StringVar(value=str(value))

        entry = ttk.Entry(scrolled_frame, bootstyle="superhero",textvariable=string_var)
        entry.grid(row=row, column=2, padx=20, pady=10, sticky=EW,)
        entries[key] = entry
        string_vars[key] = string_var
        row += 1

    # 布局优化
    for i in range(3):
        scrolled_frame.columnconfigure(i, weight=1)
    return label_frame, entries ,string_vars

def change_setting(entries, string_vars,order):
    changed_dict={}
    json_path = Path(__file__).parent.parent / 'jsonFolder' / order_dict[order]
    for key, value in string_vars.items():
        changed_dict.update({key:value.get()})

    with json_path.open('w') as json_file:
        if order == "1":
            changed_dict.update({'explanation':'自动函数库设置',})
        elif order == "2":
            changed_dict.update({'explanation': '开荒库设置', })
        json.dump(changed_dict, json_file,indent=4)

        show_dialog_success('配置修改成功,你需要重启脚本以更新配置')
        print('修改成功')

def show_dialog_success(str):
    # 显示确认对话框
    result = Messagebox.okcancel(
        title="success",                   # 标题
        message=str,      # 内容
        bootstyle="success"                # 主题样式
    )
    if result == "OK":
        pass
def show_dialog_fail(str):
    # 显示确认对话框
    result = Messagebox.okcancel(
        title="danger",                   # 标题
        message=str,      # 内容
        bootstyle="danger"                # 主题样式
    )
    if result == "OK":
        pass