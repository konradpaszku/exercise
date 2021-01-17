class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def set_base(self, base):
        self.base = base

    def set_height(self, height):
        self.height = height

    def get_base(self):
        return f'Podstawa trójkąta wynosi {self.base}'

    def get_height(self):
        return f'Wysokość trójkąta wynosi {self.height}'

    def get_field_triangle(self):
        result = (self.base * self.height) / 2
        return f'Pole trójkąta wynosi {result}'