"""This script is intended to create a "collage" of an area. The collage is a method to obtain an image with more than 640 x 640 pixels for a zoom level."""

##Custom library import
import sys
sys.path.insert(1, '../lib')
import satellite_imagery
print(satellite_imagery.maptype)
##

"""
lat = 61.22475
lon = -149.8390833
"""
name = 'TESTING.png'
lat = 34.050151
lon = -118.257040    
zoom = 18
step = 0.95 #1-overlap
radius = 5
radiuskm = 1 #Only used if radius == 0

meters_pixel = satellite_imagery.getMetersPerPixel(lat, zoom)
lat_pixel = meters_pixel * satellite_imagery.getLatPerMeter()
lon_pixel = meters_pixel * satellite_imagery.getLonPerMeter(lat)

##Code to assign radius to encompass the desired area in km
if radius == 0:
    radius_pix = (radiuskm * 1000) / meters_pixel
    radius_imgs = (radius_pix - img_size[0]/2) / (img_size[0] * step)
    print(radius_imgs)
    radius = math.ceil(radius_imgs)



print("Each pixel represents ....\n\t{} meters\n\t{}degrees latitude\n\t{}degrees longitude".format(meters_pixel, lat_pixel, lon_pixel))


###Use a sliding window to probe across a specific area

satellite_imagery.createCollage(lat, lon, zoom, step, radius, name)