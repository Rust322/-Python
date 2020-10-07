
#1

def my_func(x, y):
    x = x ** y
    return x


print(my_func(2, 5))
#-------------------------


def my_func(x, y):
    for i in range(y):
        if i == 0:
            result = 1
        result = result * x
    return result


print(my_func(10, 4))