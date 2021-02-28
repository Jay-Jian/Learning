import cv2
import numpy as np

##老師版
m1=cv2.imread("h2.png",1)
m2=cv2.bitwise_not(m1[:,:,2])
m2=cv2.add(m2,m1[:,:,1])
m2=cv2.add(m2,m1[:,:,0])
# m2=cv2.multiply(m2,np.full(m2.shape,255,np.uint8))
cv2.imshow("m2", m1)
cv2.waitKey(0)
cv2.destroyAllWindows()



# m1=cv2.imread("h2.png", 1)
# m2=np.full(m1.shape,255,np.uint8)
# m3=cv2.multiply(m1,m2)

# m4=np.full(m1.shape,[0,0,255],np.uint8)
# m5=cv2.add(m3,m4)

# m6=np.full(m1.shape,[255,0,0],np.uint8)
# m7=cv2.add(m5,m6)
# m8=cv2.cvtColor(m7,cv2.COLOR_BGR2GRAY)
# cv2.imshow("grey",m8)
# m9=np.full((m8.shape[0],m8.shape[1],1),(254),np.uint8)
# m8=cv2.subtract(m8,m9)
# m8=cv2.subtract(m8,m9)
# cv2.imshow("m3",m8)

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