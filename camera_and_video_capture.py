import numpy as np;
import cv2;

# Define a variable to access the webcam
camera_and_video_capture = cv2.VideoCapture(0);  

def open_frame():
  while True:
    ret, frame = camera_and_video_capture.read();  #Open the webcam

    image = np.zeros(frame.shape, np.uint8); #Return an array

    cv2.imshow('frame', image);
    if(cv2.waitKey(1) & 0xFF == ord('q')):  #press q to quit frame
      break;                                                                                

open_frame();

# When everything done, release the capture
camera_and_video_capture.release(); 
cv2.destroyAllWindows();