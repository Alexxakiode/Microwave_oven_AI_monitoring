#Importing MongoClient 
from pymongo import MongoClient

#Creating client variable on MongoDB
client = MongoClient("mongodb+srv://alexanderakiode:Greats11@cluster0.qcurgqp.mongodb.net/?retryWrites=true&w=majority")

#Creating the database called Real_estate on MongoDB
db = client['Real_estate']

#Creating the collection called Real_estate_collection on MongoDB
collection = db["Real_estate_collection"]

