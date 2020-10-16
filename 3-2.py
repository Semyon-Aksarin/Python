def my_func(*args):
    print(*args)


name = input("Введите ваше имя: ")
lastname = input("Введите вашу фамилию: ")
year = input("Введите год вашего рождения: ")
city = input("Введите название города в котором вы проживаете: ")
email = input("Введите ваш адрес электронной почты: ")
phone = input("Введите ваш номер телефона: ")

my_func(name, lastname, year, city, email, phone)
