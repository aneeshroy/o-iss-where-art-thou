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
def help():
    """
    Gives all routes available in this app for ISS data

    Returns:
        A String of all commands that can be used
    """

    logging.info("all commands printed")

    commands = "/help - (GET) Information on how to interact with the application"
    commands += "\n/load_data - (POST) load data (XML) into app"
    commands += "\n/epoch - (GET) All Epochs in the positional data"
    commands += "\n/epoch/<epoch> - (GET) All information about a specific Epoch in the positional data" 
    commands += "\n/countries - (GET) All Countries from the sighting data"
    commands += "\n/countries/<country> - (GET) All information about a specific Country in the sighting data"
    commands += "\n/countries/<country>/regions - (GET) All Regions associated with a given Country in the sighting data"
    commands += "\n/countries/<country>/regions/<region> - (GET) All information about a specific Region in the sighting data"
    commands += "\n/countries/<country>/regions/<region>/cities - (GET) All Cities associated with a given Country and Region in the sighting data"
    commands += "\n/countries/<country>/regions/<region>/cities/<city> - (GET) All information about a specific City in the sighting data"

    return commands


@app.route('/load_data', methods = ['POST'])
def load_data():
    
    """
    Reads in XML data files as global dicts

    Args:
        None

    Returns:
        A string indicating the loading is successful.
    
    """

    global pos_data
    global sight_data

    logging.info('loading data\n')

    with open('ISS.OEM_J2K_EPH.xml','r') as pos:
        pos_data = xmltodict.parse(pos.read())

    with open('XMLsightingData_citiesUSA04.xml', 'r') as sight:
        sight_data = xmltodict.parse(sight.read())

    return 'Data loaded into application.\n'

@app.route('/epochs', methods=['GET'])
def epochs():
    """
    Takes all of the epochs from the positional data and displays as a string

    Args:
        None
    
    Returns:
        epochs: String containing all epochs
    
    """

    logging.info("getting epochs")

    epochs = ''

    for i in range(len(pos_data['ndm']['oem']['body']['segment']['data']['stateVector'])):
        epochs += (str(pos_data['ndm']['oem']['body']['segment']['data']['stateVector'][i]['EPOCH']) + '\n')

    return epochs


@app.route('/epochs/<epochs>', methods=['GET'])
def epoch_info():

    """
    Finds the epoch given and returns all information about the specific epoch.

    Args:
        epoch: String of epoch name selected

    Returns:
        epoch_data: 
    
    """

@app.route('/countries', methods=['GET'])
def countries():

@app.route('/countries/<countries>', methods=['GET'])
def country_info():

@app.route('/countries/<country>/regions', methods=['GET'])
def regions():

@app.route('/countries/<country>/regions/<region>', methods=['GET'])
def region_info():

@app.route('/countries/<country>/regions/<region>/cities', methods=['GET'])
def cities():

@app.route('/countries/<country>/regions/<region>/cities/<city>', methods=['GET'])
def city_info():

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')