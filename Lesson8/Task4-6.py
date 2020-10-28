from abc import abstractmethod, ABC


class Interface:

    @staticmethod
    def get_main():
        print('*'*10)
        print("Основное меню:")
        print("1. Оборудование")
        print("2. Доступные остатки на складе")
        print("3. Подразделения компании")
        print("4. Завершить")
        print('*' * 10)
        try:
            choice = int(input("Введите число от 1 до 4 чтобы перейти в интересующее вас меню "))
            if choice < 1 or choice > 4:
                print("Error. Введите число от 1 до 4")
                Interface.get_main()
            if choice == 1:
                Interface.get_menu()
            if choice == 2:
                pass
            if choice == 3:
                pass
            if choice == 4:
                raise SystemExit()
        except ValueError:
            print("Это не число!")

    @staticmethod
    def get_menu():
        print("Доступные позиции оборудования:")
        print("1. Ксерокс")
        print("2. Принтер")
        print("3. Сканнер")
        input_choice = int(input("Введите номер нужного оборудования: "))
        if input_choice == 1:
            OfficeEquipment.list_of_brands()
            Copier.get_brand(input("Введите номер интересующего вас элемента меню "))
        if input_choice == 2:
            pass
        if input_choice == 3:
            pass


class Warehouse:

    items = []

    @staticmethod
    def what_to_do():
        print("Хотите переместить на склад или в конкретное отделение компании? 1/2")
        try:
            choice = int(input("Введите 1 для перемещения на склад или 2 чтобы выбрать отделение компании"))
            if choice < 1 or choice > 2:
                print("1 или 2")
                Warehouse.what_to_do()
            if choice == 1:
                Warehouse.items.append(Copier("Monochrome", brand="Xerox", country="USA", year=2017))
        except ValueError:
            print("Error! Введите 1 или 2")
            Warehouse.what_to_do()


class CompanyBranch:
    pass


class OfficeEquipment:

    def __init__(self, brand, country, year):
        self.brand = brand
        self.country = country
        self.year = year

    def __str__(self):
        return f"Бренд:{self.brand}, Страна выпуска:{self.country}, Год: {self.year}"

    @staticmethod
    def list_of_brands():
        print("Доступные бренды: \n1. Xerox\n2. HP\n3. Canon")


class Printer(OfficeEquipment):
    def __init__(self, variety, **kwargs):
        super().__init__(**kwargs)
        self.variety = variety


class Scanner(OfficeEquipment):

    def __init__(self, scan, **kwargs):
        super().__init__(**kwargs)
        self.scan = scan


class Copier(OfficeEquipment):

    def __init__(self, color, **kwargs):
        super().__init__(**kwargs)
        self.color = color

    @staticmethod
    def get_brand(choice):
        if choice == '1' or choice == "Xerox":
            choose_string = "Вы выбрали Xerox"
            print(choose_string)
            Warehouse.what_to_do()
        elif choice == '2' or choice == "HP":
            choose_string = "Вы выбрали HP"
            print(choose_string)
        elif choice == '3' or choice == "Canon":
            choose_string = "Вы выбрали Canon"
            print(choose_string)


printer = Printer("Laser", brand="HP", country="USA", year=2020)
scanner = Scanner("Digital", brand="Canon", country="Japan", year=2019)
copier = Copier("Monochrome", brand="Xerox", country="USA", year=2017)


Interface.get_main()
print(Warehouse.items[0])