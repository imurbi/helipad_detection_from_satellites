import json
import cv2
import numpy
import random

random.seed("032") #Makes randomness repeatable
rdm = 100 #Random offset range in pixels. Helipad will be centered if this is set to 0
sample_size = [640, 640] #Sample size of the image. Will determine size of output image
expected_size = sample_size[0] * sample_size[1] * 3

##PATHS
json_file = 'datasets/export-2020-11-03T18 22 36.922Z.json'
#Source Image locations. Note that this assumes a specific format. (Should eventually be changed with retrieval from labelbox)
source_images = "unlabeled2/{}_18-collage.{}"
#output directory. ASSUMES SUBFOLDERS FOR LABELS.
output_dir = 'new-classes'
##

#json collected from labelbox(NOTE MAY REQUIRE SOME CLEANUP)
with open(json_file, 'r') as file:
    data = file.read()
data = json.loads(data)

for row in data:
    #External ID is the name of the uploaded file
    print(row["External ID"])
    
    if("objects" in row["Label"]): #Checks for the existence of labels for the image
        
        file = row["External ID"].split(".")
        im = cv2.imread(source_images.format(file[0], file[1]))
        a = numpy.asarray(im)
        print("unlabeled2/{}_18-collage.{}".format(file[0], file[1]))
        
        ###The are min values for the center. This ensures that the area to be taken is represented in the image
        minH = sample_size[0] / 2
        maxH = numpy.size(a, 0) - minH - 1
        
        minV = sample_size[1] / 2
        maxV = numpy.size(a, 1) - minH - 1
        ###
        
        number = 0 #Counter for number of labels in an image
        
        for object in row["Label"]["objects"]:
            print("({})".format(object["value"]))
            box = object["bbox"]
            
            ##Center of label
            centerV = box["top"] + (box["height"] / 2)
            centerH = box["left"] + (box["width"] / 2)
            ##Random noise so the helipad won't always be centered
            shiftH = random.randrange(-rdm, rdm, 1)
            shiftV = random.randrange(-rdm, rdm, 1)
            ##Bound the center to be in a valide range
            pollV = min(max(centerV + shiftV, minV), maxV)
            pollH = min(max(centerH + shiftH, minH), maxH)
            ##Find start of the box
            pollV = pollV - (sample_size[0] / 2)
            pollH = pollH - (sample_size[1] / 2)
            ##
            
            cv2.imshow('image',a[pollV:pollV+sample_size[0], pollH:pollH+sample_size[1]])
            if(numpy.size(a[pollV:pollV+sample_size[0], pollH:pollH+sample_size[1]]) != expected_size):
                print("Error: something went wrong here")
                exit()
            print('{}\{}\{}-{}.png'.format(output_dir, object["value"], file[0], number))
            cv2.imwrite('{}\{}\{}-{}.png'.format(output_dir, object["value"], file[0], number), a[pollV:pollV+sample_size[0], pollH:pollH+sample_size[1]])
            #cv2.waitKey(1000)
            number = number + 1
