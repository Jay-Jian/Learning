import cv2
import numpy as np 

##功課2[去背更換字體&背景顏色紀錄]


##自己的寫法，卡住了[還有底未清乾淨且字體有色差]
m1=cv2.imread("h2.png", 1)
m2=np.full(m1.shape,255,np.uint8)
m3=cv2.multiply(m1,m2)
m3=cv2.cvtColor(m3,cv2.COLOR_BGR2GRAY)

cv2.imshow("m3", m3)
cv2.waitKey(0)
cv2.destroyAllWindows()




##Ting的寫法
# m1=cv2.imread("h2.png", 1)

# m3=np.full(m1.shape,255,np.uint8)  =m2
# m5=cv2.multiply(m1,m3)  =m3

# m6=np.full(m1.shape,[0,0,255],np.uint8)=m4
# m7=cv2.add(m5,m6)=m5

# m8=np.full(m1.shape,[255,0,0],np.uint8)
# m9=cv2.add(m7,m8)

# m10=cv2.cvtColor(m9,cv2.COLOR_BGR2GRAY)
# cv2.imshow("grey",m10)
# grey_254=np.full((m10.shape[0],m10.shape[1],1),(254),np.uint8)
# m10=cv2.subtract(m10,grey_254)
# m10=cv2.subtract(m10,grey_254)
# cv2.imshow("black",m10)

# cv2.waitKey(0)
# cv2.destroyAllWindows()




##第二種寫法[老師教後修改版]
# m1=cv2.imread("h2.png", 1)
# m2=m1.copy()
# m2=cv2.inRange(m1,(0,0,255),(0,0,255))
# m2=cv2.bitwise_not(m2)

# # cv2.imshow("m1", m1)
# cv2.imshow("m2", m2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()









# m1=cv2.imread("h2.png",1)
# m2=m1.copy()

# m2=cv2.inRange(m1, (0,0,255), (0,0,255))
# m2=cv2.bitwise_not(m2)

# cv2.imshow("m1", m1)
# cv2.imshow("m2", m2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()