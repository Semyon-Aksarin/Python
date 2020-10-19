from sys import argv

name, hours, cent_per_hour, award = argv
def my_func(hours, cent_per_hour, award):
    try:
        return (int(hours) * int(cent_per_hour)) + int(award)
    except ValueError:
        print("Ошибка!")

print(my_func(hours, cent_per_hour, award))