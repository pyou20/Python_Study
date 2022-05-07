# coding=gbk
import cv2
import os
import tkinter as tk
from tkinter.messagebox import *
import recognition as r


def creat(name):
    class_name = name
    if os.path.exists(class_name):
        pass
    else:
        os.mkdir(class_name)
    return class_name


def take_photo():
    window = tk.Tk()
    window.withdraw()  # �˳�Ĭ�� tk ����
    showinfo('��ʾ', 'ѡ�д��尴x������������,����¼�밴q����')

    class_name = creat('sign_user')
    cap = cv2.VideoCapture(0)
    width = 640
    height = 480
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    index = 0

    while True:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        c = cv2.waitKey(1)
        if c == ord('x'):
            index = index + 1
            user_code = str(index)
            cv2.imwrite("%s/%s.jpeg" % (class_name, "user" + user_code),
                        cv2.resize(frame, (640, 480), interpolation=cv2.INTER_AREA))
            showinfo('��ʾ', '������Ϣ����ɹ���')
            break

        if c == ord('q'):
            break

    cap.release()
    cv2.DestroyAllWindows()


def take_photo_login():
    window = tk.Tk()
    window.withdraw()  # �˳�Ĭ�� tk ����
    showinfo('��ʾ', 'ѡ�д��尴x��ʼʶ��,��q�˳�')
    class_name = creat('login_user')
    cap = cv2.VideoCapture(0)
    width = 640
    height = 480
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    while True:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        c = cv2.waitKey(1)

        if c == ord('x'):
            cv2.imwrite("%s/%s.jpeg" % (class_name, "user_ing"),
                        cv2.resize(frame, (640, 480), interpolation=cv2.INTER_AREA))
            flag = r.main()
            return flag
        if c == ord('q'):
            break

    cap.release()
    cv2.DestroyAllWindows()


# take_photo()
