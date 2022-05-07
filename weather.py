import urllib.request
import gzip
import json
import tkinter as tk


def windows_weather():
    weather_window = tk.Tk()
    weather_window.title('天气查询')
    weather_window.geometry('500x500')
    date = tk.StringVar(weather_window)
    weather_txt = tk.Text(weather_window, height=40)
    select = tk.IntVar(weather_window)
    choice = tk.Checkbutton(weather_window, text='是否要显示未来四天天气', font=('宋体', 12), variable=select, onvalue=1, offvalue=0)

    # 获取数据
    def get_weather_data():
        # city_name = input('请输入要查询的城市名称：')
        city_name = weather_entry.get()
        url1 = 'http://wthrcdn.etouch.cn/weather_mini?city=' + urllib.parse.quote(city_name)
        # print(urllib.parse.quote(city_name)+'test')
        url2 = 'http://wthrcdn.etouch.cn/weather_mini?citykey=101010100'
        # 网址1只需要输入城市名，网址2需要输入城市代码
        # print(url1)
        weather_data = urllib.request.urlopen(url1).read()
        # 读取网页数据
        weather_data = gzip.decompress(weather_data).decode('utf-8')
        # 解压网页数据
        weather_dict = json.loads(weather_data)
        # print(weather_dict)
        # 将json数据转换为dict数据
        return weather_dict

    def show_weather(weather_data):
        weather_dict = weather_data
        # 将json数据转换为dict数据
        if weather_dict.get('desc') == 'invilad-citykey':
            print('你输入的城市名有误，或者天气中心未收录你所在城市')
            weather_txt.insert('0.0',"你输入的城市名有误，或者天气中心未收录你所在城市")
        elif weather_dict.get('desc') == 'OK':
            forecast = weather_dict.get('data').get('forecast')
            weather_txt.insert('end', '城市：'+weather_dict.get('data').get('city')+ '\n')
            weather_txt.insert('end', '温度：' + weather_dict.get('data').get('wendu') + '℃ '+ '\n')
            weather_txt.insert('end', '感冒：' + weather_dict.get('data').get('ganmao')+ '\n')
            weather_txt.insert('end', '风向：' + forecast[0].get('fengxiang')+ '\n')
            weather_txt.insert('end', '风级：' + forecast[0].get('fengli')+ '\n')
            weather_txt.insert('end', '高温：' + forecast[0].get('high')+ '\n')
            weather_txt.insert('end', '低温：' + forecast[0].get('low')+ '\n')
            weather_txt.insert('end','天气：' + forecast[0].get('type')+ '\n')
            weather_txt.insert('end', '日期：'+forecast[0].get('date')+ '\n\n')
            if select.get() == 1:
                for i in range(1, 5):
                    weather_txt.insert('end', '日期：' + forecast[i].get('date') + '\n')
                    weather_txt.insert('end', '风向：' + forecast[i].get('fengxiang') + '\n')
                    weather_txt.insert('end', '风级：' + forecast[i].get('fengli') + '\n')
                    weather_txt.insert('end', '高温：' + forecast[i].get('high') + '\n')
                    weather_txt.insert('end', '低温：' + forecast[i].get('low') + '\n')
                    weather_txt.insert('end', '天气：' + forecast[i].get('type') + '\n\n')
            elif select.get() == 0:
                pass
                # print('test')

    def button():
        weather_txt.delete('1.0','end')
        weather_date = get_weather_data()
        show_weather(weather_date)

    weather_entry = tk.Entry(weather_window, show=None, font=('Arial', 15))  # 显示成明文形式
    weather_title = tk.Label(weather_window, text='请输入要查询的城市名称', bg='white', fg='green', font=('Arial', 20), width=50,
                        height=2)
    weather_button = tk.Button(weather_window, text='查询', width=20, height=2, font=('Arial', 12),command=button)

    # 显示
    weather_title.pack()
    weather_entry.pack()
    choice.pack()
    weather_button.pack()
    weather_txt.pack()
    weather_window.mainloop()


# windows_weather()



