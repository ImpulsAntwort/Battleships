""" Functions for puzzling the ships together.
    assembly_ship_parts is following the factory pattern """
from random import randint, choice


def ship_builder(size, player):

    if player.is_npc:
        ship_generator = _define_ship_randomly
    else:
        ship_generator = _define_ship_by_user
    start_coords, direction = ship_generator(size, player.board)
    ship_parts = _assembly_ship_parts(start_coords, direction, size)
    orientation = _get_ship_axis(direction)
    return ship_parts, orientation


def _define_ship_randomly(size, board):
    x = randint(0, board.width-1)
    y = randint(0, board.height-1)
    direction = choice(["N", "E", "S", "W"])
    return (x, y), direction


def _define_ship_by_user(size, *args):
    """ User inputs for a single ship """

    print(f"Setze die Startkoordinaten für ein Schiff mit Größe {size}")
    start_coords_inp = input("x,y -> ")
    x, y = start_coords_inp.split(",")
    start_coords = (int(x), int(y))

    print("Gen welche Himmelsrichtung? Mögliche Werte: 'N', 'E', 'S', 'W'")
    direction = input("-> ")
    print("\n\n")

    return start_coords, direction


def _get_ship_axis(direction):
    """ Determines the axis (horizonal/vertical) of the ship """

    orientation = {"N": "V", "S": "V", "E": "H", "W": "H"}
    return orientation[direction]


def _assembly_ship_parts(start_coords, direction, size):
    """ Builds the Ship from a starting point (x,y) along a
    direction (N,E,S,W) and determines it's orientation (H/V).
    Ship is a dict with keys as coordinates and values as life points"""

    ship_part_assembler = _build_orientator(direction)
    #  ship_coords = list()
    ship_parts = dict()
    for i_ship_part in range(size):
        new_part = ship_part_assembler(start_coords, i_ship_part)
        ship_parts[new_part] = True
    return ship_parts


def _build_orientator(direction):
    """ Chooses a building function according to the direction """

    orientator = {"S": _create_part_s,
                  "N": _create_part_n,
                  "E": _create_part_e,
                  "W": _create_part_w}
    return orientator[direction]


def _create_part_s(start_coords, i_ship_part):
    """ Creates a new ship part in southern direction """

    new_ship_part = (start_coords[0], start_coords[1] + i_ship_part)
    return new_ship_part


def _create_part_n(start_coords, i_ship_part):
    """ Creates a new ship part in northern direction """

    new_ship_part = (start_coords[0], start_coords[1] - i_ship_part)
    return new_ship_part


def _create_part_e(start_coords, i_ship_part):
    """ Creates a new ship part in eastern direction """

    new_ship_part = (start_coords[0] + i_ship_part, start_coords[1])
    return new_ship_part


def _create_part_w(start_coords, i_ship_part):
    """ Creates a new ship part in western direction """

    new_ship_part = (start_coords[0] - i_ship_part, start_coords[1])
    return new_ship_part
