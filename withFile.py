import requests
from jproperties import Properties

configs = Properties()

with open('key.properties', 'rb') as config_file:
    configs.load(config_file)

place_det = 'https://maps.googleapis.com/maps/api/place/details/json'

file1 = open('places.txt', 'r')
uniquePlaces = file1.readlines()

f1 = open("placesFull.txt","w")

for placeid in uniquePlaces:
	params = dict(
		place_id=placeid.strip(),
		key=configs.get("MAPS_KEY")
	)
	placeResp = requests.get(url=place_det, params=params)
	print()

	placeRespData = placeResp.json()['result'] # Check the JSON Response Content documentation below
	print(",".join(placeRespData['types']))

	row = "%s,%s,%s" %(placeRespData['place_id'],placeRespData['url'],'#'.join(placeRespData['types']))

	f1.write('%s\n'%(row))