my_list = [7, 5, 3, 3, 2]
a = input("Введите новый элемент рейтинга (это обязательно должно быть число): ")

if a.isdigit():
    for i in my_list:
        if i < int(a):
            my_list.insert(my_list.index(i), int(a))
            break
        else:
            pass
    if int(a) <= my_list[- 1]:
        my_list.append(int(a))
    print(my_list)
else:
    print("Я же говорил число!")
