import urllib.request
import gzip
import json
import tkinter as tk


def window():
    comments_window = tk.Tk()
    comments_window.title('网易热评')
    comments_window.geometry('500x500')
    comments_text = tk.Text(comments_window, font=('楷体', 15),height=20)

    def page_date():
        comments_text.delete('1.0','end')
        url = 'https://api.muxiaoguo.cn/api/163reping'
        comments_data = urllib.request.urlopen(url).read()
        comments_data = json.loads(comments_data)

        s = comments_data.get('data')
        # print(s.get('content'))

        comments_text.insert('end','  '+comments_data.get('data').get('content') + '\n\n\n')
        # comments_text.insert('end', '音乐封面：' + s.get('songPic') + '\n')
        comments_text.insert('end', '音乐作者：' + s.get('songAutho') + '\n')
        comments_text.insert('end', '音乐名称：' + s.get('songName') + '\n')
        comments_text.insert('end', '音乐ID：' + s.get('songId') + '\n')
        comments_text.insert('end', '用户昵称：' + s.get('nickname') + '\n')
        # comments_text.insert('end', '用户头像：' + s.get('avatar') + '\n')
        comments_text.insert('end', '点赞数量：' + s.get('likedCount') + '\n')
        # comments_text.insert('end', '发表时间：' + s.get('time') + '\n')
        print(s)

    comments_text.pack()
    page_date()
    change_button = tk.Button(comments_window, text='换一个', command=page_date)
    change_button.pack()
    comments_window.mainloop()


# window()
