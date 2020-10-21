class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        if self.cell < other.cell:
            return 0
        else:
            return self.cell - other.cell

    def __mul__(self, other):
        return self.cell * other.cell

    def __floordiv__(self, other):
        division = self.cell // other.cell
        return division

    def make_order(self, number_of_cells):
        for el in range(self.cell):
            if el % number_of_cells == 0:
                print("")
            print("*", end=" ")

        return ""

cell1 = Cell(12)
cell2 = Cell(7)

print(cell1+cell2)
print(cell1-cell2)
print(cell1*cell2)
print(cell1//cell2)

print(cell1.make_order(3))
print(cell2.make_order(2))
