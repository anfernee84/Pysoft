from pymongo import MongoClient

myclient = MongoClient("mongodb://10.0.17.42:27017")

db_name = "assistant"
dblist = myclient.list_database_names()

if db_name not in dblist:
