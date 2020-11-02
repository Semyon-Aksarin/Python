class Worker:
    def __init__(self, name, surname, position, salary, prize):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'salary' : salary, 'prize' : prize}


class Position(Worker):
    def get_full_name(self):
        return f'Полное имя работника {self.name} {self.surname}'

    def get_total_income(self):
        profit = sum(self._income.values())
        return f'Зарплата {self.name} {self.surname} составляет {profit}'

woker = Position('Steve', 'Jobs', 'Manager', 50000, 15000)
print(woker.get_full_name())
print(woker.get_total_income())
print(woker.position)