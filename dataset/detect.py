import cv2
import os
import sys
import glob

path = sys.argv[1]
print(path)

files = glob.glob(path + '/*.jpg')
i = 0
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
for f in files:
	images = cv2.imread(f,cv2.IMREAD_COLOR)
	gray = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(
	    	gray,
	    	scaleFactor=1.1,
	    	minNeighbors=5,
	    	minSize=(30, 30),
# 	        # flags = cv2.CV_HAAR_SCALE_IMAGE
	    )
	label = int(os.path.split(f)[1].split(".")[0])
	count = int(os.path.split(f)[1].split(".")[1])
	# print(str(label) + '.' + str(count)) 
	for face in faces:
		x, y, w, h = [ v for v in face ]
		cv2.rectangle(images, (x, y), (x+w, y+h), (0, 255, 0), 2)
		sub_face = images[y:y+h, x:x+w]
		img_scaled = cv2.resize(sub_face,(480, 480), interpolation = cv2.INTER_AREA)
		newdir = "Detected"
		# filename = str(label) + '.' + ''
		# str(label)+ '.' + str(count) + ".jpg"
		cv2.imwrite(os.path.join(newdir, str(face)+".jpg"),img_scaled)
		show = cv2.imshow("Images", img_scaled) 
		show = cv2.imshow("Images", images)
		k = cv2.waitKey(1000)
		if k == 27:
			break