import sys
import PIL
from PIL import Image


if len(sys.argv) == 1:
	print("usage: python3 extract_frames.py imgfile nbofimages [outputprefix]");
else:
	inputpng= sys.argv[1]
	print("loading " + inputpng)
	im = Image.open(inputpng)

	n = int(sys.argv[2])
	print("to be cut in " + str(n) + " images");

	if len(sys.argv) == 3:
		outputpngprefix = inputpng[:-4]
	else:
		outputpngprefix = sys.argv[3]

	width, height = im.size 
	  
	for i in range(0,n):
            im1 = im.crop((0, i * height/n, width, (i+1)*height/n)) 
            im1.save(outputpngprefix + str(i) + ".png")
            
	print("done!")
