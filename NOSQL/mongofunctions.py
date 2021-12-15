import pymongo


client = pymongo.MongoClient("mongodb://10.0.17.42:27017")
db_name = client["assistant"]
series_collection = db_name["series"]

def insert_document(name, phone, email, address):
    data = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    insert_res = series_collection.insert_one(data)
    return insert_res.inserted_id


def find_document(name, multiple = False):
    if multiple:
        results = series_collection.find({"name": name}, {"name":True, "phone":True, "email":True, "address":True, '_id': False})
        return[i for i in results]
    else:
        return series_collection.find_one({"name": name}, {"name":True, "phone":True, "email":True, "address":True, '_id': False})


def update_document(name, phone, email, address):
    return series_collection.update_one({"name": name}, {"$set": {"name":name, "phone":phone, "email": email, "address": address}})


def delete_document(name):
    return series_collection.delete_one({"name": name})

def select_all():
    results =  series_collection.find({}, { '_id': False })
    for i in results:
        print (f"{i}\n")


