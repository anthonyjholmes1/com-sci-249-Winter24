# com-sci-249-Winter24


## Overview of the repo

There are three sections
1. Code
2. Data
3. Report

They should be self explanatory.

### Code
I have broken this up into two sections, clean up scripts and Google Colab Notebooks. The clean up scripts shouldnt be necessary for running the notebooks as the dat has already been cleaned. 

### Data
It is broken into two sections, the wildfires, and the weather. The weather data is broken up into different years as its huge, there are a lot of datapoints

### Reports
They're just copy of the reports submitted.

## How to run

1. I used my Google Drive to store and run the files in the notebooks. Youll need create a folder in the root drive called CS249-Winter2024-Project.
2. In the git repo, copy the ca_state_boundary folder thats in the Data folder into the CS249-Winter2024-Project folder in Google Drive.
3. In the git repo, copy the weather_202x.csv files into the CS249-Winter2024-Project folder in Google Drive.
4. In the git repo, copy the wildfires.csv file into the CS249-Winter2024-Project folder in Google Drive.
5. Run the Data_transformations.ipynb file. it will create a bunch of other files that will be stored in your Google Drive.
6. Run the Stations_data.ipynb file.
7. Run the Closest_stations.ipynb file.
8. Run the stations_and_wildfires.ipynb file.
9. Run the Elevation_study.ipynb file.



### Data 
1. https://www.ncei.noaa.gov/pub/data/ghcn/daily/by_year/


### Stations data explanation
These variables have the following definitions:

ID         is the station identification code.  Note that the first two
           characters denote the FIPS  country code, the third character 
           is a network code that identifies the station numbering system 
           used, and the remaining eight characters contain the actual 
           station ID. 

           See "ghcnd-countries.txt" for a complete list of country codes.
	   See "ghcnd-states.txt" for a list of state/province/territory codes.

           The network code  has the following five values:

           0 = unspecified (station identified by up to eight 
	       alphanumeric characters)
	   1 = Community Collaborative Rain, Hail,and Snow (CoCoRaHS)
	       based identification number.  To ensure consistency with
	       with GHCN Daily, all numbers in the original CoCoRaHS IDs
	       have been left-filled to make them all four digits long. 
	       In addition, the characters "-" and "_" have been removed 
	       to ensure that the IDs do not exceed 11 characters when 
	       preceded by "US1". For example, the CoCoRaHS ID 
	       "AZ-MR-156" becomes "US1AZMR0156" in GHCN-Daily
           C = U.S. Cooperative Network identification number (last six 
               characters of the GHCN-Daily ID)
	   E = Identification number used in the ECA&D non-blended
	       dataset
	   M = World Meteorological Organization ID (last five
	       characters of the GHCN-Daily ID)
	   N = Identification number used in data supplied by a 
	       National Meteorological or Hydrological Center
           P = "Pre-Coop" (an internal identifier assigned by NCEI for station
               records collected prior to the establishment of the U.S. Weather
               Bureau and their management of the U.S. Cooperative (Coop) 
               Observer Program
	   R = U.S. Interagency Remote Automatic Weather Station (RAWS)
	       identifier
	   S = U.S. Natural Resources Conservation Service SNOwpack
	       TELemtry (SNOTEL) station identifier
           W = WBAN identification number (last five characters of the 
               GHCN-Daily ID)

LATITUDE   is latitude of the station (in decimal degrees).

LONGITUDE  is the longitude of the station (in decimal degrees).

ELEVATION  is the elevation of the station (in meters, missing = -999.9).


STATE      is the U.S. postal code for the state (for U.S. stations only).

NAME       is the name of the station.

GSN FLAG   is a flag that indicates whether the station is part of the GCOS
           Surface Network (GSN). The flag is assigned by cross-referencing 
           the number in the WMOID field with the official list of GSN 
           stations. There are two possible values:

           Blank = non-GSN station or WMO Station number not available
           GSN   = GSN station 

HCN/      is a flag that indicates whether the station is part of the U.S.
CRN FLAG  Historical Climatology Network (HCN) or U.S. Climate Refererence
          Network (CRN).  There are three possible values:

           Blank = Not a member of the U.S. Historical Climatology 
	           or U.S. Climate Reference Networks
           HCN   = U.S. Historical Climatology Network station
	   CRN   = U.S. Climate Reference Network or U.S. Regional Climate 
	           Network Station

WMO ID     is the World Meteorological Organization (WMO) number for the
           station.  If the station has no WMO number (or one has not yet 
	   been matched to this station), then the field is blank.  
