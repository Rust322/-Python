
#5

result = 0
set = 0

while True:
    string = input("Введите числа через пробел, для выхода введите 'Q' ").split()
    for i in string:
        if i == "Q" or i == "q":
            string.remove(i)
            set = 1

    result = + result
    for i in range(len(string)):
        result += int(string[i])
    if set == 1:
        print(result)
        break

    print(result)





