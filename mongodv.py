import os,sys
import pymongo
from pymongo import MongoClient
import datetime

def mongoclient(data, filename):
    status = False
    try:
        
        client=MongoClient()
        client =MongoClient('mongodb://localhost:27017/IMAGETOTEXT')
        db = client.IMAGETOTEXT
    #post = {"heading": "Optical Character Recognition ",
         # "done by": "joseph roshen",
          #"tags": ["mongodb", "python", "tesserect","pymongo"],
          #"date": datetime.datetime.utcnow()}
        post={"imgString" : data,"fileName" : filename}

        db.Text_Speech.insert(post)
        status = True
    except Exception, exc:
        print exc
    return status
