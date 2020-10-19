from math import factorial

try:
    a = int(input("Введите число: "))


    def my_func():
        for el in range(a + 1):
            yield factorial(el)

    for i in my_func():
            print(i)

except ValueError:
    print("Алярм! Ошибка!!!")