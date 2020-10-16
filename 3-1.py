def my_func(x, y):
    try:
        if int(y) == 0:
            print("На 0 делить низзззя!!!")
        else:
            c = int(x) / int(y)
            print(c)
    except ValueError:
            print("Введены неправильные значения!")


x = input("Введите делимое число: ")
y = input("Введите делитель: ")

my_func(x, y)