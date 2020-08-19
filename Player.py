from sys import exit


class Observable:

    def __init__(self):
        self.observers_vis = []
        self.observers_msg = []

    def register_observer_vis(self, observer):
        self.observers_vis.append(observer)

    def register_observer_msg(self, observer):
        self.observers_msg.append(observer)

    def notify_observer_vis(self):
        for observer in self.observers_vis:
            observer.notify()

    def notify_observer_msg(self, plr_name, msg):
        for observer in self.observers_msg:
            observer.notify(plr_name, msg)


class Player(Observable):

    def __init__(self, name, board, is_npc=False):
        super().__init__()
        self.name = name
        self.board = board
        self.is_npc = is_npc
        self.ships = []
        self.missed_shots = set()

    def add_ship(self, new_ship):
        if self.ship_fits_board(new_ship):
            self.ships.append(new_ship)
            self.board.place_all_ships(self.ships)
            return True
        else:
            return False

    def ship_fits_board(self, new_ship):
        for coords in new_ship.parts.keys():
            if coords[0] >= 0 and coords[0] < self.board.width and coords[1] >= 0 and coords[1] < self.board.height:
                for other_ship in self.ships:
                    if other_ship.is_hit(coords):
                        return False
            else:
                return False
        return True

    def update_board(self):
        self.board.place_all_ships(self.ships)
        self.board.place_missed_shots(self.missed_shots)
        self.notify_observer_vis()

    def process_incoming_shot(self, shot_coords):
        any_ship_hit = False

        for ship in self.ships:
            if ship.is_hit(shot_coords):
                any_ship_hit = True
                if ship.hit_on_healthy_part(shot_coords):
                    self.notify_observer_msg(self.name, "getroffen!")
                    if not ship.is_alive():
                        self.notify_observer_msg(
                            self.name, "Schiff versenkt.")
                        if self.all_ships_destroyed():
                            self.notify_observer_msg(
                                self.name, "hat alle Schiffe verloren!")
                            self.notify_observer_msg(
                                self.name, "HAT VERLOREN")
                            exit()
                break
        if not any_ship_hit:
            self.missed_shots.add(shot_coords)

    def all_ships_destroyed(self):
        all_ships_lost = True
        for ship in self.ships:
            all_ships_lost = all_ships_lost and not ship.alive
        return all_ships_lost
