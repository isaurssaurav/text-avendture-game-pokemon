import player
from player import Player
import globalVariable

class Action():
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs
 
    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)

class MoveNorth(Action):
    def __init__(self):
        super().__init__(method=Player.move_north, name='Move north', hotkey='n')
 
 
class MoveSouth(Action):
    def __init__(self):
        super().__init__(method=Player.move_south, name='Move south', hotkey='s')
 
 
class MoveEast(Action):
    def __init__(self):
        super().__init__(method=Player.move_east, name='Move east', hotkey='e')
 
 
class MoveWest(Action):
    def __init__(self):
        super().__init__(method=Player.move_west, name='Move west', hotkey='w')
 
 
class ViewInventory(Action):
    """Prints the player's inventory"""
    def __init__(self):
        super().__init__(method=Player.print_inventory, name='View inventory', hotkey='i')

class ViewPokemons(Action):
    """Prints the player's pokemon"""


    def __init__(self):
        super().__init__(method=Player.print_available_pokemons, name='View Pokemons', hotkey='v')

class selectPokemon(Action):
    """Prints the player's pokemon"""

    def __init__(self):
        super().__init__(method=Player.select_pokemon, name='Select Pokemon', hotkey='p')

class makeFullHeath(Action):
    def __init__(self):
        super().__init__(method=Player.health_up_all_pokemon , name='Heath up for all Your Pokemon', hotkey='h')

class Attack(Action):
    def __init__(self, enemy):
        super().__init__(method=Player.attack, name="Attack", hotkey='a', enemy=enemy)

class Flee(Action):
    def __init__(self, tile):
        super().__init__(method=Player.flee, name="Flee", hotkey='f', tile=tile)

class CatchPokemon(Action):
    def __init__(self,enemy,tile):
        super().__init__(method=Player.catch_pokemon, name="Catch Pokemon", hotkey='c', enemy=enemy,tile=tile)


