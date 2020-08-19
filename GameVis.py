import os


class GameVis():

    # 0: empty, 1: destroyed ship, 2: missed shot, 3: healthy ship
    str_representation = {0: ".", 1: "X", 2: "0", 3: "I", 4: "="}

    def __init__(self, player1, player2, message_hub):
        self.players = [player2, player1]
        self.message_hub = message_hub
        # Observer pattern:
        for player in self.players:
            player.register_observer_vis(self)
        self.render()

    def notify(self):
        """ Belongs to Observer Pattern """
        self.render()

    def render_msg_box(self):
        msg = self.message_hub.msg_out()
        max_msg_len = 0
        for line in msg:
            if len(line) > max_msg_len:
                max_msg_len = len(line)
        border_l = "| "
        border_r = " |"

        self.print_separator(len(border_l) +
                             len(border_r) + max_msg_len, "-")
        for line in msg:
            new_line = border_l + line + " "*(max_msg_len-len(line)) + border_r
            print(new_line)
        self.print_separator(len(border_l) +
                             len(border_r) + max_msg_len, "-")

    def render(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        self.print_separator(15, "=")
        for player in self.players:
            print(f"{player.name}:")
            self.print_pretty_board(player)
            self.print_separator(15, "=")

        self.render_msg_box()

    @staticmethod
    def print_separator(num, sep):
        print(num*sep)

    def print_pretty_board(self, player):
        """ Prints the current Board """

        #  print("\n")
        border_top_numbers = "  " + \
            "".join([str(i)
                     for i in range(player.board.width)]) + " "
        print(border_top_numbers)
        border_horizontal = " +" + \
            "".join(["-" for _ in range(player.board.width)]) + "+"
        print(border_horizontal)

        pretty_board = self.pretty_board(player)
        i_row = 0
        for row in pretty_board:
            print(f"{i_row}|" + "".join(row) + "|")
            i_row += 1

        print(border_horizontal)
        #  print("\n")

    def pretty_board(self, player):
        """ Convert the int values into str representation """
        converted_board = []
        for row in player.board.board:
            converted_row = map(self.conv, row)
            converted_board.append(converted_row)

        return converted_board

    @classmethod
    def conv(cls, row_int_repr):
        return cls.str_representation[row_int_repr]
