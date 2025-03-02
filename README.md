# TinkleStarKnightsScript
## 简介
    疯狂星期四闪耀星骑士的脚本。包括主线和新月塔的开荒和一些日活

## 基本使用说明
    此脚本仅支持pc端的模拟器。DMMPlayer、手机端、网页端请自行绕道  （开发时使用的是MuMu12）
    详细的使用说明已经嵌入在了gui页面中

## 项目结构
    所有包下的globals存放了全局参数，global_set里是一些用于修改全局参数的方法

### autoFunction
    基本函数库，包括了一些最基本的脚本操作
#### simple_function
    里面包含了最基本的自动化原子命令，例如模拟图像识别的点击，模拟滑动
#### composite_function
    里面包含了简单的复合原子操作，例如回到主页，检测错误

### explorationTask
    开荒库，里面包括了主线开荒，新月塔开荒，和通用开荒
#### moon_tower
    新月塔开荒相关代码
#### main_quest
    主线开荒相关代码
#### common_exploration
    通用开荒相关代码
### ScriptsGui
    可视化页面库
#### mainPage
    最外层框架页面相关代码
#### ScriptsPage
    脚本执行页面相关代码
#### SettingsPage
    设置页面相关代码
#### InstructionPage
    使用说明页面相关代码
#### script_button_actions
    按钮调用的函数相关代码
#### utils
    gui页面使用函数代码

