import time
import cv2
import mediapipe as mp

mp_hands=mp.solutions.hands
hands=mp_hands.Hands()

mp_draw=mp.solutions.drawing_utils#for drawing landmarks for the hands

prev_time=0
curr_time=0

cap=cv2.VideoCapture(0)#using we cam 0 for video capturing

while cap.isOpened():
    sc,img=cap.read()#reading the frame
    img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)#converting to RGB from BGR
    
    hnd_proces=hands.process(img_rgb)#it processes the hand captured in the frame
    
    if hnd_proces.multi_hand_landmarks: #if there is no hand detected then there will be none multihand landmarks, but if hand is detected then we can proceed further
        for hnd_lm in hnd_proces.multi_hand_landmarks:#looping through each landmark
            
            for id,lnd in enumerate(hnd_lm.landmark):
                #id relates to the index number relating to the index of our finger landmark
                height,width,channels=img.shape
                #we will multiply the lnd with these image shapes as lnd is the ratio of these and we need the value in pixels for performing any operation
                cx, cy=int(lnd.x*width),int(lnd.y*height)
                #these are the co-ordinates of all the landmarks in the shown video
                if id==12:
                    cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)
                
                
            mp_draw.draw_landmarks(img,hnd_lm,mp_hands.HAND_CONNECTIONS)
            
    
    
    
    curr_time=time.time()
    fps=1/(curr_time-prev_time)#frame rates per sec
    prev_time=curr_time
    
    #putting the frame rate on the image
    
    
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,255,0),2)
    cv2.imshow("Video:",img)
    
    if(cv2.waitKey(40)==27):
        break
    
    
cv2.destroyAllWindows()
cap.release()


