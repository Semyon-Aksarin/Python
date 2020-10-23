my_file = open("Lesson5_1.txt", "w", encoding="utf-8")
line = input('Введите текст \n')
while line:
    my_file.writelines(line + '\n')
    line = input('Введите текст \n')
    if not line:
        break

my_file.close()

i = 0
with open("Lesson5_1.txt", encoding="utf-8") as f_obj:
    for line in f_obj:
        n = len(line.split())
        i += 1
        print(f'В строке {i} - {n} слов')
print(f"В файле {i} строк")

