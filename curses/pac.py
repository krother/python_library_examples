"""
Minimalistic pac game
"""
import curses
import random
import time

# WASD keys + exit key (X)
KEY_COMMANDS = {97: (-1, 0), 100: (1, 0), 119: (0, -1), 115: (0, 1), 120: (0, 0)}

# prepare the screen
screen = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.curs_set(0)
curses.noecho()
curses.raw()
screen.keypad(False)

win = curses.newwin(30, 15, 0, 0)
win.nodelay(True)


def draw(level, player, ghost, screen, win):
    screen.clear()
    for y, row in enumerate(level):
        for x, char in enumerate(row):
            screen.addch(y, x*2, char, curses.color_pair(1))
    screen.addch(player[1], player[0] * 2, "O", curses.color_pair(1))
    screen.addch(ghost[1], ghost[0] * 2, "G", curses.color_pair(1))
    win.refresh()
    screen.refresh()


def get_keyboard(win):
    char = win.getch()
    return KEY_COMMANDS.get(char)


def move(position, direction, level):
    x, y = position
    dx, dy = direction
    nx, ny = x + dx, y + dy
    if level[ny][nx] == "#":
        return x, y
    return nx, ny


def move_player(player, direction, level):
    x, y = move(player, direction, level)
    level[y] = level[y][:x] + " " + level[y][x+1:]
    return x, y


def move_ghost(ghost, level):
    direction = random.choice(list(KEY_COMMANDS.values())[:-1])
    return move(ghost, direction, level)


def pac_game(screen):
    """called by curses"""
    level = """
###########
#....#....#
#.##...##.#
#.#..#..#.#
#....#....#
##.#####.##
#....#....#
#.#..#..#.#
#.##...##.#
#....#....#
###########""".strip().split()
    player = 1, 1
    ghost = 9, 9
    
    while player != ghost and any([row for row in level if "." in row]):
        ghost = move_ghost(ghost, level)
        draw(level, player, ghost, screen, win)
        if direction := get_keyboard(win):
            if direction == (0, 0):
                player = ghost
            else:
                player = move_player(player, direction, level)
        else:
           time.sleep(0.1)


if __name__ == "__main__":
    curses.wrapper(pac_game)
    curses.endwin()