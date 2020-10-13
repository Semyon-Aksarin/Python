a = []
while True:
    n = input("Введите очередное значение списка или нажмите 'x' для продолжения: ")
    if n == "x":
        break
    else:
        a.append(n)

for i in a:
    if int(i) % 2 == 0:
        b = a.pop(int(i) - 1)
        a.insert(int(i) - 2, b)
    else:
        pass
print(a)
