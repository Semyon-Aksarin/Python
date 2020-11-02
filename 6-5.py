class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationary):
    def draw(self):
        print(f'Вы взяли {self.title}. Запуск отрисовки ручкой')


class Pencil(Stationary):
    def draw(self):
        print(f'Вы взяли {self.title}. Запуск отрисовки карандашом')


class Handle(Stationary):
    def draw(self):
        print(f'Вы взяли {self.title}. Запуск отрисовки маркером')


pen = Pen('Parker')
pencil = Pencil('ErichKrause')
handle = Handle('Stabilo')
pen.draw()
pencil.draw()
handle.draw()
