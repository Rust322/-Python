
duct = {}

salary_list = []

with open("text_3.txt", encoding='UTF-8') as data:
    for line in data:
        key, value = line.split()
        duct[key] = value
        if float(value) < 20000.0:
            print(key, " получает зарплату менее 20000")
        salary_list.append(value)

salary_sum = 0.0

for el in salary_list:
    salary_sum += float(el)

average_salary = salary_sum / len(salary_list)

print("Средняя зарплата составляет:", average_salary)