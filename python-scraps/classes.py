'''class it out'''

class Car():
    def __init__(self, name, manufacturer):
        self.name = name
        self.manufacturer = manufacturer


    def get_details(self):
        print('car name is ' + self.name + ' and manufacturer is ' + self.manufacturer)


my_car = Car('mustang', 'ford')
my_car.get_details()

class Electric(Car):
    def __init__(self, name, manufacturer, batt_power):
        super().__init__(name, manufacturer)
        self.batt_power = batt_power


    def get_details(self):
        print('car name is ' + self.name + ' and manufacturer is ' + self.manufacturer + ' batt power is ' + str(self.batt_power))

my_electric_car = Electric('mustang', 'ford', 70)
my_electric_car.get_details()


''' want to keep track of the order in which key-value pairs
are added, you can use the OrderedDict class from the collections module'''
from collections import OrderedDict

my_collection = OrderedDict()
my_collection['jen'] = 'python'
my_collection['sarah'] = 'c'
my_collection['edward'] = 'ruby'
my_collection['phil'] = 'python'

for name, language in my_collection.items():
 print(name.title() + "'s favorite language is " +
 language.title() + ".")