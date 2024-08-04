#Open Cv
#import
import cv2

#load the image
img=cv2.imread('C:/Users/Ayushi/OneDrive/Desktop/my learning/open cv/sample img.jpg',1)#image path

#resize the image
img=cv2.resize(img,(200,200))

#rotate the image
img=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)

#image save
cv2.imwrite('output image.jpg',img)
#show the image
img=cv2.imshow('image display window',img)
cv2.waitKey(0) #wait until any action is taken
cv2.destroyAllWindows(img)




