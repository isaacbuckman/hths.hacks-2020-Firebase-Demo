from firebase import firebase

firebase = firebase.FirebaseApplication("https://test-ddf2c.firebaseio.com/", None)

name1 = "HTHS"
currentlat = float(input("Current Latitude: "))
currentlong = float(input("Current Longitude: "))

data = {
    'name':name1,
    'lat':currentlat,
    'long':currentlong
}

post = firebase.post('people', data)