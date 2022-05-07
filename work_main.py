# !/usr/bin/python
# -*- coding: UTF-8 -*-


def my_work():
    import tkinter as tk
    import work_transform as tf
    import game
    import pm25_prefer
    import weather
    import comments
    import takephoto
    import recognition as r
    # 创建窗口
    my_windows = tk.Tk()
    my_windows.title('期末大作业V1.0')

    # 窗口大小
    my_windows.geometry('600x400')

    pm_num = tk.Label(my_windows, text='期末作业', bg='white', fg='green', font=('Arial', 12), width=30, height=2)
    pm_num.pack()

    # 查询pm2.5
    pm = tk.Button(my_windows, text='pm2.5查询', width=20, height=2, command=pm25_prefer.windows_pm)
    pm.pack()

    # 天气查询
    weather = tk.Button(my_windows, text='各地天气查询', width=20, height=2, command=weather.windows_weather)
    weather.pack()
    pm.pack()

    # 网易云热评
    commants = tk.Button(my_windows, text='网易云热评', width=20, height=2, command=comments.window)
    commants.pack()

    # 进制转换
    num = tk.Button(my_windows, text='十进制二进制转换', width=20, height=2, command=tf.window)
    num.pack()

    # 石头剪刀布
    game = tk.Button(my_windows, text='石头剪刀布', width=20, height=2, command=game.window)
    game.pack()
    my_windows.mainloop()

# my_work()
