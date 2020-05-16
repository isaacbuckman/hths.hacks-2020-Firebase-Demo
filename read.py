import firebase_admin
from firebase_admin import credentials, db
import math

cred = credentials.Certificate("test-ddf2c-firebase-adminsdk-5tva7-6b546e57b4.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://test-ddf2c.firebaseio.com/'
})

root = db.reference()

lat = float(input("Enter Lat: "))
longi = float(input("Enter Long: "))

people = db.reference('people').get()

if people is not None:
	for p in people.values():
		distance = math.sqrt((lat - float(p['lat']))**2 + (longi - float(p['long']))**2)
		print("You are {distance} degress from {name}.".format(distance = distance, name = p['name']))