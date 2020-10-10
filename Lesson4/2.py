import random

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 124]

my_list3 = [my_list[el] for el in range(len(my_list)) if my_list[el] > my_list[el-1] and el != 0]

print(my_list3)

"""------------------------"""

my_list4 = [random.randint(0, 124) for el in range(0, 20)]

my_list5 = [my_list4[el] for el in range(len(my_list4)) if my_list4[el] > my_list4[el-1] and el != 0]

print("Сгенерированный список: ", my_list4)
print("Итог", my_list5)
