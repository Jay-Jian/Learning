import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

p=cv2.VideoCapture("C:\\Users\\user\\Desktop\\h3.mp4")
print("總共的畫面數量：",p.get(7))
# print("寬：",p.get(3))
# print("高：",p.get(4))
# print("FPS：",p.get(5))
##畫面數量:509
##寬:640、高:360、FPS:30


v2=p.isOpened()
