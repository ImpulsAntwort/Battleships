from random import randint
from time import sleep


def set_shot(active_player, targeted_player, ki=None):

    shot_generator = npc_shot if active_player.is_npc else user_shot
    shot_coords = shot_generator(active_player.board, ki)
    game_goes_on = targeted_player.process_incoming_shot(shot_coords)
    targeted_player.update_board()
    return game_goes_on


def user_shot(board, *args):
    go_on = True
    while(go_on):
        try:
            shot_coords = input("Setze Schuss Koordinaten\nx,y -> ")
            x, y = shot_coords.split(shot_coords[1])
            shot_coords = (int(x), int(y))
            if shot_coords[0] >= 0 and shot_coords[0] < board.width and shot_coords[1] >= 0 and shot_coords[1] < board.height:
                go_on = False
            else:
                raise ValueError
        except ValueError:
            print("Ungültige Eingabe.")
    return shot_coords


def npc_shot(board, ki=None):
    x = randint(0, board.width-1)
    y = randint(0, board.height-1)
    sleep(0.5)
    return (x, y)
