import curses
from curses import wrapper


def main(stdscr):
    direction = 'DOWN'
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

    while True:
        val = stdscr.getch()
        if val == -1:
            val = None
        if snake[0][0] in (0, curses.COLS - 1) or snake[0][1] in (0, curses.LINES - 1):
            break
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
                if (snake[0][0] + 1, snake[0][1]) in snake:
                    break
                if snake[0][0] < curses.COLS - 1:
                    snake.insert(0, (snake[0][0] + 1, snake[0][1]))
            case 'LEFT':
                if (snake[0][0] - 1, snake[0][1]) in snake:
                    break
                if snake[0][0] > 0:
                    snake.insert(0, (snake[0][0] - 1, snake[0][1]))
            case 'UP':
                if (snake[0][0], snake[0][1] - 1) in snake:
                    break
                if snake[0][1] > 0:
                    snake.insert(0, (snake[0][0], snake[0][1] - 1))
            case 'DOWN':
                if (snake[0][0], snake[0][1] + 1) in snake:
                    break
                if snake[0][1] < curses.LINES - 1:
                    snake.insert(0, (snake[0][0], snake[0][1] + 1))
        snake.pop()
        stdscr.clear()
        for pos in snake:
            stdscr.addstr(pos[1], pos[0], "#")
        stdscr.refresh()

    stdscr.keypad(False)
    curses.echo()

wrapper(main)