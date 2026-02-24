# sandbox to playaround with classes

class Dog:
    """ A simple attempt to model a dog. """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"
    
    def sit(self):
        return f"{self.name} is sitting."
    
    def roll_over(self):
        return f"{self.name} rolled over!"


dog = Dog("Puppy", 5)

print(dog.name)
print(dog.age)
print(dog.bark())
print(dog.sit())
print(dog.roll_over())


class Car:
    """A simple attempt to model a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # optional attribute with default value

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}".title()

    def read_odometer(self):
        return f'{self.make} {self.model} has {self.odometer_reading} miles on it.'
    
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value. 
        Reject the change if it attempts to roll back the odometer."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            raise ValueError("You can't roll back an odometer!")
        
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles < 0:
            raise ValueError("You can't increment the odometer with negative miles!")
        self.odometer_reading += miles
    
car = Car("Toyota", "Corolla", 2020)
print(car.get_descriptive_name())
print(car.read_odometer())

car.odometer_reading = 15000
print(car.read_odometer())

car.update_odometer(20000)
print(car.read_odometer())

#car.update_odometer(10000)  # This should raise an error

car.increment_odometer(500)
print(car.read_odometer())

 # Inheritance

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery_size = 75  # default battery size in kWh

    def describe_battery(self):
        return f"This car has a {self.battery_size}-kWh battery."

    def get_descriptive_name(self):
        return f"{super().get_descriptive_name()} (Electric)".title()


my_tesla = ElectricCar("Tesla", "Model S", 2025)
print(my_tesla.get_descriptive_name())
print(my_tesla.describe_battery())

#Compositoin
class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        return f"This car has a {self.battery_size}-kWh battery."

class ElectricCarWithBattery(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()  # composition: ElectricCar has a Battery

be6_xuv = ElectricCarWithBattery("Mahindara", "BE6", 2025)
print(be6_xuv.get_descriptive_name())
print(be6_xuv.battery.describe_battery())   