a = input("Введите предложение из нескольких слов: ")
b = list(a.split())

for i, b in enumerate(b, 1):
    if len(b) <= 10:
        print(i, b)
    else:
        print(i, b[:10])
