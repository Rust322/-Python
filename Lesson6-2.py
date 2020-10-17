class Road:

    def __init__(self, _width, _length, mass_square, thickness):
        self._width = _width
        self._length = _length
        self.mass_square = mass_square
        self.thickness = thickness

    def mass(self):

        asphalt = self._width * self._length * self.mass_square * self.thickness
        print(asphalt, "тонн")


calc = Road(20, 50, 25, 5)
calc.mass()