from itertools import count
from sys import argv

name, num = argv

try:
    for i in count(int(num)):
        if i > int(num) + 20:
            break
        else:
            print(i)
except ValueError:
    print("Стоит использовать число!")