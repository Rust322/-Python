from sys import argv

script_name, hours, per_hour, award = argv


def salary(hrs, pr_hr, awrd):
    return int(hrs)*int(pr_hr)*int(awrd)


print("Имя скрипта ", script_name)
print("Количество часов  ", hours)
print("Денег/час ", per_hour)
print("Премия ", award)
print("Итог:", salary(hours, per_hour, award))

"""либо проще без "salary" print("Итог:", int(hours)*int(per_hour)*int(award)) """


