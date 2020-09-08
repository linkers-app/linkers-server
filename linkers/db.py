import pymongo as mongo

MONGO_URI = "mongodb://localhost:27017/linkers"
client = mongo.MongoClient(MONGO_URI)
db = client.linkers
