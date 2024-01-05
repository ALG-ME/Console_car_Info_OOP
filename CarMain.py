import datetime

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f'Марка: {self.make}, Модель: {self.model}, Год выпуска: {self.year}')

    def calculate_age(self, current_year):
        return current_year - self.year


# Создание объектов класса Car
car1 = Car('Toyota', 'Camry', 2018)
car2 = Car('Tesla', 'Model S', 2020)
car3 = Car('Ford', 'F-150', 2015)

# Вывод информации о каждом автомобиле
car1.display_info()
car2.display_info()
car3.display_info()

# Вычисление возраста каждого автомобиля
current_year = datetime.datetime.now().year
print(f"Возраст автомобиля 1: {car1.calculate_age(current_year)} лет")
print(f"Возраст автомобиля 2: {car2.calculate_age(current_year)} лет")
print(f"Возраст автомобиля 3: {car3.calculate_age(current_year)} лет")
