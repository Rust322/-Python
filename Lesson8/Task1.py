class MyDate:

    def __init__(self, data):
        self.date = data

    @classmethod
    def getdate(cls, data):
        cls.data = [int(el) for el in data.split("-")]
        return cls.data

    @staticmethod
    def valid_date(data):
        valid_month = [el for el in range(1, 13)]
        valid_day31 = [1, 3, 5, 7, 8, 10, 12]
        valid_day30 = [4, 6, 9, 11]
        valid_day29 = [2]
        if data[1] in valid_month:
            if data[1] in valid_day31 and data[0] in range(1, 32):
                print("-".join(str(el) for el in data))
            elif data[1] in valid_day30 and data[0] in range(1, 31):
                print("-".join(str(el) for el in data))
            elif data[1] in valid_day29 and data[0] in range(1, 30) and data[2] % 4 == 0:
                print("-".join(str(el) for el in data), "- Вискосный год!")
            elif data[1] in valid_day29 and data[0] in range(1, 29) and data[2] % 4 != 0:
                print("-".join(str(el) for el in data))
            else:
                print("Такого дня быть не может!")
        else:
            print("Месяц не верен!")
        return data


MyDate.valid_date(MyDate.getdate("31-12-2011"))
MyDate.valid_date(MyDate.getdate("31-12-2020"))
MyDate.valid_date(MyDate.getdate("28-02-2020"))
MyDate.valid_date(MyDate.getdate("29-02-2020"))
MyDate.valid_date(MyDate.getdate("29-13-2020"))



