
#6

list3 = []


def int_func(text):
    text = text.split()
    for el in text:
        el = el.capitalize()
        list3.append(el)
    my_list = ' '.join(list3)
    return my_list


print(int_func(input("Введите ваш текст ")))



