"""Collects positive images based on how 'Database_structure.csv' file is setup.
NOTE: there is a 25,000 image a day limit for the google maps static API. However as there is less than 10,000 positive samples this should not be a problem.
NOTE ALSO: All positive samples should have been confirmed at some point, meaning that imagery should be available for everything.
"""
import csv

##Custom library import
import sys
sys.path.insert(1, '../lib')
import satellite_imagery
print(satellite_imagery.maptype)
##
zoom = 18

meta_data = csv.reader(open("../datasets_positive/#Database_structure.csv"), delimiter=',')
for meta_row in meta_data:
    if meta_row[0] == ('file_name'):
        continue
    line_count = 1
    print(meta_row[0])
    with open('../datasets_positive/{}'.format(meta_row[0])) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            if line_count == 1:
                 line_count +=1
            else:
                if row[int(meta_row[1])].strip()== "1":
                    file_name = "../raw_data/1/{}_{:04d}.png".format(meta_row[4].strip(), line_count)
                    image = satellite_imagery.grab_image(row[int(meta_row[2])], row[int(meta_row[3])], zoom, file_name)
                    print('line: {} \t name: {}'.format(line_count, file_name))
                line_count += 1
print('done')
    
