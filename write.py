import firebase_admin
from firebase_admin import credentials, db
import math

cred = credentials.Certificate("test-ddf2c-firebase-adminsdk-5tva7-6b546e57b4.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://test-ddf2c.firebaseio.com/'
})

root = db.reference()

new_person = {}
new_person['name'] = input("name: ")
new_person['lat'] = float(input("Latitude: "))
new_person['long'] = float(input("Longitude: "))

root.child('people').push(new_person)