import cv2
import os


path = "images/"
images = []

for file in os.listdir(path):
    name,ext = os.path.splitext(file)
    if ext in [".gif",".png" , ".jpg", ".jpeg",".jfif"]:
        file_name = path+"/"+file
        print(file_name)
        images.append(file_name)
count = len(images)
frame = cv2.imread(images[0])
height,width,channels = frame.shape
size= (width,height)
print(size)
out = cv2.VideoWriter("Project.avi",cv2.VideoWriter.fourcc(*"DIVX"),0.8,size)
for i in range(0,count-1):
    cv2.imread(frame)

out.write()
print("done")