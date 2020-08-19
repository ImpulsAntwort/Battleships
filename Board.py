

class Board:

    def __init__(self, board_size, is_hidden):
        self.board = []
        self.height = board_size["y"]
        self.width = board_size["x"]
        self.is_hidden = is_hidden
        self.create_empty()

    def update(self, ships, missed_shots):
        self.place_all_ships(ships)
        self.place_missed_shots(missed_shots)
        #  self.pretty_print()

    def place_missed_shots(self, missed_shots):
        for missed_shot_coords in missed_shots:
            self.update_field(missed_shot_coords, 2)

    def update_field(self, coords, board_value):
        self.board[coords[1]][coords[0]] = board_value

    def place_all_ships(self, all_ships):
        for ship in all_ships:
            self.place_ship(ship.parts, ship.orientation)

    def place_ship(self, ship_parts, orientation):
        """ Places the ship's status (int representation) on a board """

        if self.is_hidden:
            ship_symbol = 0
        else:
            ship_symbol = 3 if orientation == "V" else 4

        for ship_part in ship_parts.items():
            coords = ship_part[0]
            value = ship_symbol if ship_part[1] else 1
            self.update_field(coords, value)

    def set_shot(self, shot_coords):
        """ Updates the Board with the new Shot. """

        new_board_val = self.new_board_value(shot_coords)
        self.update_field(shot_coords, new_board_val)

    def new_board_value(self, shot):
        """ Decides whether the new shot missed or hitted a ship """

        content_targeted_place = self.board[shot[1]][shot[0]]

        if content_targeted_place == 0:
            """ Shot on empty place, return missed shot """
            return 2
        elif content_targeted_place == 1:
            """ Shot on already destroyed part, return destroyed part """
            return 1
        elif content_targeted_place == 2:
            """ Shot on missed shot, return missed shot """
            return 2
        elif content_targeted_place == 3:
            """ Shot on healthy ship part, return destroyed part """
            return 1
        else:
            raise ValueError("Falscher int-Wert auf dem Board")

    def create_empty(self):
        """ Creates an empty board for further use for placing
        ships and shots"""

        for _ in range(self.height):
            empty_line = [0 for _ in range(self.width)]
            self.board.append(empty_line)

