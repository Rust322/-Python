class Worker:

    name = str
    surname = str
    position = str
    _income = {}


class Position(Worker):

    def get_full_name(self, name, surname):
        self.name = name
        self.surname = surname
        print(name, surname)

    def get_total_income(self):
        self._income = Worker._income
        self.wage["wage"] = int(input("Введите зарплату "))
        self._income["bonus"] = int(input("Введите премию "))
        print(sum(self._income.values()))


worker = Position()
worker.get_full_name("Jonny", "Bravo")
worker.get_total_income()


