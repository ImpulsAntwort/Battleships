
class Battleship():

    def __init__(self, parts, orientation):
        self.parts = parts
        self.orientation = orientation
        self.alive = True

    def is_hit(self, shot_coords):
        is_hit = False
        if shot_coords in set(self.parts.keys()):
            is_hit = True
        return is_hit

    def hit_on_healthy_part(self, shot_coords):
        ''' checks whether the shot coords occure in ship part coords.
        Returns True, if a ship part has been destroyed with the current shot.
        Returns False, if shot hits an already destroyed part or misses
        the ship'''
        is_new_hit = self.parts[shot_coords]
        self.parts[shot_coords] = False
        return is_new_hit

    def is_alive(self):

        self.alive = any(self.parts.values())
        return self.alive

