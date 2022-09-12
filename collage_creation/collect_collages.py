import csv

##Custom library import
import sys
sys.path.insert(1, '../lib')
import satellite_imagery
print(satellite_imagery.maptype)
##

zoom = 18
step = 0.95
radius = 2
    
###
with open("datasets/Annotated FAA Dataset.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    line_count = 1
    previous_id = None
    for row in csvreader:
        ##throw away the first line as it contains labels
        if line_count == 1:
            line_count += 1
        else:
            if(row[1] != '1' and row[1] != '0' and previous_id != row[0]):
                satellite_imagery.createCollage(float(row[9]), float(row[10]), zoom, step, radius,  "unlabeled2\\{}.png".format(line_count))
                previous_id = row[0]
            line_count += 1
        
