import dlib
from imageio import imread
import numpy as np

from tkinter.messagebox import *


def main():
    detector = dlib.get_frontal_face_detector()  # 检测人脸
    predictor_path = 'shape_predictor_68_face_landmarks.dat'
    predictor = dlib.shape_predictor(predictor_path)  # 参数：‘data/data_dlib/shape_predictor_68_face_landmarks.dat’：68
    # 个关键点模型地址返回值：人脸关键点预测器'
    face_rec_model_path = 'dlib_face_recognition_resnet_model_v1.dat'
    face_rec = dlib.face_recognition_model_v1(face_rec_model_path)  # 面部识别器

    def get_feature(path):
        img = imread(path)
        dets = detector(img)
        # print('检测到了 %d 个人脸' % len(dets))
        shape = predictor(img, dets[0])
        face_vector = face_rec.compute_face_descriptor(img, shape)
        return face_vector

    def distance(a, b):
        a, b = np.array(a), np.array(b)
        sub = np.sum((a - b) ** 2)
        add = (np.sum(a ** 2) + np.sum(b ** 2)) / 2.
        return sub / add

    path_lists1 = ["login_user/user_ing.jpeg", "sign_user/user1.jpeg"]

    feature_lists1 = [get_feature(path) for path in path_lists1]


    out1 = distance(feature_lists1[0], feature_lists1[1])

    def classifier(a, b, t=0.09):
        if distance(a, b) <= t:
            ret = True
        else:
            ret = False
        return ret

    if classifier(feature_lists1[0], feature_lists1[1]):
        print("识别成功")
        showinfo('提示', '验证成功！')
        return 1
    if not classifier(feature_lists1[0], feature_lists1[1]):
        print("识别失败")
        showinfo('提示', '验证失败！')
        return 0
