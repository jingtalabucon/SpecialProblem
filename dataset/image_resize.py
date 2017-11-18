#check frames extracted from video
#python display.py [folder name]/[folder name]

import cv2
import os
import sys

dir = sys.argv[1]
print(dir)

folder = "Resize"
# os.mkdir(folder)
onlyfiles = next(os.walk(dir))[2] 
count = len(onlyfiles)+1
for fn in range(1,count):
    path = dir + "/5." + str(fn) +".jpg"                #change name
    print (path)
    images = cv2.imread(path)
    img_scaled = cv2.resize(images,(480, 480), interpolation = cv2.INTER_AREA)
    cv2.imwrite(os.path.join(folder,"5.{}.jpg".format(fn)), img_scaled)     #change name
    