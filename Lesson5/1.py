import os

# os.remove("task_1.txt")
# чтобы каждое изменение не удалять вручную файл

try:
    with open("task_1.txt", "x") as task_one:
        while True:
            line = input("Введите ваш текст ")
            task_one.writelines(line + "\n")
            if not line:
                break
except FileExistsError:
    print("Файл уже существует")


with open("task_1.txt", "r") as task_one:
    print(task_one.read())

