class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model},Year: {self.year}")


car1 = Car("HONDA", "Honda Accord EX Sedan", 2018)
car2 = Car("FORD", "Fisker Ocean Ultra SUV ", 2023)

print("Car 1:")
car1.display_info()
print("Car 2:")
car2.display_info()
