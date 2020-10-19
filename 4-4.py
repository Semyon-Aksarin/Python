from random import randint

my_list = [randint(0, 50) for i in range(50)]
print(f'Список случайных 50 чисел от 0 до 50 - {my_list}')

new_list = [i for i in my_list if my_list.count(i) == 1]
print(f'Список чисел присутствующих в списке в 1 экземпляре - {new_list}')