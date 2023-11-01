

####################################### this is only a rough version ######################################

# import the necessary packages
import cv2
import numpy as np

ball_colors = {'red', 'green', 'blue'}

# color ranges in bgr order for inRange function
## you will need to tune the values based on your camera and real-world condition ##
## since in different environment, the color of the box may be different because of the light or some other factors ##
color_ranges = {'red': {'Lower': np.array([0,50,50]), 'Upper': np.array([10,255,255])},
                'blue': {'Lower': np.array([98,50,50]), 'Upper': np.array([139,255,255])},     
                'green': {'Lower': np.array([30, 150, 20]), 'Upper': np.array([255, 255, 100])}}

# capture the video from the camera
## 0 means the first camera, If your computer has a built-in webcam, then "0" typically represents it ##
## so if you have an external camera, you may need to change it to "1" or "2" ##

cap = cv2.VideoCapture(0)
color=input()
# check if the camera is opened successfully
while cap.isOpened():
    # capture frame-by-frame
    ret, frame = cap.read()
    if ret:
        if frame is not None:
            ###### main part of your code ######

            cap_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            color_mask={}
            if(color == "red" or color == 'blue'): 
                lower=color_ranges[color]["Lower"]
                upper=color_ranges[color]["Upper"]
                color_mask=cv2.inRange(cap_frame,lower,upper)

            # show the frame
            colorfinal=cv2.bitwise_and(frame,frame,mask=color_mask) 
            cv2.imshow('frame', frame)
            cv2.imshow('color_mask',colorfinal) # to display the blue object output 
            cv2.waitKey(1)

            ###### end of this main part ######
        else:
            print("No picture, frame is empty")
    else:
        print("Cannot load camera")

# when everything is done, release the capture and close all windows
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()












