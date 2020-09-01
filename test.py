import cv2
import numpy as np

cap = cv2.VideoCapture('a.mp4')
bg=None

lower1 = np.array([20,40,92],np.uint8)
upper1 = np.array([20,255,255],np.uint8)
lower2 = np.array([24,33,95],np.uint8)
upper2 = np.array([24,255,255],np.uint8)
lower3 = np.array([23,34,96],np.uint8)
upper3 = np.array([23,255,255],np.uint8)
lower4 = np.array([21,50,100],np.uint8)
upper4 = np.array([21,255,255],np.uint8)
lower5 = np.array([22,38,93],np.uint8)
upper5 = np.array([22,255,255],np.uint8)
lower6 = np.array([22,41,90],np.uint8)
upper6 = np.array([22,255,255],np.uint8)
lower7 = np.array([24,32,96],np.uint8)
upper7 = np.array([24,255,255],np.uint8)
while True:
    _,img = cap.read()

    if bg is None:
        bg = img

    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(hsv,lower1,upper1)
    mask2 = cv2.inRange(hsv, lower2, upper2)
    mask3 = cv2.inRange(hsv, lower3, upper3)
    mask4 = cv2.inRange(hsv, lower4, upper4)
    mask5 = cv2.inRange(hsv, lower5, upper5)
    mask6 = cv2.inRange(hsv, lower6, upper6)
    mask7 = cv2.inRange(hsv, lower7, upper7)
    mask = cv2.add(mask1,mask4)
    mask = cv2.add(mask,mask3)
    mask = cv2.add(mask, mask5)
    mask = cv2.add(mask, mask6)
    mask = cv2.add(mask, mask7)
    mask = cv2.medianBlur(mask,13)
    kernel = np.ones((5,5),np.uint8)
    mask = cv2.dilate(mask,kernel,iterations=1)

    areacolor = cv2.bitwise_and(bg,bg,mask=mask)
    maskInv = cv2.bitwise_not(mask)
    sinAreaColor = cv2.bitwise_and(img,img,mask=maskInv)
    finalFrame = cv2.addWeighted(areacolor,1,sinAreaColor,1,0)

    cv2.imshow('VIDEO', img)
    cv2.imshow('MASK', mask)
    cv2.imshow('JADOO', finalFrame)
    cv2.waitKey(5)

cap.release()

cv2.destroyAllWindows()