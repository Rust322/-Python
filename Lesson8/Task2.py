class MyException(Exception):

    def __init__(self, text):
        self.text = text


arg_one = float
arg_two = float

try:
    arg_one = float(input("Введите число 1 "))
    arg_two = float(input("Введите число 2 "))
except ValueError:
    print("Это не число(а)!")

try:
    if arg_two == 0:
        raise MyException("Делить на ноль нельзя!")
    result = arg_one / arg_two
except MyException as my_ex:
    print(my_ex)
except TypeError:
    print("Что-то пошло не так")
else:
    print(f"Результат деления = {result}")



