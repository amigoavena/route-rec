import requests
from jproperties import Properties

configs = Properties()

with open('key.properties', 'rb') as config_file:
    configs.load(config_file)

url = 'https://maps.googleapis.com/maps/api/directions/json'

nearby = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'

place_det = 'https://maps.googleapis.com/maps/api/place/details/json'

params = dict(
    origin='stockholm',
    destination='gothenburg',
    key=configs.get("MAPS_KEY")
)

resp = requests.get(url=url, params=params)
data = resp.json() # Check the JSON Response Content documentation below

#print(data)

listPlaces = []

f = open("route.txt","w")

for route in data['routes']:
	for leg in route['legs']:
		print(leg['distance']['text'])
		print(leg['duration']['text'])
		print(len(leg['steps']))
		for step in leg['steps']:
			params = dict(
				location='%s,%s'%(step['start_location']['lat'],step['start_location']['lng']),
				radius=50,
				key=configs.get("MAPS_KEY")
			)
			f.write('%s,%s\n'%(step['start_location']['lat'],step['start_location']['lng']))
			nearResp = requests.get(url=nearby, params=params)
			nearRespData = nearResp.json() # Check the JSON Response Content documentation below
			for place in nearRespData['results']:
				try:
					""
					#print(place['next_page_token'])
				except:
					""
					#print("only one page")
				listPlaces.append(place['place_id'])

f.close()

f1 = open("places.txt","w")

uniquePlaces = set(listPlaces)
print(len(uniquePlaces))

for placeid in uniquePlaces:
	f1.write('%s\n'%(placeid))
	params = dict(
		place_id='%s'%(placeid),
		key=configs.get("MAPS_KEY")
	)
	#placeResp = requests.get(url=place_det, params=params)
	#placeRespData = placeResp.json() # Check the JSON Response Content documentation below
	#print(",".join(placeRespData['types']))