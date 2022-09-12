import cv2
import numpy

im = cv2.imread("testing18-collage.png")
a = numpy.asarray(im)

print(numpy.size(a, 0))

for x in range(0, numpy.size(a, 0) - 320, 320):
    print(x)
    for y in range(0, numpy.size(a, 0) - 320, 320): 
        cv2.imshow('image',a[x:x+640, y:y+640])
        cv2.imwrite('windowed\subset{}-{}.png'.format(x, y), a[x:x+640, y:y+640])
        cv2.waitKey(1000)