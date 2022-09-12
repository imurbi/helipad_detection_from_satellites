# helipad_detection_from_satellites
This branch contains the code used for collecting the satellite imagery needed for use in training neural networks.

## Getting started
The code is intended to collect satellite imagery from the google maps static API. In order to work with this API, permission is needed.

#### Collect API key
setup a project, and requeset usage of the API. From their generate an API key and copy this API key. setup instructions can be found at....
https://developers.google.com/maps/gmp-get-started

#### Add API key to code.
In "lib/satellite_imagery.py" there is an unset variable "api_key" on line 6. In order to collect satellite imagery, api_key should be set to the API key from google.

#### setup environment
Most of the used code relies on CV2 and numpy and should be installed. A few additional libraries may be required for some of the scripts

## Collecting the datatset
All the code needed to collect a dataset to train is found in dataset_creation, and to create a dataset the following steps should be done

### Run "collect_raw_positives.py"
"collect_raw_positives.py" is a script that takes the datasets in the "dataset_positive" folder. The files and columns in those files to parse is defined in #databse_structure

### Run "collect_negative_coordinates"/recollect_raw_negatives
"recollect_raw_negatives.py" creates a dataset of 10,000 coordinates "valid" coordinates, and collects those images. "recollect_raw_negatives" will go over the datasets defined in #random_ranges and collect images of those coordinates
NOTE: that it is recomended to add all sampling parameters used in collect_negative_coordinates to #random_ranges to keep a record, and recollect the images later.
NOTE2: a "valid" coordinate is a coordinate where imagery is available.

### etc. code "collect_FA1_negatives.py"/"labelbox_parser_API_calls.py"
collect_FA1_negatives will collect the samples labeled as "0" in the FA1 dataset. labelbox_parser_API_calls will collect imagery on labelbox from the FA1 dataset. NOTE: the directories need to be specified differently as this has 8 classes

### "curate_dataset.py"
This will move all positive imagery, and the amount of imagery specified in #random_ranges and move the data to a separate folder for training purposes.

### "single_parse.py"
This will collect imagery from a specified .csv file. This is included for collecting imagery to evaluate.
