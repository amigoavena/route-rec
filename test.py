import requests
from jproperties import Properties

configs = Properties()

with open('key.properties', 'rb') as config_file:
    configs.load(config_file)

url = 'https://maps.googleapis.com/maps/api/directions/json'

params = dict(
    origin='stockholm',
    destination='gothenburg',
    key=configs.get("MAPS_KEY")
)

resp = requests.get(url=url, params=params)
data = resp.json() # Check the JSON Response Content documentation below

#print(data)

for route in data['routes']:
	for leg in route['legs']:
		print(leg['distance']['text'])
		print(leg['duration']['text'])
		print(len(leg['steps']))
		for step in leg['steps']:
			print(step['start_location']['lat'])
			print(step['start_location']['lng'])
			print(step['travel_mode'])