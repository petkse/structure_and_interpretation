class Point:
    # Конструктор инициализирует объект P
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Метод для сложения двух объектов. Возвращает новый объект.
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Метод для вывода
    def display(self):
        print(f"x: {self.x}, y: {self.y}")

if __name__ == "__main__":

    p1 = Point(3, 4)
    p2 = Point(1, 2)
    p3 = p1 + p2


    p1.display()
    p2.display()
    p3.display()
