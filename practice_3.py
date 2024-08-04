#capture webcam
import numpy as np
import cv2

#load the webcam
capture=cv2.VideoCapture(0)

while True:
    ret,frame=capture.read() #return false if webcam is open somewhere else...
    width=int(capture.get(3))
    height=int(capture.get(4)) #to know the actual height and width of window ...

    image=np.zeros(frame.shape,np.uint8) #creating a blank frame shize shape for multiple mirroring of black color
    
    small_frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)#shrink the image
    image[:height//2, :width//2]=cv2.rotate(small_frame,cv2.ROTATE_180) # top-left
    image[height//2:, :width//2]=small_frame #bottom left
    image[:height//2, width//2:]=cv2.rotate(small_frame,cv2.ROTATE_180) #top right
    image[height//2:, width//2:]=small_frame # bottom right

    cv2.imshow('Window frame',image)
    if cv2.waitKey(1)==ord('q'):
        break  # stop displaying when q pressed

capture.release() # exit the webcam
cv2.destroyAllWindows() #close the windows
