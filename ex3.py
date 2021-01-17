class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.field = 3.14 * radius ** 2

    def set_radius(self, radius):
        self.radius = radius
        self.field = 3.14 * radius ** 2

    def get_radius(self):
        return f'Promień koła wynosi {self.radius}'

    def get_field(self):
        return f'Pole koła wynosi {self.field:.2f}'

    def get_circuit(self):
        result = self.radius * 2 * 3.14
        return f'Obwód koła wynosi {result:.2f}'


