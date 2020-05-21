class Car:
    user_input_model = 'Corvette'
    number_of_cars = 0

    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

        Car.number_of_cars += 1

    def change_model(self):
        self.model = self.user_input_model

    @classmethod
    def inital_number_of_cars(cls, number_of_cars):
        cls.number_of_cars = number_of_cars

Car.inital_number_of_cars(8)
car1 = Car('Chevrolet', 'Camaro', '2010', 10000)
car2 = Car('Kia', 'Rio', '2018', 80000)
car3 = Car('Volkwagen', 'Bora', '2008', 50000)
print(car1.__dict__)
car1.change_model()
print(car1.__dict__)
print(Car.number_of_cars)


