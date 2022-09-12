"""Common functions used for thte collection of satellite imagery"""
import urllib.request
import os, cv2, math
import numpy as np
endpoint = 'https://maps.googleapis.com/maps/api/staticmap?' #API calls are sent here. Will probably remain the same unless something happens
api_key = 
maptype = 'satellite' #maps can also be retrieved, but helipads are only visible from satellite imagery
size = [640, 640]#Note max size of imagery is 640 x 640. As the desired image will typically be of this size, and can be altered after collection, this will be fixed.

error_image = "../lib/error_image.png"
error_size = os.path.getsize(error_image)

def grab_image(lat, lon, zoom, filename):
    map_request = 'center={},{}&zoom={}&size={}x{}&maptype={}&key={}'.format(lat, lon, zoom, size[0], size[1], maptype, api_key)
    request = endpoint + map_request
    response = urllib.request.urlopen(request)
    image = response.read()
    #Unfortanetly ths call returns the image in binary mode, and the simplest way to work with it is to write the image and load it.
    file = open(filename, 'wb')
    file.write(image)
    file.close()
    
def is_no_image(filename):
    file_size = os.path.getsize(filename)
    if file_size < (error_size << 1): #If the image is not twice as big as the error image, it's either a no image message, or a very simple image.
        return True
    else:
        return False
        
def getMetersPerPixel(latitude, zoom):
    return 156543.03392 * math.cos(latitude * math.pi / 180) / math.pow(2, zoom)
    
def getLatPerMeter():
    return 1/111320
    
def getLonPerMeter(latitude):
    return 1/(40075000 * math.cos(latitude * math.pi/180) / 360)

def createCollage(lat, lon, zoom, step, radius, name):
    meters_pixel = getMetersPerPixel(lat, zoom)
    lat_pixel = meters_pixel * getLatPerMeter()
    lon_pixel = meters_pixel * getLonPerMeter(lat)
    
    start_lon = lon - radius*size[0]*step*lon_pixel
    grab_image(lat - radius*size[0]*step*lat_pixel, start_lon, zoom, "temp.png")
    cimage = cv2.imread("temp.png")
    for x in range(-1 * radius+1, radius + 1):
        clat = lat + (x * size[1] * step * lat_pixel)
        grab_image(clat, start_lon, zoom, "temp.png")
        image = cv2.imread("temp.png")
        cimage = np.concatenate((image[0:int(size[0] * step), :], cimage), axis=0)
    cv2.imwrite("col.png", cimage)
    for y in range(-1 * radius+1, radius + 1):
        clon = lon + (y * size[0] * step * lon_pixel)
        print(clon)
        grab_image(lat - radius*size[1]*step*lat_pixel, clon, zoom, "temp.png")
        temp = cv2.imread("temp.png")
        for x in range(-1 * radius+1, radius + 1):
            clat = lat + (x * size[0] * step * lat_pixel)
            grab_image(clat, clon, zoom, "temp.png")
            image = cv2.imread("temp.png")
            temp = np.concatenate((image[0:int(size[0] * step), :], temp), axis=0)
        cv2.imwrite('col.png', temp)
        cimage = np.concatenate((cimage, temp[:, int(size[0] * (1-step)):640]), axis=1)

    cv2.imwrite(name, cimage)