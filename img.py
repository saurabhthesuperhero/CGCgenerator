from cv2 import imread
img=imread('pic.png')
for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        print('Cordinates:({},{}) rgbcode:{}'.format(i,j,img[i][j]))



