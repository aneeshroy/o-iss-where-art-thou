import pytest
from app import *

load_data()

def test_help():
    assert isinstance(help(), str) == True

def test_load_data():
    assert isinstance(load_data(), str) == True

def test_epochs():
    assert isinstance(epochs(), str) == True

def test_epoch_info():
    assert isinstance(epoch_info("2022-042T12:04:00.000Z"), dict) == True

def test_countries():
    assert isinstance(countries(), str) == True

def test_country_info():
    assert isinstance(country_info("United_States"), list) == True

def test_regions():
    assert isinstance(regions("United_States"), str) == True

def test_region_info():
    assert isinstance(region_info("United_States", "Iowa"), list) == True

def test_cities():
    assert isinstance(cities("United_States", "Iowa"), str) == True

def test_city_info():
    assert isinstance(city_info("United_States", "Iowa", "Decorah"), list) == True