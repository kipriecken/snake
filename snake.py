import curses
from curses import wrapper, cbreak

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    position = {'x': 70, 'y': 0}

    stdscr.addstr(position['y'], position['x'], "#")
    stdscr.refresh()
    curses.noecho()

    stdscr.keypad(True)

    cbreak()
    while True:
        val = stdscr.getch()
        match val:
            case curses.KEY_RIGHT:
                position['x'] += 1
            case curses.KEY_UP:
                if position['y'] > 0:
                    position['y'] -= 1
            case curses.KEY_DOWN:
                position['y'] += 1
            case curses.KEY_LEFT:
                if position['x'] > 0:
                    position['x'] -= 1
            case ord('q'):
                break
        stdscr.clear()
        stdscr.addstr(position['y'], position['x'], "#")
        stdscr.refresh()

    stdscr.keypad(False)
    curses.echo()

wrapper(main)