
# 3

number = int(input("Put your number here "))

number2 = int("%d%d" % (number, number))

number3 = int("%d%d%d" % (number, number, number))

result = number + number2 + number3

print("Результат: %d + %d + %d = %d" % (number, number2, number3, result))

