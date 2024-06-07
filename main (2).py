class transport:
    def start(self):
        pass  # Заглушка для метода запуска транспортного средства.

    def stop(self):
        pass  # Заглушка для метода остановки транспортного средства.


class Car(transport):
    def __init__(self, mark):
        self.mark = mark

    def start(self):
        print(f"Запуск автомобиля {self.mark}")  
    def stop(self):
        print(f"Остановка автомобиля {self.mark}")  


class Motorcycle(transport):
    def __init__(self, mark):
        self.mark = mark

    def start(self):
        print(f"Запуск мотоцикла {self.mark}") 

    def stop(self):
        print(f"Остановка мотоцикла {self.mark}") 

if __name__ == "__main__":

    car = Car("Fiat Doblo")
    motorcycle = Motorcycle("Harley")

    # Запуск и остановка автомобиля 
    car.start()
    car.stop()
    # Запуск и остановка мотоцикла
    motorcycle.start()
    motorcycle.stop()
