import cv2 
import numpy as np

def nothing(x):
    pass

cap=cv2.VideoCapture(0);#taking input from camera

cv2.namedWindow("Color")
cv2.createTrackbar("LH","Color",0,255,nothing)#for lower Hue
cv2.createTrackbar("LS","Color",0,255,nothing)#for lower saturation value
cv2.createTrackbar("LV","Color",0,255,nothing)#for lower value
cv2.createTrackbar("UH","Color",255,255,nothing)#for Upper Hue
cv2.createTrackbar("US","Color",255,255,nothing)#for upper saturation
cv2.createTrackbar("UV","Color",255,255,nothing)#for upper value
#we will take a range of HSV value and detect the object in that range

while(True):
    res, frame= cap.read()

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#converting the frame to HSV
    #getting values from trackbar
    l_h=cv2.getTrackbarPos("LH","Color")
    l_s=cv2.getTrackbarPos("LS","Color")
    l_v=cv2.getTrackbarPos("LV","Color")

    u_h=cv2.getTrackbarPos("UH","Color")
    u_s=cv2.getTrackbarPos("US","Color")
    u_v=cv2.getTrackbarPos("UV","Color")

    l_hsv=np.array([l_h,l_s,l_v])#lower range of HSV value
    u_hsv=np.array([u_h,u_s,u_v])#Upper range of HSV value
    #masking of the frame
    mask=cv2.inRange(hsv,l_hsv,u_hsv)

    #applying mask through frame using bitwise and 
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("result",res)

    key=cv2.waitKey(1)#to take response from keyboard
    if key==27:
        break
cv2.destroyAllWindows()
cap.release()


