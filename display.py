import cv2
import os
import sys

def pick_vid():
	print("Pick video:")
	vid = input("1 - Happiness\n2 - Ice Cream Cake\n3 - Russian Roulette\n")

	if vid == '1':
		filename = 'happiness_list.txt'
	elif vid == '2':
		filename = 'ice_cream_cake_list.txt'
	elif vid == '3':
		filename = 'russian_roulette_list.txt'

	# Show contents of file
	with open(filename) as f:
			print(f.read())

	clip = input("Enter corresponding number of clip to open: ")

	dir = ''
	with open(filename) as fp:  
	   line = fp.readline()
	   count = 1
	   dir = line
	   while line:
	       line = fp.readline()
	       count += 1
	       if  str(count) == clip:
	       		dir = line
	       		break
	return dir.strip()       		

if __name__ == '__main__':
	dirpath = pick_vid()

	cascPath = "haarcascade_frontalface_default.xml"
	faceCascade = cv2.CascadeClassifier(cascPath)

	onlyfiles = os.listdir(dirpath)
	count = len(onlyfiles) - 1

	dir_results = dirpath+"detected"
	os.mkdir(dir_results)

	for fn in range(0,count):
		path = dirpath + "/frame" + str(fn) + ".jpg"
		images = cv2.imread(path,cv2.IMREAD_COLOR)
		gray = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
		faces = faceCascade.detectMultiScale(
	    	gray,
	    	scaleFactor=1.1,
	    	minNeighbors=5,
	    	minSize=(30, 30),
	        # flags = cv2.CV_HAAR_SCALE_IMAGE
	    )

		for f in faces:
			x, y, w, h = [ v for v in f ]
			cv2.rectangle(images, (x, y), (x+w, y+h), (0, 255, 0), 2)
			
			sub_face = images[y:y+h, x:x+w]

			img_scaled = cv2.resize(sub_face,(480, 480), interpolation = cv2.INTER_AREA)
			# cv2.imshow(str(f), img_scaled)

			#save images  after getting  high confidence for detection
			# cv2.imwrite(os.path.join(dir_results,str(f)+".jpg"),img_scaled)
			show = cv2.imshow("Images", images) 

		k = cv2.waitKey(1)
		if k == 27:
			break 

cv2.destroyAllWindows()
