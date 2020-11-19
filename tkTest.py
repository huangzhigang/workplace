#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.font as tkFont
import time

LOG_LINE_NUM = 0
log_data_Text = Text  # 日志框
check_ver = StringVar()

#设置窗口
def set_init_window(init_window_name):
    init_window_name.title("Richard_v1.0")           #窗口名
    #self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
    init_window_name.geometry('496x380+10+10')
    #self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
    #self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
    ft = tkFont.Font(family='微软雅黑', size=10, weight=tkFont.BOLD)
    #标签
    init_data_label = Label(init_window_name, text="功能区", font=ft)
    init_data_label.grid(row=0, column=0, sticky=W)
    log_label = Label(init_window_name, text="日志", font=ft)
    log_label.grid(row=0, column=5, padx=12, sticky=W)
    init_data_label = Label(init_window_name, text="副本", font=ft)
    init_data_label.grid(row=1, column=0, sticky=W)
    label_zhuagui = Label(init_window_name, text="抓鬼", font=ft)
    label_zhuagui.grid(row=4, column=0, sticky=W)
    label_sperator = Label(init_window_name, text="------------------------------", font=ft)
    label_sperator.grid(row=5, column=0, columnspan=4)
    label_richang_huodong = Label(init_window_name, text="日常活动", font=ft)
    label_richang_huodong.grid(row=6, column=0)

    #多选框
    #CheckVarList = IntVar()[10]
    global check_ver
    check_ver = IntVar()
    CheckVar530 = IntVar()
    cb_all_fuben = Checkbutton(init_window_name, text="530", variable=check_ver, command=set530, onvalue=1, offvalue=0)
    cb_all_fuben.grid(row=1, column=1, sticky=W)
    cb_xiashi1 = Checkbutton(init_window_name, text="侠士1", variable=CheckVar530, onvalue=1, offvalue=0)
    cb_xiashi1.grid(row=2, column=0, sticky=N+W)
    cb_xiashi2 = Checkbutton(init_window_name, text="侠士2", variable=CheckVar530, onvalue=1, offvalue=0)
    cb_xiashi2.grid(row=2, column=1, sticky=N+W)
    cb_putong1 = Checkbutton(init_window_name, text="普通1", variable=CheckVar530, onvalue=1, offvalue=0)
    cb_putong1.grid(row=3, column=0, sticky=N+W)
    cb_putong2 = Checkbutton(init_window_name, text="普通2", variable=CheckVar530, onvalue=1, offvalue=0)
    cb_putong2.grid(row=3, column=1, sticky=N+W)
    cb_putong3 = Checkbutton(init_window_name, text="普通3", variable=CheckVar530, onvalue=1, offvalue=0)
    cb_putong3.grid(row=3, column=2, sticky=N+W)
    #抓鬼
    cb_zhuagui3 = Checkbutton(init_window_name, text="3轮", variable=CheckVar530, onvalue=1, offvalue=0)
    cb_zhuagui3.grid(row=4, column=1, sticky=W)
    cb_zhuagui_overnight = Checkbutton(init_window_name, text="通宵鬼", variable=CheckVar530, onvalue=1, offvalue=0)
    cb_zhuagui_overnight.grid(row=4, column=2, sticky=W)
    CheckVar3 = IntVar()
    menpai = Checkbutton(init_window_name, text="门派", variable=CheckVar530, onvalue=1,offvalue=0)
    menpai.grid(row=7, column=0, sticky=W)

    #文本框
    global log_data_Text
    log_data_Text = Text(init_window_name, width=40, height=26)  # 日志框
    log_data_Text.grid(row=1, column=5, padx=12, rowspan=20, sticky=N+S+E)

    #按钮
    str_trans_to_md5_button = Button(init_window_name, text="开始", bg="lightblue", relief=GROOVE, command=startTask)  # 调用内部方法  加()为直接调用
    str_trans_to_md5_button.grid(row=1, column=2, rowspan=2, sticky=N+W+E+S)

#一条龙绑定设置
def set530():
    global check_ver
    print(check_ver)
    write_log_to_Text("530选项状态变为"+ str(check_ver))
    #self.CheckVar1=self.CheckVar530
    CheckVar3 = 0
    CheckVar4 = 0
    CheckVar5 = 0
    CheckVarGui3 = 0


#功能函数
def startTask():
    write_log_to_Text("Start pressed!")


#获取当前时间
def get_current_time():
    current_time = time.strftime('%m-%d %H:%M:%S',time.localtime(time.time()))
    return current_time


#日志动态打印
def write_log_to_Text(logmsg):
    global LOG_LINE_NUM
    current_time = get_current_time()
    logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行
    log_data_Text.insert(END, logmsg_in)


def gui_start():
    init_window = Tk()  # 实例化出一个父窗口
    # 设置根窗口默认属性
    set_init_window(init_window)
    init_window.resizable(0,0)

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示

gui_start()