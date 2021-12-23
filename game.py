import world
from player import Player
import os

def play(map,starting_room_index=1):
    world.load_tiles(map,starting_room_index)
    player = Player()
    # Always start from starting position
    x, y = world.starting_position
    room = world.tile_exists(x, y)

    print(room.intro_text())
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)

        if player.is_alive() and not player.victory:
            print('\n')
            print("Choose an action:\n")
            available_actions = room.available_actions(player)
            for action in available_actions:
                print(action)
            action_input = input('Action: ')
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break
    if player.victory:
        action_input = input('Action: Do you want to play next level/map? (Y/N):')
        if map == "map_waterBadge.txt": #level 2
            play('map_fireBadge.txt',2)
        if map == "map_fireBadge.txt": #level 2
            play('map_thunder_badge.txt',3)

if __name__ == "__main__":
    play('map_waterBadge.txt')