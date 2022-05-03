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
    commands += "\n/countries/<country>/regions/<region>/city - (GET) All information about a specific City in the sighting data"

    return commands


@app.route('/load_data', methods = ['POST'])
def load_data():
    
    """
    Reads in XML data files as global dicts

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

    return 'Data loading is complete.\n'



if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')