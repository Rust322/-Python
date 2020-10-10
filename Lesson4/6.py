from itertools import count
from itertools import cycle

for el in count(1):
    if el > 14:
        break
    else:
        print(el)

it = 0

for el in cycle("abcdefghijklmnopqrstuvwxyz"):
    if it >= len("abcdefghijklmnopqrstuvwxyz")*2:
        break
    print(el+el)
    it += 1

