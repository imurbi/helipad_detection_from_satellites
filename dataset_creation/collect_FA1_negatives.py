"""NOTE: as negatives were requrested from specifically the FA1 set, this code was designed to collect negatives specifically from that set
"""
import csv

##Custom library import
import sys
sys.path.insert(1, '../lib')
import satellite_imagery
print(satellite_imagery.maptype)
##

###data-parse.py is a script that goes through a database, collects the longitude, and latitude coordinates, and then calls the google map API to retrieve an image at the given coordinates, with the given parameters


##Grab image function parameters
endpoint = 'https://maps.googleapis.com/maps/api/staticmap?'
api_key = 
maptype = 'satellite'
size = [1600, 1600]#Google will provide an image of size [min(640, x), min(640), y)] for zoom of 20 (other levels need testing)
zoom = 18

##Info of the structure of the CSV
file_name = "datasets/Annotated FAA Dataset.csv"
lat_pos = 9
long_pos = 10

##Main code. Goes through the CSV file parsing coordinates and saving the cordinates
#print(os.path.exists("datasets/heliports_with_runway_info.csv"))
with open(file_name) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    line_count = 4999
    print(csvreader)
    for row in csvreader:
    
        ##throw away the first line as it contains labels
        if line_count == 4999:
            print(row)
            line_count = 5000
        else:
            if row[1] == "0":
                folder = 0
                image = satellite_imagery.grab_image(row[lat_pos], row[long_pos], zoom, "images/train/{}/{}.png".format(folder, str(line_count)))
                print(line_count, row[lat_pos], row[long_pos])
                print("https://www.google.com/maps/@{},{},{}z".format(row[lat_pos],row[long_pos],zoom))
                line_count += 1
    
