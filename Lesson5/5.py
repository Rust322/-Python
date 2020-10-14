import os

try:
    os.remove("numbers.txt")
except FileNotFoundError:
    print("Файл пока не создан, идем дальше ->")


with open("numbers.txt", "x") as data:
    def loop():
        numbers = input("Введите численный ряд ")
        data.write(numbers)
        numbers = numbers.split()
        summa = 0
        for el in numbers:
            try:
                summa = summa + int(el)
            except ValueError:
                print("Это не численный ряд ")
                break
        return summa

    print(loop())



