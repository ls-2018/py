# encoding=utf-8
import cv2
import os

path = r'D:\Destop\新建文件夹 (2)'

path = r'G:\清华_尹成_C语言从菜鸟到高手 10月14版\3传智播客_尹成_C语言从菜鸟到高手_第三章C语言数据类型_运算符与表达式\3.4 基本运算符与表达式\视频'

file_l = list(os.walk(path))[0][2]
sum = 0
for file_path in file_l:

    cap = cv2.VideoCapture(os.path.join(path, file_path))
    # file_path是文件的绝对路径，防止路径中含有中文时报错，需要解码
    if cap.isOpened():  # 当成功打开视频时cap.isOpened()返回True,否则返回False
        # get方法参数按顺序对应下表（从0开始编号)
        rate = cap.get(5)  # 帧速率
        FrameNumber = cap.get(7)  # 视频文件的帧数
        duration = FrameNumber / rate / 60  # 帧速率/视频总帧数 是时间，除以60之后单位是分钟
        sum += duration
print(sum / 60)
# print(10661 / 60)  # 180 个小时

