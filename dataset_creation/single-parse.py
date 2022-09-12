"""Collects imagery from coordinates and deposists the images in a specified folder. Note that this to collect unlabeled imagery.
"""

import csv
import os

##Custom library import
import sys
sys.path.insert(1, '../lib')
import satellite_imagery
print(satellite_imagery.maptype)
##

src_file = '../datasets_positive/Sheet_1_data.csv'
lat_col = 2
lon_col = 3
dst_directory = 'grabs2/unlabeled'

zoom = 18

line_count=1
with open(src_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        if line_count ==1:
            line_count +=1
        else:
            file_name = os.path.join(dst_directory, "TEST_{:04d}.png".format(line_count))
            image = satellite_imagery.grab_image(row[lat_col], row[lon_col], zoom, file_name)
            print('line: {} \t name: {}'.format(line_count, file_name))
            line_count += 1
print('done')
    
