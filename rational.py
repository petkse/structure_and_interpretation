from math import gcd

# Класс для представления рациональных чисел
class Rational:
    def __init__(self, numerator, denominator):
        # Вычисляем наибольший общий делитель (НОД) числителя и знаменателя
        common_divisor = gcd(numerator, denominator)
        # Сокращаем числитель и знаменатель на НОД
        self.numerator = numerator // common_divisor
        self.denominator = denominator // common_divisor

    # Метод для строкового представления рационального числа
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    # Метод для перегрузки оператора сложения
    def __add__(self, other):
        # Вычисляем новый числитель и знаменатель для суммы
        new_numerator = (self.numerator * other.denominator + other.numerator * self.denominator)
        new_denominator = (self.denominator * other.denominator)
        # Возвращаем новый объект Rational
        return Rational(new_numerator, new_denominator)

# Создаем два рациональных числа
x = Rational(3, 5)
y = Rational(1, 4)

sum_result = x + y

print(f"Сумма чисел {x} и {y} равна {sum_result}")
