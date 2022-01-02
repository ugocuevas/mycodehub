

class Car:
    def __init__(self, brand, model, colour, max_speed):
        self.brand = brand
        self.model = model
        self.colour = colour
        self.max_speed = max_speed
        self.transmission = 'Automatic' #adding a default parameter to the class
    
    def check_transmission_type(self):
        print(f"This {self.colour} {self.brand} car has {self.transmission} gear system")
    
    def car_details(self):
        print(f'''This car is a {self.colour} {self.brand} {self.model} with a maximum speed of {self.max_speed} km/h''')
        
    def change_transmission_type(self, transmission): 
        """Modifying an attribute value using a method"""
        if transmission == 'Manual':
            print(f"You have chosen the {transmission} transmission gear")
            self.transmission = 'Manual'
        else:
            print(f"You have chosen the {transmission} transmission gear system")
            self.transmission = 'Automatic'
        
# my_car = Car('Lexus', 'RX450', 'Silver', 240)
# my_car.check_transmission_type()
# my_car.change_transmission_type('Manual')
# my_car.check_transmission_type()

#Inheritance
#Super classes and subclasses
#Super classes are basically parents of subclasses
#Subclasses are children of superclasses

class Suv(Car):
    def __init__(self, brand, model, colour, max_speed):
        """Initialize all the parent attributes"""
        super().__init__(brand, model, colour, max_speed) #Enables you to call the class methods
  
my_suv = Suv('Benz', 'GL230', 'Black', 280)
my_suv.car_details()      
        