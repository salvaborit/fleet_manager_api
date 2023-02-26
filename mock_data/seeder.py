#!/usr/bin/python3

import requests
import json
# url_vehicles = 'http://localhost:8000/vehicles/'
# url_drivers = 'http://localhost:8000/drivers/'
# file_vehicles = 'fleet_manager_vehicles.json'
# file_drivers = 'fleet_manager_drivers.json'

# print(f'\n\nVEHICLES')
# with open(file_vehicles, 'r') as file:
#     obj_list = json.load(file)
#     for item in obj_list:
#         resp = requests.post(url_vehicles, item)
#         print(f'{resp.status_code}')


# with open(file_drivers, 'r') as file:
#     obj_list = json.load(file)
#     for item in obj_list:
#         resp = requests.post(url_drivers, item)
#         print(f'{resp.status_code}')


print(f'\n\nDRIVER DOCS')
json_file = 'fleet_manager_driver_docs.json'
url = 'http://localhost:8000/driver-docs/'


with open(json_file, 'r') as file:
    obj_list = json.load(file)
    for item in obj_list:
        resp = requests.post(url, item)
        print(f'{resp.status_code}')


print(f'\n\VEHICLE DOCS')
json_file = 'fleet_manager_vehicle_docs.json'
url = 'http://localhost:8000/vehicle-docs/'


with open(json_file, 'r') as file:
    obj_list = json.load(file)
    for item in obj_list:
        resp = requests.post(url, item)
        print(f'{resp.status_code}')
