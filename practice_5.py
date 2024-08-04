#text, shapes, lines in opencv
import cv2
import numpy as np

#image=np.zeros((400,400)) #created a plain black window first 
image=np.zeros((400,400,3),np.uint8) #added channel for colors
image[:]=0,255,0 #green color box
#create lines
cv2.line(image,(0,0),(image.shape[1],image.shape[0]),(255,0,0),2) 

#create rectangle
cv2.rectangle(image,(0,0),(100,200),(0,0,255),cv2.FILLED)

#create circle
cv2.circle(image,(200,200),20,(0,0,255),2)

#text
cv2.putText(image,"Helloooo",(300,300),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2)

cv2.imshow('output window',image)
cv2.waitKey(0)
cv2.destroyAllWindows()