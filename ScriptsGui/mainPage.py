import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ScriptsGui import SettingsPage
from ScriptsGui import ScriptsPage
from ScriptsGui import InstructionPage

def gui_show():
        root = ttk.Window(
                title="疯狂星期四脚本",        #设置窗口的标题
                themename="superhero",     #设置主题
                size=(1066,600),        #窗口的大小
                position=(100,100),     #窗口所在的位置
                minsize=(0,0),          #窗口的最小宽高
                maxsize=(1920,1080),    #窗口的最大宽高
                alpha=0.8,              #设置窗口的透明度(0.0完全透明）
                )
        root.place_window_center()    #让显现出的窗口居中

        frame = ttk.Frame(root)
        frame.pack(fill=BOTH,padx=5,pady=5,side=TOP,expand=True)

        notebook = ttk.Notebook(frame)
        notebook.pack(side=TOP, fill=BOTH, expand=YES,padx=5,pady=5)
        notebook.add(ScriptsPage.get_frame(notebook),text='脚本页面',sticky=NSEW)
        notebook.add(SettingsPage.get_frame(notebook),text='设置界面',sticky=NSEW)
        notebook.add(InstructionPage.get_frame(notebook), text='使用说明', sticky=NSEW)
        root.mainloop()
