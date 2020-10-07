
#1

def division():
    var_1 = input("Число номер 1 ")
    var_2 = input("Число номер 2 ")
    while True:
        if var_1.isdigit() and var_2.isdigit():
            break
        else:
            var_1 = input("ЧИСЛО номер 1 ")
            var_2 = input("ЧИСЛО номер 2 ")

    var_1 = int(var_1)
    var_2 = int(var_2)
    return var_1/var_2


var_3 = division()
print(var_3)