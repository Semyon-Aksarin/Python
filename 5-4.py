rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open("text_4.txt", "r", encoding="utf-8") as f_obj:
    for line in f_obj:
        n = line.split()
        new_file.append(rus[n[0]] + '  ' + n[1] + ' ' + n[2])
    print(new_file)

with open('text_4_new.txt', 'w') as f_obj_2:
    for i in new_file:
        f_obj_2.writelines(i + '\n')
