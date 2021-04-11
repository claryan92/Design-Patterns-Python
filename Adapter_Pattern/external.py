class Musician:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'The musician {self.name}'

    def play(self):
        return 'plays music'


class Dancer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'The dancer {self.name}'

    def dance(self):
        return 'dances'
