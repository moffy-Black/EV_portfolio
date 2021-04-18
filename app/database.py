import pyrebase
import json, os

with open(("/usr/src/app/firebaseConfig.json")) as f:
    firebaseConfig = json.loads(f.read())
firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()
db = firebase.database()