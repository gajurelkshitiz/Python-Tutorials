from car import Car

Car1 = Car("Tesla", 2023, "grey", True)
Car2 = Car("BMW", 2020, "red", False)
Car3 = Car("Maruti", 2022, "blue", True)
car4 = Car("Mustang", 2023, "white", True)

print(Car2.model)
print(Car2.color)
print(Car2.year)
print(Car2.for_sale)

Car2.drive()

Car3.stop()

Car1.describe()