class MyException(Exception):

    def __init__(self, text):
        self.text = text


numbers_list = []
string = ""
spy_count = 0

while True:
    string = input("Введите ваше число либо несколько чисел через пробел ")
    if string == "stop":
        break
    try:
        if " " in string:
            for el in string.split():
                if el.isnumeric():
                    numbers_list.append(int(el))
                else:
                    spy_count += 1
                    print(f"Здесь есть шпион в колиестве {spy_count}!")
        elif not string.isnumeric():
            raise MyException("Это не число!")
        else:
            numbers_list.append(int(string))
    except MyException as my_ex:
        print(my_ex)

print(numbers_list)



