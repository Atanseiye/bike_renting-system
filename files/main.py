# import the required liberaries
print('stated')
print('.\n.\n.\n.')
import random
import string
# from mongodb import MongoDB
import datetime
# from fastapi import FastAPI
from pymongo import MongoClient





# Create a client that connects to the mongodb server
client = MongoClient('mongodb://localhost:27017')

# Create a database witht the client instance class
db = client.Bike_company

# Create a collection in the database
bikesdb = db.bikes
customersdb = db.customers






# load the current date and time here
current_date_time = datetime.datetime.now()
print(current_date_time.date())

# create the bike class
class Bike:

    # this is the bike instance class which serves as the database
    # where all the availabe or registered bike are stored
    bike_instance = []

    # this method is used to generate bike id
    def Bike_id(length=6):
        character = string.ascii_letters + string.digits
        id = 'bike-' + ''.join(random.choice(character) for _ in range(length))
        return id

    # this method is used to generate time the bike was registered
    def date_time():
        current_date_time = datetime.datetime.now()
        return [current_date_time.date(), current_date_time.time()]
    
    # this method is used to create or register a new bike 
    def __init__(self, Bike_name):
        self.Bike_name = Bike_name
        

        # append all created bike to the bike instance above
        Bike.bike_instance.append(self)

    # this method has a decorator, it is used to reference the instances in the bike class
    @classmethod
    def in_bike(cls):
        # A method to get all the created bike instances
        if len(cls.bike_instance) == 0: # this checks if there's any bike in the database
            return 'No bike have been added'  # returns the string if there's none
        else:
            return cls.bike_instance # else, 

    # this method gets all the bike class in the bike instance class
    def all_bikes():
        all = []
        for bike_data in Bike.in_bike():
            vaules = {'Name': bike_data.Bike_name,
            'ID': Bike.Bike_id(), 
            'Condition': 'good', 
            'Rented': False,
            'Date': str(Bike.date_time()[0]),
            'Time': str(Bike.date_time()[1])
            }
            all.append(vaules)
        return all
                

    @classmethod
    def num_of_Bikes(cls):
       if len(cls.bike_instance) == 0:
           return 'There is no bike available'
       else:
           list = len(cls.bike_instance)
           return list



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Customer:

    customers_instance = []

    def customer_id(length=7):
        character = string.ascii_letters + string.digits
        id = 'customer-' + ''.join(random.choice(character) for _ in range(length))
        return id

    def date_time():
        current_date_time = datetime.datetime.now()
        return [current_date_time.date(), current_date_time.time()]
    
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin

        # add each registered customer to the customers' instance
        Customer.customers_instance.append(self)


    @classmethod
    def in_values(cls):
        if len(cls.customers_instance) == 0:
            return 'We don\'t have any customer yet'
        else:
            return cls.customers_instance


    def all_customer():
        all = []
        for customer_data in Customer.in_values():
            vaules = {
                'Name': customer_data.name,
            'ID': Customer.customer_id(), 
            'Origin': customer_data.origin,
            'Date': str(Customer.date_time()[0]),
            'Time': str(Customer.date_time()[1])
            }
            all.append(vaules)
        return all
        

    @classmethod
    def num_of_customers(cls):
        if len(cls.customers_instance) == 0:
            return 'There is no customer yet'
        else:
            return len(cls.customers_instance)



# Create a dummy values for the bike and the customers
ind_bikes = []
for i in range(2000):
    ind_bikes.append(Bike('Mountain'))

ind_customer  = []
for customers in range(200):
    ind_customer.append(Customer('Kolade', 'Ekiti'))

bikes = Bike.all_bikes()
customerss = Customer.all_customer()
writeBikes = bikes
writeCustomers = customerss
print(type(writeBikes), 'reached here')
print(type(writeCustomers), 'reached here')


# Populate the bike and customer database with the dummy variable 
bikesdb.insert_many(writeBikes)
customersdb.insert_many(writeCustomers)


print('Done')