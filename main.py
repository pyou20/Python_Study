import tkinter as tk
import tkinter.messagebox
import pickle
import work_main
import takephoto
from tkinter.messagebox import *

window = tk.Tk()
window.title('期末大作业V1.0')
window.geometry('450x500')


tk.Label(window, text='欢迎来到我的期末作业', bg="green",fg="yellow",font=('Arial', 16)).pack()
canvas = tk.Canvas(window, width=500, height=361)
image_file = tk.PhotoImage(file='picture.gif')
image = canvas.create_image(250, 0, anchor='n', image=image_file)
canvas.pack(side='top')


tk.Label(window, text='用户名:', font=('Arial', 14)).place(x=20, y=380)
tk.Label(window, text='密码:', font=('Arial', 14)).place(x=20, y=420)

# 用户登录输入框entry
# 用户名
var_user_name = tk.StringVar()
var_user_name.set('')
entry_user_name = tk.Entry(window, textvariable=var_user_name, font=('Arial', 14))
entry_user_name.place(x=120, y=380)
# 用户密码
var_user_pwd = tk.StringVar()
entry_user_pwd = tk.Entry(window, textvariable=var_user_pwd, font=('Arial', 14), show='*')
entry_user_pwd.place(x=120, y=420)


# 登录
def user_login():
    user_name = var_user_name.get()
    user_pwd = var_user_pwd.get()

    # 异常捕获&&匹配信息
    try:
        with open('user_info/users_info.pickle', 'rb') as user_info_file:
            users_info = pickle.load(user_info_file)
    except FileNotFoundError:
        # 没有读取到`user_info_file`的时候，程序会创建一个`user_info_file`这个文件
        with open('user_info/users_info.pickle', 'wb') as user_info_file:
            users_info = {'admin': 'admin'}  # 写入管理员账号
            pickle.dump(users_info, user_info_file)
            user_info_file.close()

    # 登录成功
    if user_name in users_info:
        if user_pwd == users_info[user_name]:
            tkinter.messagebox.showinfo(title='欢迎', message='登录成功！\n欢迎 ' + user_name)
            window.destroy()
            work_main.my_work()
        # 如果用户名匹配成功，而密码输入错误，则会弹出'密码错误！请重试'
        else:
            tkinter.messagebox.showerror(message='密码错误！请重试')
    else:  # 如果发现用户名不存在
        is_sign_up = tkinter.messagebox.askyesno('提示', '该用户不存在是否注册？')
        # 提示需不需要注册新用户
        if is_sign_up:
            user_sign_up()


# 定义用户注册功能
def user_sign_up():
    def sign_up():
        # 获取注册信息
        new_user = new_name.get()
        new_psw = new_pwd.get()
        re_user_psw = new_pwd_confirm.get()

        # 打开文件，读取用户信息
        with open('user_info/users_info.pickle', 'rb') as user_file:
            exist_user_info = pickle.load(user_file)
        # 两次密码输入不一致，则提示Error, 两次输入必须一致
        if new_psw != re_user_psw:
            tkinter.messagebox.showerror('Error', '两次输入不一致')

        # 如果用户名已存在，则提示Error, 已经注册
        elif new_user in exist_user_info:
            tkinter.messagebox.showerror('Error', '该用户名已注册')

        # 最后如果输入无以上错误，则将注册输入的信息记录到文件当中，并提示注册成功，关闭窗口。
        else:
            exist_user_info[new_user] = new_psw
            with open('user_info/users_info.pickle', 'wb') as user_file:
                pickle.dump(exist_user_info, user_file)
            tkinter.messagebox.showinfo('提示', '注册成功')
            window_sign_up.destroy()  # 关闭

    # 注册窗口
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('300x200')
    window_sign_up.title('注册')

    new_name = tk.StringVar()
    new_name.set('')
    tk.Label(window_sign_up, text='用户名: ').place(x=10, y=10)  # 将用户名放置在坐标（10,10）
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)  # 创建一个注册名的`entry`，变量为`new_name`
    entry_new_name.place(x=130, y=10)  # `entry`放置在坐标（150,10）.

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='密码: ').place(x=10, y=50)
    entry_user_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_user_pwd.place(x=130, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='再次输入密码: ').place(x=10, y=90)
    entry_user_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_user_pwd_confirm.place(x=130, y=90)

    # 下面的 sign_up
    button_comfirm_sign_up = tk.Button(window_sign_up, text='注册', command=sign_up)
    button_comfirm_sign_up.place(x=180, y=120)


def face_login():  # 调用识别模块
    if takephoto.take_photo_login() == 1:
        window.destroy()
        work_main.my_work()


def face_sign():
    takephoto.take_photo()
    showinfo('提示', '人脸注册成功！')


# 登录、注册按钮
button_login = tk.Button(window, text='登录', command=user_login)
button_login.place(x=118, y=450)
button_face_login = tk.Button(window, text='人脸识别登录', command=face_login)
button_face_login.place(x=158, y=450)
button_face_sign = tk.Button(window, text='人脸注册', command=face_sign)
button_face_sign.place(x=248, y=450)
button_sign_up = tk.Button(window, text='注册', command=user_sign_up)
button_sign_up.place(x=318, y=450)

window.mainloop()
