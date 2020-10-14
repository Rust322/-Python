import os

words = []

with open("text_4.txt") as data:
    for line in data:
        line = line.replace("One", "Один")
        line = line.replace("Two", "Два")
        line = line.replace("Three", "Три")
        line = line.replace("Four", "Четыре")
        words.append(line)

try:
    with open("text_4_result.txt", "x") as outcome:
        outcome.writelines(words)
except FileExistsError:
    print("Файл уже существует")



