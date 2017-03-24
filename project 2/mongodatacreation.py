#Store data to mongo db.
import os,sys
from pymongo import MongoClient
#from mongodv import mongoclient
def get_db():
    
       # Function to return the db object.
    
    # 'localhost:27017'
    user = "joseph roshen"
    password = "cathY1234"
    host = "local"
    port = "192.168.13.13"
    database = "MongoClient"
    mongo_uri = "mongodb://"+user+":"+password+"@"+host+":"+port+"/"+database

    client = MongoClient(mongo_uri)
    db = client.invoice
    print 'hi...!'
    return db

def add_statement(data):
    
   # Module will insert statements to database.
    
    status = False
    try:
        db = get_db()
        db.statement.insert(data)
        status = True
    except Exception, exc:
        logger.error(exc)
        print 'hi..'
    return status

#def main():
    #pass

#if __name__ == '__main__':
   # get_db()