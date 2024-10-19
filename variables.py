from pymongo import MongoClient

connection_url = "mongodb+srv://root:my^7#kj@cluster0.9podb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_url)