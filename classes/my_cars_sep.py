from cars import Car
from electric_car_sep import ElectricCar as EC

my_dream_car = Car('Audi', 'Q5', 2019)
print(my_dream_car.get_descriptive_name())

my_tesla = EC('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
