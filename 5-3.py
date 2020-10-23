i = []
with open("text_3.txt", "r", encoding="utf-8") as f_obj:
    for line in f_obj:
        n = line.split()
        i.append(float(n[1]))
        if float(n[1]) <= 20000:
            print(f'{n[0]} очень бедствует')
s = sum(i) / len(i)
print(f"Средняя зарплатана предприятии составляет {s}, прям сказка, а не работа")
