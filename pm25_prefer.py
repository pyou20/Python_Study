import tkinter as tk
import requests
from bs4 import BeautifulSoup
import time


def loadingmenu():
    print("请稍等")

    print("Loading", end="")
    for i in range(10):
        print(".", end='', flush=True)
        time.sleep(0.5)


def windows_pm():
    pm_window = tk.Tk()
    pm_window.title('PM2.5查询')
    pm_window.geometry('500x500')
    date = tk.StringVar(pm_window)

    url1 = 'http://www.pm25x.com/'
    html = requests.get(url1)
    sp0 = BeautifulSoup(html.text, 'html.parser')
    # print(sp0)
    def test(sp1):
        city_name = pm_entry.get()
        t3 = ""
        flag = 0
        p1 = sp1.find_all('a')
        for t2 in p1:
            t4 = t2.string
            t4 = str(t4)
            if t4 == city_name:
                flag += 1
                t3 = t2.get('href')
                break
        if flag == 0:
            return "你的输入的城市不存在!"

        city = sp1.find("a", {"title": "北京PM2.5"})
        city.get("href")
        url2 = url1 + t3

        html2 = requests.get(url2)
        sp2 = BeautifulSoup(html2.text, "html.parser")
        data1 = sp2.select(".aqivalue")
        pm25 = data1[0].text
        return city_name + "此时的PM2.5值为：" + pm25

    def fun():
        date.set(test(sp0))

    pm_entry = tk.Entry(pm_window, show=None, font=('Arial', 15))  # 显示成明文形式
    pm_title = tk.Label(pm_window, text='请输入要查询的城市名称', bg='white', fg='green', font=('Arial', 20), width=50, height=2)
    pm_button = tk.Button(pm_window, text='查询', width=20, height=2, font=('Arial', 12), command=fun)
    pm_date = tk.Label(pm_window, textvariable=date, bg='green', fg='white', font=('Arial', 12), width=60, height=5)
    pm_title.pack()
    pm_entry.pack()
    pm_button.pack()
    pm_date.pack()
    pm_window.mainloop()

# windows_pm()
