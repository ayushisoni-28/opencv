#basic functions in open cv:
import cv2
import numpy as np
kernel=np.ones((5,5),np.uint8)
image=cv2.imread('C:/Users/Ayushi/OneDrive/Desktop/my learning/open cv/sample img.jpg')
cv2.imshow('Output window',image)
#change the color scale to gray
image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('Output window gray image',image_gray)

#change the blurness
image_blurrness=cv2.GaussianBlur(image_gray,(7,7),0) #blur scale
cv2.imshow('Output window blur',image_blurrness)

#Edge in image
image_canny=cv2.Canny(image_gray,100,100)
cv2.imshow('Output window edge',image_canny)

#image thickness
image_dialtor=cv2.dilate(image_canny,kernel,iterations=1)
cv2.imshow('Output window thickness',image_dialtor)

#image thinness
image_eroded=cv2.erode(image_dialtor,kernel,iterations=1)
cv2.imshow('Output window thinness',image_eroded) 

cv2.waitKey(0)
cv2.destroyAllWindows()