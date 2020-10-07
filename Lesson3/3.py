
#1

def arguments(*args):
    return max(args)


var_1 = int(input("Число № 1 "))
var_2 = int(input("Число № 2 "))
var_3 = int(input("Число № 3 "))

print(arguments(var_1, var_2, var_3))

#print(arguments(1, 5, 7))