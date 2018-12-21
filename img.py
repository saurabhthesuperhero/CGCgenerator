from cv2 import imread
import numpy as np
f=open("cfile.cpp","w+")
img=imread('temp.png')
cppcode='#include<iostream.h>\n \
#include<conio.h>\n \
#include <graphics.h>\n \
void main()\n \
{ int i,x,y;\n \
int gd=DETECT,gm,color;\n \
initgraph(&gd,&gm,"c://turboc3//bgi");\n'

x=[]
y=np.array([0,0,0])
count=0

x=0
y=0
ix=0
jy=0
for i in range(0,img.shape[0]):
    ix+=1
    for j in range(0,img.shape[1]):

        if np.array_equal(img[i][j], [0,0,0]) is False: 
            if np.array_equal(img[i][j],[255,255,255]) is True and count==0:
                count=1
                ix=i
                jy=j
                x=i
                y=j
            elif np.array_equal(img[i][j],[255,255,255]) is True:
                count=1
                jy+=1
            elif count==1:
                count=0
                cppcode+='\nfor (x='+str(x)+';x<'+str(ix)+';x++){\nfor(int y='+str(y)+';y<'+str(jy)+';y++) {putpixel(x,y,WHITE);\n}}'
            #print('Cordinates:({},{}) rgbcode:{}'.format(i,j,img[i][j]))
            else:
                cppcode+='\nputpixel({},{},({},{},{}));'.format(i,j,img[i][j][0],img[i][j][1],img[i][j][2])

            
cppcode+="getch();\n\nclosegraph(); \n}"    
print(cppcode)
f.write(cppcode)
f.close()
print("ok")


