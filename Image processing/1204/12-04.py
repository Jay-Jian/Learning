import cv2
import  numpy as np

# m1=cv2.imread("unnamed.jpg", 1)
# m2=cv2.inRange(m1,(200,200,200),(255,255,255))
# m2=cv2.erode(m2,np.ones((3,3)))

# a,b=cv2.findContours(m2,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

# m3=np.full(m1.shape,255,np.uint8)
# cv2.drawContours(m3,a,-1,(0,0,255),2)
# cv2.imshow("m3"+str(i),m1[y:y+h,x:x+w])
# cv2.waitKey(0)
# cv2.destroyAllWindows()

##留空還少一大段


##文字辨識
##若字體顏色仍有雜訊無法辨識，可使用以下方式處理。
##EX:【1.轉為兩色去除雜訊進行辨識、2.繪製輪廓重新給原色再進行辨識】
# import pytesseract as pt

# m1=cv2.imread("C:\\Users\\user\\Desktop\\4.png",1)
# text=pt.image_to_string(m1,"eng","")
# print(text)
# cv2.imshow("m1",m1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# m1=cv2.imread("C:\\tesseract-Win64_3.05\\tesseract-Win64_3.05\\tessdata\\1.png",1)
# m2=cv2.inRange(m1,(0,0,180),(100,100,255))
# m2=cv2.dilate(m2,np.ones((10,10)))#侵蝕


#文字辨識 辨識結果=pt.image_to_string(圖片變數, 語言包名稱, 設定值)
#設定值內可以接白名單【-c tessedit_char_whitelist=字元】、黑名單【-c tessedit_char_blacklist=字元】
# text=pt.image_to_string(m1,"my","")

#如果想讓特定字不顯示【空白】需要透過以下方式【下列以B為例】
# for i in range(0,len(text)):
# 	if text[i]=="B":
# 		print("",end="")
# 		continue
# 	print(text[i],end="")

# print(text)
# cv2.imshow("m1",m1)
# cv2.imshow("m2",m2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#可以搭配老師的training.bat訓練辨識語言包【例如圖像為123，將語言包改為ABC往後都會辨識為ABC】
# m1=cv2.imread("C:\\tesseract-Win64_3.05\\tesseract-Win64_3.05\\tessdata\\1.png",1)
# text=pt.image_to_string(m1,"my","")
# print(text)
# cv2.imshow("m1",m1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


from pyzbar import pyzbar
##二維碼辨識
##for可以用來辨識單一圖片內多個二維碼【同時顯示】
# m1=cv2.imread("12043.png",1)

# ret=pyzbar.decode(m1)
# for d in ret:
# 	print("條碼類型:",d.type)
# 	print(d.data.decode("utf-8"))
# 	x,y,w,h=d.rect
# 	cv2.rectangle(m1,(x,y),(x+w,y+h),(0,0,255),2)
# 	print("=========================")
# cv2.imshow("m1",m1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


##p=cv2.videoCapture(N)，N=0=掃描影片內的二維碼【可以輸入影片路徑讀取影片】
##可以將結果存入list，掃碼後先與list比對排除重複值再辨識寫入
# p=cv2.videoCapture(0)
# while p.isOpened()==True:
# 	ret,m1=p.read()
# 	if ret==True:
# 		ret=pyzbar.decode(m1)
# 		for d in ret:
# 			print("存的資料:",d.data.decode("utf-8"))
# 			x,y,w,h=d.rect
# 			cv2.rectangle(m1,(x,y),(x+w,y+h),(0,0,255),2)
# 		cv2.imshow("m1",m1)
# 		if cv2.waitKey(33)!=-1:
# 			break
# 	else:
# 		break

# r.release()
# cv2.destroyAllWindows()

##辨識二維碼內含的中文內容
##except是用來處理意外【套件為日本人所製作，可能會有部分中文字無法辨識】
# m1=cv2.imread("12044.png",1)

# ret=pyzbar.decode(m1)
# for d in ret:
# 	print("條碼類型:",d.type)
# 	try:
# 		print("存的資料:",d.data.decode("utf-8").encode("sjis").decode("utf-8"))
# 	except:
# 		print("存的資料:",d.data.decode("utf-8"))
# 	x,y,w,h=d.rect
# 	cv2.rectangle(m1,(x,y),(x+w,y+h),(0,0,255),2)
# 	print("=========================")
# cv2.imshow("m1",m1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


###相片人臉辨識
# m1=cv2.imread("12049.png",1)
# ##結果變數=控制變數.detectMultiScale(圖像變數,minNeighbors=檢測門檻數,minSize=最小尺寸)
# ##p1=cv2.CascadeClassifier("接分類文件進行辨識")
# p1=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# ret=p1.detectMultiScale(m1,minNeighbors=1, minSize=(10,10))
# for x,y,w,h in ret:
# 	cv2.rectangle(m1,(x,y),(x+w,y+h),(0,0,255),2)

# cv2.imshow("m1",m1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




##影像人臉辨識
# p=cv2.videoCapture(0)
# p1=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# while p.isOpened()==True:
# 	ret,m1=p.read()
# 	if ret==True:
# 		ret=p1.detectMultiScale(m1,minNeighbors=5, minSize=(10,10))
# 		for x,y,w,h in ret:
# 			cv2.rectangle(m1,(x,y),(x+w,y+h),(0,0,255),2)

# 		cv2.imshow("m1",m1)
# 		if cv2.waitKey(33)!=-1:
# 			break
# 	else:
# 		break
# cv2.destroyAllWindows()


##相片人臉辨識
# m1=cv2.imread("C:/Users/user/Desktop/classifier_training/classifier_training/Data/Image.jpg",1)
# ##結果變數=控制變數.detectMultiScale(圖像變數,minNeighbors=檢測門檻數,minSize=最小尺寸)
# ##p1=cv2.CascadeClassifier("接分類文件進行辨識")
# p1=cv2.CascadeClassifier("C:\\Users\\user\\Desktop\\classifier_training\\classifier_training\\xml\\cascade.xml")
# ret=p1.detectMultiScale(m1,minNeighbors=3, minSize=(10,10))
# for x,y,w,h in ret:
# 	cv2.rectangle(m1,(x,y),(x+w,y+h),(0,0,255),2)

# cv2.imshow("m1",m1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()