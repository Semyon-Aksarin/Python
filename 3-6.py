def int_func(a):
    return a.title()


b = input("Введите предложение: ")
c = list(b.split(" "))
d = []

for i in c:
    for n in i:
        if n < "a" or n > "z":
            break
    else:
        d.append(int_func(i))


f = " ".join(d)
print(f)

