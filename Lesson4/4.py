import random

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 12]

my_list2 = [el for el in my_list if my_list.count(el) <= 1]

print(my_list2)

"""-----------------------------------------------------"""
my_list4 = [random.randint(0, 124) for el in range(0, 20)]

my_list3 = [el for el in my_list4 if my_list4.count(el) <= 1]

print(my_list4)
print(my_list3)