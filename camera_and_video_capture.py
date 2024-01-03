import numpy as np;
import cv2;

# Define a variable to access the webcam
camera_and_video_capture = cv2.VideoCapture(0);

def open_frame():
  while True:
    ret, frame = camera_and_video_capture.read();
    cv2.imshow('frame',frame);
    
    if(cv2.waitKey(1) & 0xFF == ord('q')):  #press q to quit frame
      break;                                                                                

# while True :
#   ret, frame = camera_and_video_capture.read();
#   cv2.imshow('frame',frame);
#   if cv2.waitKey(1) & 0xFF == ord('q'): #press q to quit frame
#     break;

open_frame();
camera_and_video_capture.release();
cv2.destroyAllWindows();