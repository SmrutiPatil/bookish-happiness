import cv2

img = cv2.imread("D:\Pictures\Anime&Misc\Graduation certificte.PNG")
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Graduation Certificate',(150,150),font,2,(255,0,255),5,cv2.LINE_AA)

cv2.imshow('Image with text',img);
