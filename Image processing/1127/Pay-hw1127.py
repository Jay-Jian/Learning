import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

# EX:讀秒
# i=0
# while True:
# 	m1=np.full((300, 500,3), (255,255,255), np.uint8)
# 	m1=Image.fromarray(m1)
# 	ImageDraw.Draw(m1).text(
# 		(150,150),
# 		str(i),
# 		(0,0,255),
# 		ImageFont.truetype("msyhbd.ttc", 50)
# 	)
# 	m1=np.array(m1)
# 	i+=1
# 	cv2.imshow("m1",m1)
# 	if cv2.waitKey(33)!=-1:
# 		break
# cv2.destroyAllWindows()


a=0
i=0
while True:
	m1=np.full((300, 500,3), (255,255,255), np.uint8)
	if a == 0 :
		cv2.rectangle(m1, (0+i,100), (100+i,200), (255,0,0), -1)
		cv2.imshow("m1",m1)
		cv2.waitKey(1)
		i+=10
		if i == 400:
			a=1
		
	elif a == 1 :
		cv2.rectangle(m1, (0+i,100), (100+i,200), (255,0,0), -1)
		cv2.imshow("m1",m1)
		cv2.waitKey(1)
		i-=10
		if i == 0 :
			a=0
	if cv2.waitKey(1)!=-1:
		break
		
cv2.destroyAllWindows()