# Meta
Hidden flag in JPG-Metadata.

**Description of the Challenge:**
Another Image for you. Take a look!

## Setup
Edit the JPG-Metadata and and hide the flag.

## Solution
Solve this challenge with "exiftool" or something similar. First part of the flag is in "Comment". For the second part you have to get the GPS Coordinates and calculate the decimal values. The last part is to find the City with the given GPS Coordinates.
Flag: THICTF{w4tch_y0ur_metadata_<Latitude in %.2f>_<Longitude in %.2f>_<City at (Lat,Lon)>}
Where:
* Lat = 48 deg 46' 0.70" N -> 48.77
* Lon = 11 deg 25' 55.44" E -> 11.43
* City = Ingolstadt

## Flag
THICTF{w4tch_y0ur_metadata_48.77_11.43_Ingolstadt}
