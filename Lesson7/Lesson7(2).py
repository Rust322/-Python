from abc import abstractmethod, ABC


class Clothes:
    @abstractmethod
    def data(self):
        pass


class Coat(ABC, Clothes):
    def __init__(self, v):
        self.v = v

    def data(self):
        return self.v/6.5 + 0.5

    @property
    def addition(self):
        return f"При объеме материала = {self.v} получится {round(self.v/6.5 + 0.5)} пальто"


class Suit(ABC, Clothes):
    def __init__(self, h):
        self.h = h

    def data(self):
        return 2 * self.h + 0.3

    @property
    def addition(self):
        return f"При объеме материала = {self.h} получится {round(2 * self.h + 0.3)} костюм(а/ов)"


coat = Coat(5)
suit = Suit(5)

print(coat.data())
print(coat.addition)
print(suit.data())
print(suit.addition)