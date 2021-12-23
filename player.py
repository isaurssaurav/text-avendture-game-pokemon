import random 
import items, world, pokemons
import globalVariable
import copy
import tutorialText
from playsound import playsound
# from storyDescriptionAndActions import player_level_map_story

class Player():
    def __init__(self):
        self.inventory = {"Gold": items.Gold(10)} #Inventory on startup
        self.available_pokemons = [pokemons.Pikachu()]
        self.currentPokemon = None
        self.hp = 100 # Health Points
        self.location_x, self.location_y = world.starting_position  #(0, 0)
        self.victory = False #no victory on start up

    def flee(self, tile):
        """Moves the player randomly to an adjacent tile"""
        playsound('./sound/flee.mp3', False)
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

    # is_alive method
    def is_alive(self):
        is_game_over = True
        for po in self.available_pokemons:
           if po.hp > 0:
                is_game_over = False
        if is_game_over:
            return False
        if self.currentPokemon != None and self.currentPokemon.hp < 0:
            print('Sadly your pokemon', self.currentPokemon.name, ' is defeated.', ' Please select another pokemon')
            number = input('select pokemon index')
            if int(number)-1 < len(self.available_pokemons) and self.available_pokemons[int(number)-1]:
                self.currentPokemon = self.available_pokemons[int(number)-1]
                print('Pokemon', self.currentPokemon.name, ' is selected.')
                return True

            return True
        else:
            return True

    def print_inventory(self):
        print('****** LEVEL: ', globalVariable.player_level, '*******')
        for attributes in self.inventory.keys():
            print(self.inventory[attributes].name + ' : ' + str(self.inventory[attributes].value))

          # Story line 3 starts
        if(globalVariable.completed_story_line[3] == False):
            globalVariable.completed_story_line[3] = True
            globalVariable.player_level +=1
            print(tutorialText.tutorial_text_3)
        # Story line 3 ends

    def health_up_all_pokemon(self):
        playsound('./sound/recovery.mp3', False)

        for pokemon in self.available_pokemons:
            pokemon.hp = 10

    def print_available_pokemons(self):
        index = 1
        for pokemon in self.available_pokemons:
            print(index,'. ' ,pokemon.name)
            print('----------------')
            print('Type: ', pokemon.type)
            print('Damage: ', pokemon.damage)
            print('HP: ', pokemon.hp)
            print('\n')
            index +=1
        # Story line 1 starts

        if(globalVariable.completed_story_line[1] == False):
            globalVariable.completed_story_line[1] = True
            globalVariable.player_level +=1
            print(tutorialText.tutorial_text_1)
        # Story line 1 ends

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())
 
    def move_north(self):
        self.move(dx=0, dy=-1)
 
    def move_south(self):
        self.move(dx=0, dy=1)
 
    def move_east(self):
        self.move(dx=1, dy=0)
 
    def move_west(self):
        self.move(dx=-1, dy=0)

    def select_pokemon(self):
        number = input('Select Pokemon Id: ')
        if int(number)-1 < len(self.available_pokemons) and self.available_pokemons[int(number)-1]:
            self.currentPokemon = self.available_pokemons[int(number)-1]
            print('Pokemon', self.currentPokemon.name, ' is selected.')
        else:
            print('There is no pokemon in this index. Please view pokemon index and select carefully.')
        # Story line 2 starts
        if(globalVariable.completed_story_line[2] == False):
            globalVariable.completed_story_line[2] = True
            globalVariable.player_level +=1
            print(tutorialText.tutorial_text_2)
        # Story line 2 ends
    def attack(self, enemy):
        playsound('./sound/hit.mp3', False)
        print('-------{} VS {}----------'.format(self.currentPokemon.name,enemy.name))

        print('{} HP: {}'.format(self.currentPokemon.name,self.currentPokemon.hp))

        print("*** {} damaged {} against {}!".format(self.currentPokemon.name, self.currentPokemon.damage ,enemy.name))

        enemy.hp -=  self.currentPokemon.damage

        print('{} HP: {}'.format(enemy.name, enemy.hp))

        if not enemy.is_alive():
            print("You have defeated {}!".format(enemy.name))

    def catch_pokemon(self,enemy,tile):
        # TODO : decrease the pokeball value
        playsound('./sound/catch_pokemon.mp3', False)

        captured_enemy = copy.deepcopy(enemy)
        self.available_pokemons.append(captured_enemy)

        tile.is_enemy_captured = True
        print('you have catch the pokemon', enemy.name)

    def do_action(self, action, **kwargs):
     action_method = getattr(self, action.method.__name__)
     if action_method:
                action_method(**kwargs)