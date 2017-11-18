import cv2
import os
import sys
import numpy as np
from PIL import Image

def getImagesAndLabels(path):
	image_paths = [os.path.join(path,f) for f in os.listdir(path)]
	images = []
	labels = []
	for image_path in image_paths:
		image_pillow = Image.open(image_path).convert('L')
		image_np = np.array(image_pillow,'uint8')
		label = int(os.path.split(image_path)[1].split(".")[0])
		faces = detector.detectMultiScale(image_np)
		# faces = faceCascade.detectMultiScale(image)
		# for (x,y,w,h) in faces:
			# images.append(image_np[y:y+h,x:x+w])
			# labels.append(label)
		labels.append(label)
		images.append(image_np)
	return images, labels

if __name__ == '__main__':
	recognizer = cv2.face.LBPHFaceRecognizer_create()
	detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

	faces, labels = getImagesAndLabels("dataset/TrainingSet")
	recognizer.train(faces, np.array(labels))
	recognizer.write('trainer/trainer.yml')