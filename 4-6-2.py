from itertools import cycle
from sys import argv

name, num = argv
c = 0
my_list = ['В', 'ы', 'к', 'л', 'ю', 'ч', 'и', ' ', 'м', 'е', 'н', 'я', '!', ' ']

try:
    for i in cycle(my_list):
        if c > 50 or c > int(num):
            break
        print(i)
        c += 1
except ValueError:
    print("Стоит использовать число!")







