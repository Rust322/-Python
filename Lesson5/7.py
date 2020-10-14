import json

firms_left_side = {}
profit_list = []
firms_right_side = {}
summa = 0
i = 0

with open("text_7.txt", "r", encoding='UTF-8') as data:
    for el in data:
        key, value, value2, value3 = el.split()
        firms_left_side[key] = int(value2) - int(value3)
        if int(value2) - int(value3) > 0:
            profit_list.append(int(value2) - int(value3))


while i < len(profit_list):
    summa = summa + profit_list[i]
    i += 1
    if i == len(profit_list):
        average = summa / i
        firms_right_side["average_profit"] = average


result_list = []
result_list.append(firms_left_side)
result_list.append(firms_right_side)

print(result_list)

with open("my_file.json", "w", encoding='UTF-8') as json_file:
    json.dump(result_list, json_file, ensure_ascii=False)

