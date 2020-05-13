import firebase_admin
from firebase_admin import credentials, db
from ipdb import launch_ipdb_on_exception
import math

with launch_ipdb_on_exception():
	cred = credentials.Certificate("test-ddf2c-firebase-adminsdk-5tva7-6b546e57b4.json")
	firebase_admin.initialize_app(cred, {
	    'databaseURL' : 'https://test-ddf2c.firebaseio.com/'
	})

	root = db.reference()

	new_person = {}
	new_person['name'] = input("name: ")
	new_person['lat'] = float(input("Latitude: "))
	new_person['long'] = float(input("Longitude: "))
	
	people = db.reference('people').get()

	if people is not None:
		for p in people.values():
			distance = math.sqrt((new_person['lat'] - float(p['lat']))**2 + (new_person['long'] - float(p['long']))**2)
			print("You are {distance} degress from {name}.".format(distance = distance, name = p['name']))
	
	root.child('people').push(new_person)