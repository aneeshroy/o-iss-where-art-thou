from locale import format_string
from flask import Flask
import logging
import socket
import xmltodict

app = Flask(__name__)

pos_data = {}
sight_data = {}
format_str=f'[%(asctime)s {socket.gethostname()}] %(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
logging.basicConfig(level = logging.INFO, format = format_str)

@app.route('/help', methods=['GET'])
def help() -> str:
    
    """
    Gives all routes available in this app for ISS data

    Returns:
        A String of all commands that can be used
    """

    logging.info("all commands printed")

    commands = "/help - Information on how to interact with the application"
    commands += "\n/load_data - load data (XML) into app"
    commands += "\n/epoch - All Epochs in the positional data"
    commands += "\n/epoch/<epoch> - All information about a specific Epoch in the positional data" 
    commands += "\n/countries - All Countries from the sighting data"
    commands += "\n/countries/<country> - All information about a specific Country in the sighting data"
    commands += "\n/countries/<country>/regions - All Regions associated with a given Country in the sighting data"
    commands += "\n/countries/<country>/regions/<region> - All information about a specific Region in the sighting data"
    commands += "\n/countries/<country>/regions/<region>/cities - All Cities associated with a given Country and Region in the sighting data"
    commands += "\n/countries/<country>/regions/<region>/cities/<city> - All information about a specific City in the sighting data"

    return commands


@app.route('/load_data', methods = ['POST'])
def load_data() -> str:
    
    """
    Reads in XML data files as global dicts

    Returns:
        A string indicating the loading is successful.
    
    """

    logging.info('loading data\n')

    global pos_data
    global sight_data

    with open('ISS.OEM_J2K_EPH.xml','r') as pos:
        pos_data = xmltodict.parse(pos.read())

    with open('XMLsightingData_citiesUSA04.xml', 'r') as sight:
        sight_data = xmltodict.parse(sight.read())

    return 'Data loaded into application.\n'


@app.route('/epochs', methods=['GET'])
def epochs() -> str:
    
    """
    Takes all of the epochs from the positional data and displays as a string

    Returns:
        epochs: String containing all epochs
    
    """

    logging.info("getting epochs")

    epochs = ''

    for i in range(len(pos_data['ndm']['oem']['body']['segment']['data']['stateVector'])):
        epochs += (pos_data['ndm']['oem']['body']['segment']['data']['stateVector'][i]['EPOCH']) + "\n"

    return epochs

 
@app.route('/epochs/<epoch>', methods=['GET'])
def epoch_info(epoch: str) -> dict:

    """
    Finds the epoch given and returns all information about the specific epoch.

    Args:
        epoch: String of epoch name selected

    Returns:
       epoch_data: dictionary with position/velocity data for epoch selected
    
    """

    logging.info("getting epoch data for " + epoch)

    for i in range(len(pos_data['ndm']['oem']['body']['segment']['data']['stateVector'])):
        if (pos_data['ndm']['oem']['body']['segment']['data']['stateVector'][i]['EPOCH'] == epoch):
            epoch_data = pos_data['ndm']['oem']['body']['segment']['data']['stateVector'][i]

    return epoch_data


@app.route('/countries', methods=['GET'])
def countries() -> str:

    """
    Takes all of the countries from sighting data displays as a string

    Returns:
        countries: string of all countries in the sighting data

    """

    logging.info("getting countries")

    countries = ''

    for i in range(len(sight_data['visible_passes']['visible_pass'])):
        if sight_data['visible_passes']['visible_pass'][i]['country'] not in countries:
            countries += sight_data['visible_passes']['visible_pass'][i]['country'] + "\n"

    return countries 


@app.route('/countries/<country>', methods=['GET'])
def country_info(country: str) -> dict:

    """
    Returns all the data about a specific country from sighting data

    Args:
        country: string of country name selected

    Returns:
        country_info: A dictionary of all info about the country (all sightings)

    """

    logging.info("getting country data for " + country)

    country_info = []

    for i in range(len(sight_data['visible_passes']['visible_pass'])):
        if (sight_data['visible_passes']['visible_pass'][i]['country'] == country):
            country_info.append((sight_data['visible_passes']['visible_pass'][i]))

    return {country:country_info}


@app.route('/countries/<country>/regions', methods=['GET'])
def regions(country: str)-> str:

    """
    Gives all of the regions within a specified country

    Args:
        country: string name of the country

    Returns:
        regions: string of all of the regions

    """

    logging.info("getting regions in " + country)

    regions = ''

    for i in range(len(sight_data['visible_passes']['visible_pass'])):
        if (sight_data['visible_passes']['visible_pass'][i]['country'] == country):
            if sight_data['visible_passes']['visible_pass'][i]['region'] not in regions:
                regions += (sight_data['visible_passes']['visible_pass'][i]['region']) + "\n"

    return regions


@app.route('/countries/<country>/regions/<region>', methods=['GET'])
def region_info(country: str, region: str) -> dict:

    """
    Returns all the data about a specific region from sighting data

    Args:
        country: string of country name selected
        region: string of region name selected

    Returns:
        region_info: A list of dictionaries of all info about the region (all sightings)

    """

    logging.info("getting region data for " + region + ", " + country)

    region_info = []

    for i in range(len(sight_data['visible_passes']['visible_pass'])):
        if (sight_data['visible_passes']['visible_pass'][i]['country'] == country):
            if (sight_data['visible_passes']['visible_pass'][i]['region'] == region):
                region_info.append((sight_data['visible_passes']['visible_pass'][i]))

    return {region:region_info}


@app.route('/countries/<country>/regions/<region>/cities', methods=['GET'])
def cities(country: str, region: str) -> str:
    
    """
    Gives all of the cities within a specified region and country

    Args:
        country: string name of the country
        region: string name of the region

    Returns:
        cities: string of all of the cities

    """

    logging.info("getting cities in " + region + ", " + country)

    cities = ''

    for i in range(len(sight_data['visible_passes']['visible_pass'])):
        if (sight_data['visible_passes']['visible_pass'][i]['country'] == country):
            if sight_data['visible_passes']['visible_pass'][i]['region'] == region:
                if sight_data['visible_passes']['visible_pass'][i]['city'] not in cities:
                    cities += (sight_data['visible_passes']['visible_pass'][i]['city']) + "\n"

    return cities



@app.route('/countries/<country>/regions/<region>/cities/<city>', methods=['GET'])
def city_info(country: str, region: str, city: str) -> dict:

    """
    Returns all the data about a specific city from sighting data

    Args:
        country: string of country name selected
        region: string of region name selected
        city: string of city name selected

    Returns:
        city_info: A list of dictionaries of all info about the city (all sightings)

    """

    logging.info("getting city data for " + city + ", " + region + ", " + country)

    city_info = []

    for i in range(len(sight_data['visible_passes']['visible_pass'])):
        if (sight_data['visible_passes']['visible_pass'][i]['country'] == country):
            if (sight_data['visible_passes']['visible_pass'][i]['region'] == region):
                if (sight_data['visible_passes']['visible_pass'][i]['city'] == city):
                    city_info.append((sight_data['visible_passes']['visible_pass'][i]))

    return {city:city_info}


if __name__ == '__main__': 
    app.run(debug = True, host = '0.0.0.0')