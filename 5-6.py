d = {}

with open('text_6.txt', 'r', encoding="utf-8") as f_obj:
    for line in f_obj:
        n = line.split()
        a = []
        for i in n:
            b = []
            c = ''
            for x in i:
                if x.isdigit():
                    b.append(x)
            for el in b:
                c += el
            if c:
                a.append(int(c))
        print(f'Общее количество часов по предмету {n[0]} - {sum(a)}')
        d[n[0]] = sum(a)

print(d)