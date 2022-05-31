import cv2
import mediapipe as mp

#used to drawing the interconnecting lines in b/w landmarks
mp_drawing= mp.solutions.drawing_utils 

#used to tracking the hands in real time
mphands=mp.solutions.hands 

cap=cv2.VideoCapture(0)
hands=mphands.Hands()

while True:
    #calling webcam fun
    data,image=cap.read()

    #flip image bcoz generally in web cam it takes mirror image
    # when we did the flip it gives selfie view image
    image=cv2.cvtColor(cv2.flip(image,1),cv2.COLOR_BGR2RGB)

    #storing the results and it stores our hands and patterns
    results=hands.process(image) 

    #find landmarks in the results
    if results.multi_hand_landmarks:#checking results contain any landmark features or not
        for hand_landmarks in results.multi_hand_landmarks:
            #it draws the interconnecting lines in the hand landmarks
            mp_drawing.draw_landmarks(image,
                hand_landmarks,mphands.HAND_CONNECTIONS)
                
    cv2.imshow('Handtracker', image)
    cv2.waitKey(1)
    
    
