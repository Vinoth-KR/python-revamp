from cars import Car

car = Car("Honda", "Civic", 2019)
print(car.get_descriptive_name())
print(car.read_odometer())
car.update_odometer(25000)
print(car.read_odometer())