import cv2
##import matplotlib.pyplot as plt

Img=cv2.imread('D:\Pictures\Anime&Misc\Graduation certificte.png');
##plt.title('Image')
##plt.imshow(Img)
cv2.imshow('Original',Img);
gray = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY);
cv2.imshow('Gray',gray);

cv2.waitKey(0)
cv2.destroyAllWindows()
