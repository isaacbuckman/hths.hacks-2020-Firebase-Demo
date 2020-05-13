from firebase import firebase
import math

firebase = firebase.FirebaseApplication("https://test-ddf2c.firebaseio.com/", None)

people = firebase.get('people', None)

currentlat = input("Current Latitude: ")
currentlong = input("Current Longitude: ")

if people is not None:
	for p in people.values():
		distance = math.sqrt((currentlat - float(p['lat']))**2 + (currentlong - float(p['long']))**2)
		print("You are {distance} degress from {name}.".format(distance = distance, name = p['name']))