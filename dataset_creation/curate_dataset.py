"""Extra imagery was collected for the sake of being able to adjust the negative set as desired. As a result, only a subset of data is to be used. This code creates that subset.
"""
import os, csv, shutil
###Note that to keep the test set separate, the test set will consist of only and all samples ending in "0.png"


###Move everything in the +ive set (As this is the limitting set)
sd = '../images_n/train/1'
dd1 = '../images/train/1'
dd2 = '../images/test/1'

for item in os.listdir(sd):
    s = os.path.join(sd, item)
    if '0.png' not in item:
        d = os.path.join(dd1, item)
    else:
        d = os.path.join(dd2, item)
    shutil.copy(s, d)

###Some of the images from the 0 set
sd = '../images_n/train/0'
dd1 = '../images/train/0'
dd2 = '../images/test/0'

meta_data = csv.reader(open("../datasets_negative/#random_ranges.csv"), delimiter=',')
for meta_row in meta_data:
    if meta_row[0] == ('lat1'):
        continue
    print(meta_row[5])
    
    for ind in range(2, 2+int(meta_row[4])):
        img = '{}_{:04d}.png'.format(meta_row[6].strip(), ind)
        s = os.path.join(sd, img)
        if '0.png' not in img:
            d = os.path.join(dd1, img)
        else:
            d = os.path.join(dd2, img)
        shutil.copy(s, d)
