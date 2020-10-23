def summary():
    try:
        with open('file_5.txt', 'w+', encoding="utf-8") as f_obj:
            line = input('Введите цифры через пробел \n')
            f_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набрано число. Ошибка ввода-вывода')
summary()