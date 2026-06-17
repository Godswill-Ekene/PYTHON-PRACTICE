
class Car:

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def introduce(self):
        print(f"This is a {self.brand} car from the year {self.year}")

toyota = Car("Toyota", 2020)

toyota.introduce()