import items, actions, world
import pokemons
import globalVariable
from storyDict import player_level_map_story
from playsound import playsound
from utils import select_current_level_story

class MapTile:
    def __init__(self, x, y, is_completed = False):
        self.x = x
        self.y = y
        self.is_completed= is_completed

    def intro_text(self):
        raise NotImplementedError()
 
    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves
 
    def available_actions(self,the_player):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewPokemons())
        moves.append(actions.selectPokemon())
        moves.append(actions.makeFullHeath())

        return moves

class StartingRoom1(MapTile):
    # override the intro_text method in the superclass



    def intro_text(self):
        playsound('./sound/professor-oak.mp3', False)
        global player_level
        current_player_level = select_current_level_story(globalVariable.player_level)
        return player_level_map_story[current_player_level]["intro_message"]

    def modify_player(self, player):
        #Room has no action on player
        pass

    def available_actions(self,the_player):
        # Up to level 3, it is tutorial so, player is able to move only after level 3
        current_player_level = select_current_level_story(globalVariable.player_level)
        if the_player.currentPokemon == None or globalVariable.completed_story_line[3] == False:

            return  player_level_map_story[current_player_level]["actions"]
        else:

            return self.adjacent_moves() + player_level_map_story[current_player_level]["actions"]



class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)
 
    def add_loot(self, player):
        player.inventory[self.item.name] = self.item
 
    def modify_player(self, player):
        self.add_loot(player)

    def available_actions(self,the_player):
        current_player_level = select_current_level_story(globalVariable.player_level)
        return self.adjacent_moves() + player_level_map_story[current_player_level]["actions"]
class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):

        self.enemy = enemy
        self.is_enemy_captured = False
        super().__init__(x, y)
 
    def modify_player(self, the_player):
        if self.enemy.is_alive():
            current_Pokemon_hp = the_player.currentPokemon.hp - self.enemy.damage
            playsound('./sound/clamp.mp3', False)
            if current_Pokemon_hp <= 0:
                the_player.currentPokemon.hp = 0
            else:
                the_player.currentPokemon.hp = current_Pokemon_hp

            print("*** {} does {} damage.".format(self.enemy.name, self.enemy.damage))

        else:
            if self.is_completed == False:
                print('*Your have leveled up!')
                self.is_completed = True
                globalVariable.player_level +=1

    def available_actions(self,the_player):
        if self.enemy.is_alive():
            if the_player.currentPokemon.hp > 0:
                return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
            else:
                return [actions.ViewPokemons(),actions.selectPokemon(),actions.Flee(tile=self)]
        else:
            aAction = self.adjacent_moves()
            aAction.append(actions.ViewPokemons())
            aAction.append(actions.selectPokemon())
            if(self.is_enemy_captured == False):
                aAction.append(actions.CatchPokemon(self.enemy,tile=self))
            return aAction

class EmptyCavePath(MapTile):
    def intro_text(self):
        return """
        Another unremarkable part of the cave. You must forge onwards.
        """
 
    def modify_player(self,the_player):
        #Room has no action on player
        pass

class HeathRoom(MapTile):
   def intro_text(self):
        return """
         You have arrived to pokemon hospital.
         Here you can increase the health of all you pokemon with action 'h'.
        """
   def modify_player(self,the_player):
        #Room has no action on player
        pass

class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, pokemons.Bulbasaur())
 
    def intro_text(self):
        if self.is_enemy_captured == True:
            return "You have captured Bulbasaur"
        if self.enemy.is_alive() or self.is_completed == False:
            return """
            A Bulbasaur is eating grass but you need to catch this pokemon to be pokemon master!
            """



class BulbasaurRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, pokemons.Bulbasaur())

    def intro_text(self):
        if self.is_enemy_captured == True:
            return "You have captured Bulbasaur"
        if self.enemy.is_alive() or self.is_completed == False:
            return """
            A Bulbasaur is eating grass. It noticed your presence and is angry now.
            """
        return """
            A defeated Bulbasaur is resting. You can catch it with pokeball.
        """

class CharmanderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, pokemons.Charmander())

    def intro_text(self):
        if self.is_enemy_captured == True:
            return "You have captured Charmander."
        if self.enemy.is_alive() or self.is_completed == False:
            return """
            Charmander is angry that you have entered his territory!
            """
        return """
            A defeated Charmander is resting. You can catch it with pokeball.
        """


class PoliwhirlRoom(EnemyRoom):
    def __init__(self,x,y):
         super().__init__(x,y, pokemons.Poliwhirl())
    def intro_text(self):
        if self.is_enemy_captured == True:
            return "You have captured Poliwhirl."
        if self.enemy.is_alive() or self.is_completed == False:
            return """
            Poliwhirl is swimming in the lake. It doesn't like human presence.
            """
        return """
            A defeated Poliwhirl is resting. You can catch it with pokeball.
        """

class SquirtleRoom(EnemyRoom):
    def __init__(self,x,y):
         super().__init__(x,y, pokemons.Squirtle())
    def intro_text(self):
        if self.is_enemy_captured == True:
            return "You have captured Squirtle."
        if self.enemy.is_alive() or self.is_completed == False:
            return """
            Squirtle is just looking for peace but seeing you with pokeball, it gets angry.
            """
        return """
            A defeated Squirtle is resting. You can catch it with pokeball.
        """

class TurtwigRoom(EnemyRoom):
    def __init__(self,x,y):
         super().__init__(x,y, pokemons.Turtwig())
    def intro_text(self):
        if self.is_enemy_captured == True:
            return "You have captured Turtwig."
        if self.enemy.is_alive() or self.is_completed == False:
            return """
            Turtwig is just looking for peace but seeing you with pokeball, it gets angry.
            """
        return """
            A defeated Turtwig is resting. You can catch it with pokeball.
        """

class GyaradosRoom(EnemyRoom):
    def __init__(self,x,y):
         super().__init__(x,y, pokemons.Gyarados())
    def intro_text(self):
        if self.is_enemy_captured == True:
            return "You have defeted the Gym Leader. You have earned water badge."
        if self.enemy.is_alive() or self.is_completed == False:
            return """
            Lukas: I am the Gym Leader with water badge. Prof. Oaks told me about you.
                   I have been waiting for you
            Ash: Why do you talk so much?
            Lukas: Hmm...
            Lukas: You little..., Gyarados I choose you.
            Lukas: Gyarados, Basic attack.
            """
        return """
            A defeated Gymleader, lucas is very unhappy but like the way you fought. He gives his pokemon Gyarados. You can catch it.
        """
class PonytaRoom(EnemyRoom):
    def __init__(self,x,y):
         super().__init__(x,y, pokemons.Gyarados())
    def intro_text(self):
        if self.is_enemy_captured == True:
            return "You have defeted the Gym Leader. You have earned Fire badge."
        if self.enemy.is_alive() or self.is_completed == False:
            return """
            Servus: I am the Gym Leader with water badge. Prof. Oaks told me about you.
                   I have been waiting for you
            Ash: Why do you talk so much?
            Servus: Hmm...
            Servus: You little..., Gyarados I choose you.
            Servus: Ponyta, Basic attack.
            """
        return """
            A defeated Gymleader, lucas is very unhappy but like the way you fought. He gives his pokemon Ponyta. You can catch it.
        """

class RattataRoom(EnemyRoom):
    def __init__(self,x,y):
         super().__init__(x,y, pokemons.Rattata())
    def intro_text(self):
        if self.is_enemy_captured == True:
            return "You have defeted the Gym Leader. You have earned Thunder badge."
        if self.enemy.is_alive() or self.is_completed == False:
            return """
            Harold: I am the Gym Leader with Thunder badge. It amazing that you are here now.
            Harold: Hmm...
            Harold: You little..., Rattata I choose you.
            Harold: Rattata, Basic attack.
            """
        return """
            A defeated Gymleader, lucas is very unhappy but like the way you fought. He gives his pokemon Rattata. You can catch it.
        """


class FindPokeBallRoom(LootRoom):
    def __init__(self,x,y):
        super().__init__(x, y, items.PokeBall(10))
    def intro_text(self):
        return """
        You found red and black 10 pokeball.
        You pick it up.
        """

class VictoryRoom(MapTile):
    def intro_text(self):
        return """
            ----- Outside of Gym Battle Room -------
            Prof. Oak and Ash's mom is waiting outside with happy face.

            Ash: Now, Lets begin the pokemon master journey.
        """

    def modify_player(self, player):
        player.victory = True


class StartingRoom2(MapTile):

    def intro_text(self):
        global player_level
        return """
            You have arrived in new world. Here you can find new pokemon. And Try to get fire badge from this level

        """

    def modify_player(self, player):
        #Room has no action on player
        pass

    def available_actions(self,the_player):
        current_player_level = select_current_level_story(globalVariable.player_level)
        return self.adjacent_moves() + player_level_map_story[current_player_level]["actions"]


class StartingRoom3(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        global player_level
        return """
            You have arrived in new world - Thunder workd. Here you can find new pokemon. And Try to get thunder badge from this level

        """

    def modify_player(self, player):
        #Room has no action on player
        pass

    def available_actions(self,the_player):
        current_player_level = select_current_level_story(globalVariable.player_level)
        return self.adjacent_moves() + player_level_map_story[current_player_level]["actions"]
