from cv2 import imread
import numpy as np
f=open("cfile.cpp","w+")
img=imread('temp.png')

f.write('#include<iostream.h>\n#include<conio.h>\n#include <graphics.h>\nvoid main()\n{ int i;\nint gd=DETECT,gm,color;\n initgraph(&gd,&gm,"c://turboc3//bgi");\n')
x=[]
y=np.array([0,0,0])
for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):

        if np.array_equal(img[i][j], [0,0,0]) is True: 
            #print('Cordinates:({},{}) rgbcode:{}'.format(i,j,img[i][j]))
            yup='\nputpixel({},{},WHITE);'.format(i,j)
 #           print(yup)
            f.write(yup)
            
f.write("getch();\n\nclosegraph(); \n}")
f.close()
print("ok")


