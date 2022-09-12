import cv2
import numpy
import os

img_size = (18880, 18880, 3)

img = numpy.empty(img_size)
cls = "P"

folder = "windowed_prediction/{}".format(cls)
for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        im = cv2.imread(file_path)
        
        a = numpy.asarray(im)
        
        print(filename[6:-4].split("-"))
        indices = filename[6:-4].split("-")
        if('18560' in indices):
            print('skipping')
            continue
        sub_img = a[160:480, 160:480]
        cv2.imshow('image', sub_img)
        img[int(indices[0])+160:int(indices[0])+480, int(indices[1])+160:int(indices[1])+480] = sub_img
        
        cv2.waitKey(1000)
        
cv2.imshow('image', img)
cv2.imwrite('final{}.png'.format(cls), img)