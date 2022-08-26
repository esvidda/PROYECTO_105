from fileinput import filename
import os
import cv2
path="Images/"
images=[]

for files in os.listdir(path):
    name,ext=os.path.splitext(files)
    if ext in ['.gif','.png','.jpg','.jpeg','.jfif']:
        filename=path+"/"+files
        print(filename)
        images.append(filename)

print(len(images))
count=len(images)

frame=cv2.imread(images[0])
height,width,layers=frame.shape
size=(width,height)

out=cv2.VideoWriter('proyect.mp4',cv2.VideoWriter_fourcc(*'XVID'),0.8,size)
for i in range(0,count):
    print(images[i])
    frame=cv2.imread(images[i])
    out.write(frame)

out.release()
print("listo")