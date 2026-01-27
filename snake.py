import curses
from curses import wrapper


def main(stdscr):
    direction = 'DOWN'
    curses.curs_set(0)
    stdscr.clear()
    position = {'x': 70, 'y': 0}
    curses.halfdelay(1)
    stdscr.nodelay(True)

    stdscr.addstr(position['y'], position['x'], "#")
    stdscr.refresh()
    curses.noecho()

    stdscr.keypad(True)
    counter = 0

    while True:
        counter += 1
        val = stdscr.getch()
        if val == -1:
            val = None
        match val:
            case curses.KEY_RIGHT:
                direction = 'RIGHT'
            case curses.KEY_UP:
                direction = 'UP'
            case curses.KEY_DOWN:
                direction = 'DOWN'
            case curses.KEY_LEFT:
                direction = 'LEFT'
            case 'q' | 'Q':
                break
        match direction:
            case 'RIGHT':
                position['x'] += 1
            case 'LEFT':
                if position['x'] > 0:
                    position['x'] -= 1
            case 'UP':
                if position['y'] > 0:
                    position['y'] -= 1
            case 'DOWN':
                position['y'] += 1
        stdscr.clear()
        stdscr.addstr(position['y'], position['x'], "#")
        stdscr.refresh()

    stdscr.keypad(False)
    curses.echo()

wrapper(main)