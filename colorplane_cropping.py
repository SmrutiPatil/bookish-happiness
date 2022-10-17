import cv2
#import numpy as np

img = cv2.imread("D:\Pictures\Anime&Misc\Graduation certificte.PNG");
cv2.imshow('Original',img)

#separating the color planes
Redplane = img[:,:,2];
Blueplane = img[:,:,0];
Greenplane = img[:,:,1];
cv2.imshow('Red plane image',Redplane);
cv2.imshow('Blue plane image',Blueplane);
cv2.imshow('Green plane image',Greenplane);

#cropping the picture in red plane
Red_Plane = Redplane[200:700,600:900];
cv2.imshow('Red plane cropped image',Red_Plane);

cv2.waitKey(0)
cv2.destroyAllWindows()
