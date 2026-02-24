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