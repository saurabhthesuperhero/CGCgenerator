from cv2 import imread
import numpy as np
img=imread('pic.png')
x=[]
y=np.array([0,0,0])
for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):

        if np.array_equal(img[i][j], [0,0,0]) is True: 
            print('Cordinates:({},{}) rgbcode:{}'.format(i,j,img[i][j]))
            
print("ok")

