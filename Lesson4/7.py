
def fact(n):
    fact_r = 1
    for s in range(1, n+1):
        fact_r = fact_r*s
        yield fact_r


for el in fact(93):
    print(el)

