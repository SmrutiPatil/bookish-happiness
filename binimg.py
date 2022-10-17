import cv2

img = cv2.imread('D:\Pictures\Anime&Misc\lol.png');
cv2.imshow('Original',img);

grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray',grey);

thresh,bandw = cv2.threshold(grey,100,255,cv2.THRESH_BINARY)
cv2.imshow('Binary',bandw)
cv2.imshow('BinThresh',thresh);

##cv2.imwrite('D:\Pictures\Anime&Misc\lol.png',bandw)

cv2.waitKey(0)
cv2.destroyAllWindows()
