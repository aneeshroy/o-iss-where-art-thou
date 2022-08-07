# o-iss-where-art-thou

## Overview

This repo contains the files used to run a fully containerized Flask App for tracking ISS positions and sightings. The app allows a user to query and receive information from two data sets regarding the ISS positional and velocity data.

## Important Files

### app.py

app.py is the functions and setup for the Flask application and multiple routes to navigate through the data.

### test_app.py

test_app.py is a unit testing file for making sure the functions/routes in app.py run smoothly.

### Dockerfile/Makefile

The Dockerfile allows a user to build and run the application in a container instead of through a machine. The Makefile shortens many different Docker commands on running/using the application.

## Instructions

To begin, using the Makefile shortcut, pull the container image from Dockerhub with everything needed.

```
   make pull
```

If you want to build the application yourself, you wil have to run a different command first to download the data sets:

```
$ wget https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_OEM/ISS.OEM_J2K_EPH.xml
$ wget https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_sightings/XMLsightingData_citiesUSA04.xml
```

After this is in the same folder as the other files, then run

```
   make build
```

To start the application, type

```
   make run
```

## Using the Application

To start the Flask Application after the image is set, run the command

```
   flask run -p 5025
```

This will start the app running on the port 5025. Then open a new terminal in the folder, and run

```
$ curl localhost:5025/load_data -X POST
```

to ensure the data is loaded from the files into the memory. From here, type

```
$ curl localhost:5025/help
```

to see further commands.

##Example Commands/Outputs

```
curl localhost:5025/countries

United_States

curl localhost:5025/countries/United_States/regions

Illinois
Indiana
Iowa
Kansas

curl localhost:5025/epochs/2022-057T11:32:56.869Z

{
  "EPOCH": "2022-057T11:32:56.869Z", 
  "X": {
    "#text": "-1290.7899096751501", 
    "@units": "km"
  }, 
  "X_DOT": {
    "#text": "7.3499692086700303", 
    "@units": "km/s"
  }, 
  "Y": {
    "#text": "-4010.9432590792699", 
    "@units": "km"
  }, 
  "Y_DOT": {
    "#text": "-2.1650281407358598", 
    "@units": "km/s"
  }, 
  "Z": {
    "#text": "5322.5420820141298", 
    "@units": "km"
  }, 
  "Z_DOT": {
    "#text": "0.14615348535767", 
    "@units": "km/s"
  }
}
```

##Citations

Goodwin, S. (n.d.). ISS_COORDS_2022-02-13. NASA. https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_OEM/ISS.OEM_J2K_EPH.xml Retrieved August 3, 2022, from https://data.nasa.gov/Space-Science/ISS_COORDS_2022-02-13/r6u8-bhhq

Goodwin, S. (n.d.). XMLsightingData_citiesUSA04. NASA. Retrieved August 3, 2022, from https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_sightings/XMLsightingData_citiesUSA04.xml
