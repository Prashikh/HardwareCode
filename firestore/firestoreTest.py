import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import os

path = os.getcwd()
#initialize SDK
cred = credentials.Certificate("/home/pi/Desktop/firestore/parkingappkeys.json")
#cerfificate/home/pi/Desktop/
firebase_admin.initialize_app(cred)
#initialize isntance of firestore
firestore_db = firestore.client()

now = datetime.now()
now = now.strftime("%m/%d/%Y, %H:%M:%S")
datfile = open('/home/pi/Desktop/tempdata.txt', 'r')
readnumber = datfile.read()
datfile.close()
print ("counter from text file:" + str(readnumber))
firestore_db.collection(u'Parking Decks').document(u'Demo').update({'openSpots':int(readnumber), 'TimeUpdated': now})