"""This selects a region, and samples random coordinates in that region. Image collection was added so error checking(coordinates with no images) can be corrected
"""

import random, csv, os
import numpy as np

##Custom library import
import sys
sys.path.insert(1, '../lib')
import satellite_imagery
print(satellite_imagery.maptype)
##


seed = 777
random.seed(seed)
zoom = 18

###Set Values
#38.922530, -77.049838, 38.872616, -76.967839, 1000, DC, 03S
set_name = "DC"
child_name = "03S"
samples = 10000
lat_range = (38.922530, 38.872616)
lon_range = (-77.049838, -76.967839)

"""    
def is_no_image(filename):
    file_size = os.path.getsize(filename)
    if file_size < (error_size << 1): #If the image is not twice as big as the error image, it's either a no image message, or a very simple image.
        return True
    else:
        return False
"""

with open('../datasets_negative/{}-{}.csv'.format(set_name, samples), 'w', newline='') as csvfile:
    line_count = 1
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['latitude', 'longitude'])
    line_count += 1
    for i in range(0, samples):
        lat = random.uniform(lat_range[0], lat_range[1])
        lon = random.uniform(lon_range[0], lon_range[1])
        
        filename = "../raw_data/0/{}_{:04d}.png".format(child_name, line_count)
        satellite_imagery.grab_image(lat, lon, zoom, filename)
        while(satellite_imagery.is_no_image(filename)):
            lat = random.uniform(lat_range[0], lat_range[1])
            lon = random.uniform(lon_range[0], lon_range[1])
            satellite_imagery.grab_image(lat, lon, zoom, filename)
        print('line: {} \t name: {}'.format(line_count, filename))    
        writer.writerow([lat, lon])
        line_count += 1
        
    
            
