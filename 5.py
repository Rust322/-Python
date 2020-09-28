
# 5

proceeds = int(input("Введите выручку "))
costs = int(input("Введите расходы "))

result = proceeds - costs

if result >= 0:
    print(f"Прибыль составила {result}")
    profit = result / proceeds * 100
    print(f"Рентабельность = {profit}%")
    staff = int(input("Введите количество сотрудников "))
    print(f"Прибыль на одного сотрудника составила {result / staff}")

else:
    print(f"Убыток составил {result}")
    profit = result / proceeds * 100
    print(f"Рентабельность = {profit}%")
    staff = int(input("Введите количество сотрудников "))
    print(f"Убыток на одного сотрудника составила {result / staff}")



