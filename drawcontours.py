import cv2

img = cv2.imread("D:\Pictures\Anime&Misc\Graduation certificte.PNG")
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(imgray,150,250,0)
cont = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)[-2]

cv2.drawContours(img,cont,-1,(255,255,0),3)

cv2.imshow('Original',img)
cv2.imshow('thresh',thresh)
cv2.waitKey(0)
