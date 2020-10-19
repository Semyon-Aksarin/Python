from random import randint

my_list = [randint(0, 1000) for i in range(15)]
print(f'Список случайных 15 чисел от 0 до 1000 - {my_list}')

new_list = [my_list[i] for i in range(len(my_list)) if my_list[i] > my_list[i - 1] and i > 0]
print(new_list)