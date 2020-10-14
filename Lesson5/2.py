count = 1

my_list = []

with open("task_2.txt", "r") as task_two:
    for el in task_two:
        print(f"Количество слов в строке № {count} = ", len(el.split()))
        count += 1
        my_list.append(el)

print("Количество строк в файле = ", len(my_list))