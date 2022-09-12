import json
import cv2
import numpy
import random
import pandas
import math

##Custom library import
import sys
sys.path.insert(1, '../lib')
import satellite_imagery
print(satellite_imagery.maptype)
##

csv_d = pandas.read_csv("../datasets_positive/Annotated FAA Dataset.csv")

zoom = 18
random.seed("032")
rdm = 150  #Max slide in pixels so that the helipads is not always centered
sample_size = [640, 640]
source_image_size = [3072, 3072]

with open('../datasets_positive/labelbox_export-2020-11-03T18 22 36.922Z.json', 'r') as file:
    data = file.read()
data = json.loads(data)

print(csv_d.iloc[0][0])



for row in data:
    print(row["External ID"])    
    if("objects" in row["Label"]):
        file = row["External ID"].split(".")
        im_number = file[0]
        
        lat = csv_d.iloc[int(im_number)-2][9]
        lon = csv_d.iloc[int(im_number)-2][10]
        print("{} {}".format(lat, lon))
        
        meters_per_pixel = 156543.03392 * math.cos(lat * math.pi / 180) / math.pow(2, zoom)
        
        lat_per_meter = 1/111320
        lon_per_meter = 1/(40075000 * math.cos(lat * math.pi/180) / 360)
        
        lat_per_pixel = lat_per_meter * meters_per_pixel
        lon_per_pixel = lon_per_meter * meters_per_pixel
        
        number = 0
        for object in row["Label"]["objects"]:
            print("({})".format(object["value"]))
            if(object["value"] == "no_helipad" or object["value"] == "no_image"):
                print("skipping")
                continue
            box = object["bbox"]
            centerV_pixels = box["top"] + (box["height"] >> 1)
            centerH_pixels = box["left"] + (box["width"] >> 1)
            
            shiftV_pixels = random.randrange(-rdm, rdm, 1)  #This offset is to ensure that the network will have some examples that are not centered
            shiftH_pixels = random.randrange(-rdm, rdm, 1)  #This offset is to ensure that the network will have some examples that are not centered
            
            pixels_from_centerV = centerV_pixels + shiftV_pixels - (source_image_size[1] >> 1)
            pixels_from_centerH = centerH_pixels + shiftH_pixels - (source_image_size[0] >> 1)
            
            
            lat_poll = lat - lat_per_pixel * pixels_from_centerV
            lon_poll = lon + lon_per_pixel * pixels_from_centerH
            
            print("{} {}".format(lat_poll, lon_poll))
            satellite_imagery.grab_image(lat_poll, lon_poll, zoom, "../raw_data/1/FA3_{}_{}.png".format('{:04}'.format(int(im_number)),number))
            
            
            
            number = number + 1