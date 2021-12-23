class Pokemon:
    def __init__(self, name, hp, damage,type):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.type =type

    def is_alive(self):
        return self.hp > 0

class Pikachu(Pokemon):
    def __init__(self):
        super().__init__(name="Pikachu", hp=10, damage=2,type='Lighting')

class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__(name="Bulbasaur", hp=10, damage=1,type='Grass')

class Ditto(Pokemon):
    def __init__(self):
        super().__init__(name="Ditto", hp=20, damage=10, type='Magic')

class Charmander(Pokemon):
    def __init__(self):
        super().__init__(name="Charmander", hp=6, damage=3,type='Fire')

class Poliwhirl(Pokemon):
    def __init__(self):
        super().__init__(name="Poliwhirl", hp=20, damage=4,type='water')

class Squirtle(Pokemon):
    def __init__(self):
        super().__init__(name="Squirtle",hp=25,damage=3,type = 'water')

class Turtwig(Pokemon):
    def __init__(self):
        super().__init__(name='Turtwig',hp=15,damage=2,type='Grass')

class Gyarados(Pokemon):
    def __init__(self):
        super().__init__(name="Gyarados",hp=25,damage=3,type = 'water')