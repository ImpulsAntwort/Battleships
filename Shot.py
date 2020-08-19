from random import randint
from time import sleep


def set_shot(active_player, targeted_player):

    shot_generator = npc_shot if active_player.is_npc else user_shot
    shot_coords = shot_generator(active_player.board)
    targeted_player.process_incoming_shot(shot_coords)
    targeted_player.update_board()


def user_shot(board):
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


def npc_shot(board):
    x = randint(0, board.width-1)
    y = randint(0, board.height-1)
    sleep(1)
    return (x, y)

