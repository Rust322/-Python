#4
number = int(input("Введите ваше число "))

frst = 0
biggest = 0

while True:
    if number > 10:
        frst = number % 10
        if frst > biggest:
            biggest = frst
        number //= 10
        continue
    elif number < 10:
        if number > biggest:
            biggest = number
        print(f"Самое большое число {biggest}")
        break

