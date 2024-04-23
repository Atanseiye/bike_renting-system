print('stated')
print('.\n.\n.\n.')
from pymongo import MongoClient

# Create a client that connects to the mongodb server
client = MongoClient('mongodb://localhost:27017')

# Create a database witht the client instance class
db = client.Bike_company

# Create a collection in the database
bikes = db.bikes
customers = db.customers

print('done')