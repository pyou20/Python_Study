import os
import tkinter as tk


def check(*arr):  # 检查输入的二进制数是否合法
    arr_len = len(arr)
    for i in range(0, arr_len):
        if int(arr[i]) > 1:
            # print("你输入的二进制数有误请重新输入！")
            return 1


def ten_two(*arr):
    arr_len = len(arr)
    num = ''  # 初始化变量
    nums = []  # 定义列表存储数字
    # print(arr[0:arr_len])测试
    for j in range(0, arr_len):
        num = num + arr[j]
    num = int(num)
    user_num = num  # 原始数字
    while num > 0:
        x = num % 2
        num = int(num / 2)
        nums.append(x)
    #     print(nums)测试
    nums.reverse()  # 颠倒数组
    #     print(nums)测试
    # print(user_num, "转化为二进制的结果为：")
    result = ''
    for i in nums:
        result += str(i)
    return result


def two_ten(*arr):
    if check(*arr) == 1:
        return '你输入的二进制有误!'
    else:
        arr_len = len(arr)
        result = 0
        j = 1
        for i in range(0, arr_len):
            result = result + int(arr[i]) * 2 ** (arr_len - j)
            j = j + 1
        # print("转化为十进制的结果为:\n%d" % result)
        return result


def window():
    root = tk.Tk()
    root.title('二进制与十进制转换')
    root.geometry('500x300')
    select = tk.StringVar(root)
    select1 = tk.IntVar(root)
    select2 = tk.IntVar(root)
    result = tk.Label(root, textvariable=select, bg='green', fg='white', font=('Arial', 20), width=50, height=4)
    entry1 = tk.Entry(root, show=None, font=('Arial', 20))

    def command_button():
        if (select1.get() == 1) & (select2.get() == 0):
            nums = entry1.get()
            num = ten_two(*nums)
            select.set("结果为："+num)
        elif (select1.get() == 0) & (select2.get() == 1):
            nums = entry1.get()
            num = str(two_ten(*nums))
            select.set("结果为："+num)
        elif (select1.get() == 0) & (select2.get() == 0):
            select.set('请选择转换模式！')
        else:
            select.set('每次只能选择一个模式！')

    choice1 = tk.Checkbutton(root, text='十进制转二进制',font=('黑体', 20), variable=select1, onvalue=1, offvalue=0)
    choice2 = tk.Checkbutton(root, text='二进制转十进制',font=('黑体', 20), variable=select2, onvalue=1, offvalue=0)
    confirm_button=tk.Button(root,text='转换',font=('黑体', 20),command=command_button)
    entry1.pack()
    choice1.pack()
    choice2.pack()
    confirm_button.pack()
    result.pack()

    root.mainloop()

# window()
