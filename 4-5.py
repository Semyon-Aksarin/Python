from functools import reduce

my_list = [i for i in range(100, 1001) if i % 2 == 0]
print(f'Результат перемножения всех элементов списка {reduce(lambda x, y: x*y, my_list)}')