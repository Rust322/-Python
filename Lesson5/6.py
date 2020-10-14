import re

curriculum = {}


def get_number(number):
    number = re.findall(r"\d+", number)
    return number


with open("text_6.txt", "r", encoding='UTF-8') as data:
    for el in data:
        key, value, value2, value3 = el.split()
        value = get_number(value)
        value2 = get_number(value2)
        value3 = get_number(value3)
        result_value = [int(el) for el in value]
        result_value2 = [int(el) for el in value2]
        result_value3 = [int(el) for el in value3]
        curriculum[key] = sum(result_value)+sum(result_value2)+sum(result_value3)


print(curriculum)
