import cv2
import os
import numpy as np
from PIL import Image


def name(id):
	if id == 1:
		return 'Irene'
	elif id == 2:
		return 'Seulgi'
	elif id == 3:
		return 'Wendy'
	elif id == 4:
		return 'Joy'
	elif id == 5:
		return 'Yeri'
	
def recognize(path):	
	image_paths = [os.path.join(path,f) for f in os.listdir(path)]
	for image_path in image_paths:
		predict_image_pillow = Image.open(image_path).convert('L')
		predict_image = np.array(predict_image_pillow, 'uint8')
		# faces = detector.detectMultiScale(predict_image)
		# for (x, y, w, h) in faces:
		nbr_predicted, conf = recognizer.predict(predict_image)
		nbr_actual = int(os.path.split(image_path)[1].split(".")[0])
		count = int(os.path.split(image_path)[1].split(".")[1])
		actual_name = name(nbr_actual)
		if nbr_actual == nbr_predicted:
			print("{} - {} is correctly recognized with {} confidence".format(actual_name, count,conf))
		else:
			print("{} - {} is incorrectly recognized as {}".format(actual_name, count, conf))
		cv2.imshow("Recognizing Face", predict_image)
		cv2.waitKey(1000)

if __name__ == '__main__':
	recognizer = cv2.face.LBPHFaceRecognizer_create()
	recognizer.read('trainer/trainer.yml')
	
	detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
	recognize('dataset/TestingSet')