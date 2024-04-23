import random
import string
import datetime
from pydantic import BaseModel


# load the current date and time here
current_date_time = datetime.datetime.now()
current_date_time.time()


# --------------------------------------------------------

class Bike(BaseModel):

    bike_instance = []

    
    def Bike_id(length=6):
        character = string.ascii_letters + string.digits
        id = 'bike-' + ''.join(random.choice(character) for _ in range(length))
        return id
    
    def __init__(self, Bike_name, 
                 Bike_id, condition, 
                 is_rented=False, 
                 date_time=current_date_time, ):
        self.Bike_name = Bike_name
        self.Bike_id = Bike.Bike_id()
        self.condition = condition
        self.is_rented = False
        self.date_time = current_date_time

        # append all  created bike instance
        Bike.bike_instance.append(self)

    @classmethod
    def in_bike(cls):
        # A method to get all the created bike instances
        if len(cls.bike_instance) == 0:
            return 'No bike have been added'
        else:
            return cls.bike_instance

    def all_bikes():
        all = []
        for bike_data in Bike.in_bike():
            vaules = {'Name': bike_data.Bike_name,
            'ID': bike_data.Bike_id, 
            'Condition': bike_data.condition, 
            'Rented': bike_data.is_rented}
            all.append(vaules)
        return all
                

    @classmethod
    def num_of_Bikes(cls):
       if len(cls.bike_instance) == 0:
           return 'There is no bike available'
       else:
           list = len(cls.bike_instance)
           return list


ind_bikes = []
for i in range(9):
    ind_bikes.append(Bike('Mountain', Bike.Bike_id(), 'good',False))


bikes = Bike.all_bikes()
bikes


# --------------------------------------------------------------

class Customer:

    customers_instance = []

    def customer_id(length=7):
        character = string.ascii_letters + string.digits
        id = 'customer-' + ''.join(random.choice(character) for _ in range(length))
        return id
    
    def __init__(self, name, id, origin, date_time=current_date_time):
        self.name = name
        self.id = id
        self.origin = origin
        self.date_time = current_date_time

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
            vaules = {'Name': customer_data.name,
            'ID': customer_data.id, 
            'Origin': customer_data.origin, 
            }
            all.append(vaules)
        return all
        

    @classmethod
    def num_of_customers(cls):
        if len(cls.customers_instance) == 0:
            return 'There is no customer yet'
        else:
            return len(cls.customers_instance)


ind_customer  = []
for customers in range(10):
    ind_customer.append(Customer('Kolade', Customer.customer_id(), 'Ekiti'))


customers = Customer.all_customer()


# ------------------------------------------------------------------------


class rent_bike:
    @staticmethod
    def get_customers_id(id):
        return id

    @staticmethod
    def check_customer_status(value):
        # Assuming there is a class called Customer with a method all_customer()
        # that returns a list of customer data
        customer_list = Customer.all_customer()
        key = 'ID'
        for d in customer_list:
            if key in d and d[key] == value:
                return True
        return "We can't find your record."

    @staticmethod
    def get_bike(verify):
        # You need to call the check_customer_status method and pass the 
        # 'verify' parameter
        verified = rent_bike.check_customer_status(verify)
        # print(verified)
        if verified:
            # Perform actions if the customer is verified
            customer_list = Customer.all_customer()
            key = 'ID'
            for d in customer_list:
                if key in d and d[key] == verify:
                    bike = bikes.pop() # remove the last bike and save it in the
                                       # bike
                    bike_granted = [d, bike]  # save the customer and the bike in a 
                                              # list called bike_granted
                    bike_granted[1]['Rented'] = True # change the is_rented to True
                    bikes.append(bike) # save back the bike in a bikes
                    return bike_granted # return the bike given to the user and the 
                                        # user in a list called bike_granted
        else:
            # Handle the case when the customer is not found
            return "Customer not found."

# Example usage:
# customer_id = 'customer-7myo6uN'
# result = rent_bike.check_customer_status(customer_id)
get = rent_bike.get_bike('customer-Tqt70cC')
print(get)
