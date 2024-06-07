import time
import sys

# Класс Чайник
class Kettle:
    def __init__(self):
        self.is_full = False  # Чайник пустой
        self.is_boiled = False  # Вода не кипяченая

# Класс Кран
class Faucet:
    def __init__(self):
        self.is_open = False  # Кран закрыт

    def open(self):
        # Открытие крана
        if not self.is_open:
            self.is_open = True
            print("Кран открыт")
        else:
            print("Кран уже открыт")

    def close(self):
        # Закрытие крана
        if self.is_open:
            self.is_open = False
            print("Кран закрыт")
        else:
            print("Кран уже закрыт")

    def fill(self, kettle):
        # Наполнение чайника водой
        if self.is_open:
            print("Наполняем")
            for i in range(1, 11):
                print(f"Почти готово - {i * 10}%")
                time.sleep(1)
            kettle.is_full = True  # Чайник наполнен
            print("Готово")
        else:
            print("Не удалось наполнить чайник, кран закрыт")

    def empty(self, kettle):
        # Опустошение чайника
        kettle.is_full = False
        print("Чайник пустой")

# Класс Спички
class Match:
    def __init__(self):
        self.is_lit = False  # Спичка не горит

    def light(self):
        # Зажжение спички
        if not self.is_lit:
            self.is_lit = True
            print("Спичка зажглась")
        else:
            print("Спичка уже горит")

    def put_out(self):
        # Потушение спички
        if self.is_lit:
            self.is_lit = False
            print("Спичка потухла")
        else:
            print("Спичка уже не горит")

# Класс плита
class Stove:
    def __init__(self):
        self.is_burning = False  # Плита не горит

    def light_stove(self, match):
        # Зажжение плиты
        if match.is_lit:
            self.is_burning = True
            print("Плита работает")
        else:
            print("Не удалось зажечь плиту, спичка не горит")

    def off_stove(self):
        # Выключение плиты
        if self.is_burning:
            self.is_burning = False
            print("Плита потухла")
        else:
            print("Плита уже не горит")

    def heat_kettle(self, kettle):
        # Кипячение воды в чайнике
        if kettle.is_full:
            print("Кипятим...")
            for i in range(1, 11):
                print(f"Почти готово - {i * 10}%")
                time.sleep(2)
            kettle.is_boiled = True  # Вода закипела
            print("Кипит!!!")
        else:
            print("Нет воды в чайнике")
            print("Аааа, горим!!!")
            sys.exit(0)

# Функция меню для выбора действий
def menu():
    kettle = Kettle()
    faucet = Faucet()
    match = Match()
    stove = Stove()

    while True:
        print("\nМеню:")
        print("1. Открыть кран")
        print("2. Закрыть кран")
        print("3. Наполнить чайник")
        print("4. Вылить чайник")
        print("5. Зажечь спичку")
        print("6. Потушить спичку")
        print("7. Зажечь газовую плиту")
        print("8. Выключить газовую плиту")
        print("9. Кипятить чайник")
        print("0. Выйти")

        choice = input("Выберите действие: ")

        # Обработка выбора пользователя
        if choice == "1":
            faucet.open()
        elif choice == "2":
            faucet.close()
        elif choice == "3":
            faucet.fill(kettle)
        elif choice == "4":
            faucet.empty(kettle)
        elif choice == "5":
            match.light()
        elif choice == "6":
            match.put_out()
        elif choice == "7":
            stove.light_stove(match)
        elif choice == "8":
            stove.off_stove()
        elif choice == "9":
            stove.heat_kettle(kettle)
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

# Запуск программы
if __name__ == "__main__":
    menu()
