class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        mass = self._length * self._width * 125 / 1000
        return mass


road = Road(5000, 20)
print(road.mass())
