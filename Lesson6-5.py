class Stationery:

    title = str

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def draw(self):
        Stationery.title = "ручка"
        print(f"Запуск отрисовки {self.title[0:4]}ой")


class Pencil(Stationery):

    def draw(self):
        Stationery.title = "карандаш"
        print(f"Запуск отрисовки {self.title}ом")


class Handle(Stationery):

    def draw(self):
        Stationery.title = "маркер"
        print(f"Запуск отрисовки {self.title}ом")


pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()