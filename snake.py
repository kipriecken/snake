import curses
from curses import wrapper


def main(stdscr):
    movement = (0, 1)
    curses.curs_set(0)
    stdscr.clear()
    snake = [
        (70, 3),
        (70, 2),
        (70, 1),
        (70, 0),
    ]
    curses.halfdelay(1)
    stdscr.nodelay(True)

    for pos in snake:
        stdscr.addstr(pos[1], pos[0], "#")
    stdscr.refresh()
    curses.noecho()

    stdscr.keypad(True)

    def advance_snake(next_head):
        snake.insert(0, next_head)
        snake.pop()
    
    def print_snake():
        for pos in snake:
            stdscr.addstr(pos[1], pos[0], "#")

    def check_collision(next_head):
        if next_head in snake:
            return True
        if next_head[0] < 0 or next_head[0] >= curses.COLS:
            return True
        if next_head[1] < 0 or next_head[1] >= curses.LINES:
            return True
        return False
    
    def render():
        stdscr.clear()
        print_snake()
        stdscr.refresh()

    while True:
        val = stdscr.getch()
        if val == -1:
            val = None
        match val:
            case curses.KEY_RIGHT:
                if movement != (-1, 0):
                    movement = (1, 0)
            case curses.KEY_LEFT:
                if movement != (1, 0):
                    movement = (-1, 0)
            case curses.KEY_UP:
                if movement != (0, 1):
                    movement = (0, -1)
            case curses.KEY_DOWN:
                if movement != (0, -1):
                    movement = (0, 1)
            case 'q' | 'Q':
                break
        
        next_head = (snake[0][0] + movement[0], snake[0][1] + movement[1])
        if check_collision(next_head):
            break
        advance_snake(next_head)

        render()

    stdscr.keypad(False)
    curses.echo()

wrapper(main)