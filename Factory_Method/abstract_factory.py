class Shark:
    """Class for the Hero of the kids game"""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f'{self} the Shark encounters {obstacle} and {act}'
        print(msg)


class Fish:
    """Class for obstacle"""

    def __str__(self):
        return 'a fish'

    def action(self):
        return 'eats it'


class SharkWorld:
    """Abstract Factory class to create main character and obstacles in game"""

    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t----- SHARK WORLD -----'

    def make_character(self):
        return Shark(self.player_name)

    def make_obstacle(self):
        return Fish()


class Warlock:
    """Class for the Hero of the adult game"""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f'{self} the Warlock battles against {obstacle} and {act}'
        print(msg)

class Goblin:
    def __str__(self):
        return 'a vile goblin'

    def action(self):
        return 'beats it'

class WarlockWorld:
    """Abstract Factory class to create main character and obstacles in game"""

    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t----- WARLOCK WORLD -----'

    def make_character(self):
        return Warlock(self.player_name)

    def make_obstacle(self):
        return Goblin()


class GameEnvironment:
    "Main entry point of the game"

    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)

def validate_age(name):
    """ Validate the age of the player"""
    try:
        age = input(f'Welcome {name}. How old are you?')
        age = int(age)
    except ValueError:
        print(f"Age {age} is invalid, please try again...")
        return (False, age)
    return (True, age)

def main():
    name = input("Hello. What's your name?")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
    game = SharkWorld if age < 18 else WarlockWorld
    environment = GameEnvironment(game(name))
    environment.play()


if __name__ == '__main__':
    main()