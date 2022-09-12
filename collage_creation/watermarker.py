import cv2
import numpy as np
import matplotlib.pyplot as plt

def markImage(filenum, id):
    img = cv2.imread('unlabeled2/{}_18-collage.png'.format(filenum))
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Check data type of original image  

    # Notice the usage of shape attribute to create image of exact same size. Zeros is to create a black image    
    blank_img = np.zeros(shape=(img_rgb.shape[0],img_rgb.shape[1],3), dtype=np.uint8) 

    # notice flip of x and y or org with image shape
    font = cv2.FONT_HERSHEY_SIMPLEX  
    cv2.putText(blank_img,  
                text='{}; #{}'.format(id, filenum),  
                org=(0, 128),   
                fontFace=font,  
                fontScale= 4,color=(255,255,255),  
                thickness=8,  
                lineType=cv2.LINE_4)  

    # original image is made a little light and watermark dark  
    blended = cv2.addWeighted(src1=img_rgb,alpha=0.7,src2=blank_img,beta=0.4, gamma = 0)  

    # make sure to use the correct color channels  
    cv2.imwrite('watermarked/{}.png'.format(filenum), cv2.cvtColor(blended, cv2.COLOR_RGB2BGR))
    
import csv

with open("datasets/Annotated FAA Dataset.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    line_count = 1
    print(csvreader)
    previous_id = None
    for row in csvreader:
    
        ##throw away the first line as it contains labels
        if line_count == 1:
            line_count += 1
        else:
            if(row[1] != '1' and row[1] != '0' and previous_id != row[0]):
                print(line_count)
                previous_id = row[0]
                markImage(line_count, row[0])
            line_count += 1