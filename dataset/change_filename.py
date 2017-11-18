import glob, os

def rename(path):
	files = glob.glob(path + '/*.jpg')
	print(files)
	i = 0
	for f in files:
		filename = '5.' + str(i) + '.jpg'
		print(filename)
		os.rename(f, os.path.join(path, filename))
		i += 1

if __name__ == '__main__':
	rename('Yeri')