
# 6

a = 7
b = 1

iteration = 1
print(f"День номер 1, дистанция {b} км")
while b < a:
    iteration += 1
    b *= 1.1
    b = float('{:.3f}'.format(b))
    print(f"День номер {iteration}, дистанция {b} км")

print(f"Спортсмен достигнет результата не менее {a} км на {iteration}-й день")



