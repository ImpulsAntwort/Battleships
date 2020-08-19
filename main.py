from Messages import MessageHub
from Board import Board
from Player import Player
from ShipBuilder import ship_builder
from GameVis import GameVis
from Battleship import Battleship
from Shot import set_shot


def build_all_ships(player, ship_sizes=[5, 4, 3, 3, 2]):
    for size in ship_sizes:
        new_ship_fits_board = False
        while(not new_ship_fits_board):
            new_ship = Battleship(*ship_builder(size, player))
            new_ship_fits_board = player.add_ship(new_ship)
        player.update_board()


if __name__ == "__main__":

    board_size = {"x": 9, "y": 9}

    player1 = Player(name="Honigsdachs",
                     board=Board(board_size, is_hidden=False),
                     is_npc=True)
    playerNPC = Player(name="Kater",
                       board=Board(board_size, is_hidden=False),
                       is_npc=True)

    msg_hub = MessageHub(player1=player1, player2=playerNPC)
    game_vis = GameVis(player1=player1, player2=playerNPC, message_hub=msg_hub)

    build_all_ships(player=player1)
    build_all_ships(player=playerNPC)

    while(True):
        set_shot(active_player=player1, targeted_player=playerNPC)
        set_shot(active_player=playerNPC, targeted_player=player1)
