import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("raspberrytest-9d922-firebase-adminsdk-8zzyt-a986bb6929.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://raspberrytest-9d922-default-rtdb.asia-southeast1.firebasedatabase.app/'
})
ref = db.reference('/mfrc')
print(ref.get())