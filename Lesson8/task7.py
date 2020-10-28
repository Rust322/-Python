class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        string = ""
        if self.b > 0:
            string = f"({self.a}+{self.b}i)"
        elif self.b < 0:
            string = f"({self.a}{self.b}i)"
        return string

    def __add__(self, other):
        string = ""
        if self.b+other.b > 0:
            string = f"({self.a + other.a}+{self.b + other.b}i)"
        elif self.b+other.b < 0:
            string = f"({self.a + other.a}{self.b + other.b}i)"
        return string

    def __mul__(self, other):
        mult = f"({self.a * other.a - self.b * other.b}+{self.b * other.a + self.a * other.b}i)"
        return mult


a = ComplexNumber(1, 2)
b = ComplexNumber(-2, 4)
d = ComplexNumber(-3, 6)

print(a*b)
print(a+b)
print(a+d)
print(a*d)

a = complex(1, 2)
b = complex(-2, 4)
d = complex(-3, 6)

print(a*b)
print(a+b)
print(a+d)
print(a*d)