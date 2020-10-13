a = []
b = "название"
c = "цена"
d = "количество"
e = "eд"
z = 0

while True:
    i = input("Введите название товара: ")
    k = input("Введите цену товара: ")
    l = input("Введите количество товара: ")
    m = input("Введите единицу измерения товара: ")
    n = input("Нажмите q для завершения ввода товаров или любую другую клавишу для введения следующего товара: ")
    z += 1
    a.append(tuple([z, {b : i, c : k, d : l, e : m}]))
    if n != "q":
        continue
    else:
        break

p = []
x = list(a[0][1])
for y in range(len(x)):
    p.append(a[y-1][1].items())
print(p)
