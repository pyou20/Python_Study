import tkinter as tk
import random as r


def window():
    game_window = tk.Tk()
    game_window.title('猜拳')
    # game_result.set('test??')
    game_window.geometry('500x500')
    game_result_date = tk.StringVar(game_window)

    def fun1():
        s=r.randint(1,3)
        if s==1:
            game_result_date.set('平局')
        elif s==2:
            game_result_date.set('机器出剪刀，您输了！')
        elif s==3:
            game_result_date.set('机器出石头，您赢了！')

    def fun2():
        s = r.randint(1, 3)
        if s == 1:
            game_result_date.set('平局')
        elif s == 2:
            game_result_date.set('机器出石头，您输了！')
        elif s == 3:
            game_result_date.set('机器出布，您赢了！')

    def fun3():
        s = r.randint(1, 3)
        if s == 1:
            game_result_date.set('平局')
        elif s == 2:
            game_result_date.set('机器出布，您输了！')
        elif s == 3:
            game_result_date.set('机器出剪，您赢了！')


    game_label = tk.Label(game_window, text='选择你要出的拳', fg='green', bg='white', font=('Arial', 12), width=60, height=2)
    game_button_bu = tk.Button(game_window, text='布',width=60, height=2, command=fun1)
    game_button_jian = tk.Button(game_window, text='剪刀',width=60, height=2, command=fun2)
    game_button_shitou = tk.Button(game_window, text='石头',width=60, height=2, command=fun3)
    game_result = tk.Label(game_window, textvariable=game_result_date, fg='green', bg='white', font=('Arial', 12), width=60,
                           height=2)
    game_label.pack()
    game_button_bu.pack()
    game_button_jian.pack()
    game_button_shitou.pack()
    game_result.pack()
    game_window.mainloop()


# window()
