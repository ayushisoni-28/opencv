#shapes and arrays of image
import cv2
import random
#Accesing the pixels
img=cv2.imread('C:/Users/Ayushi/OneDrive/Desktop/my learning/open cv/sample img.jpg',1)
print(img[0][67]) #accesing the pixel with 0th row
print(img.shape) #(row,column,channels)

#changing pixel colors
'''for i in range(100): #100 rows
    for j in range(img.shape[1]):#shape of columns
        img[i][j]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]

'''
#copying a part of image and pasting it somewhere else:
part_cut=img[250:400,250:400]
img[150:300,150:300]=part_cut

cv2.imshow('Display window',img)
cv2.waitKey(0)
cv2.destroyAllWindows()




