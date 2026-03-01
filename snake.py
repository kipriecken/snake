import curses
from curses import wrapper
import random


def main(stdscr):
    movement = (0, 1)
    curses.curs_set(0)
    stdscr.clear()
    snake = [(70, x) for x in range(8, 5, -1)]

    high_score = 0
    try:
        with open("highscore.txt", "r") as f:
            high_score = int(f.read().strip())
    except FileNotFoundError:
        with open("highscore.txt", "w") as f:
            f.write("0")

    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)

    left_boundary = 30
    top_boundary = 1
    right_boundary = 90
    bottom_boundary = 20
    horizontal_walls = [
        (x, top_boundary) for x in range(left_boundary + 1, right_boundary)
    ] + [(x, bottom_boundary) for x in range(left_boundary, right_boundary)]
    vertical_walls = [
        (left_boundary, y) for y in range(top_boundary + 1, bottom_boundary + 1)
    ] + [(right_boundary, y) for y in range(top_boundary + 1, bottom_boundary + 1)]

    food = (0, 0)

    def print_score():
        score = len(snake) - 3
        new_high_score = "NEW HIGH SCORE!"
        if score > high_score:
            with open("highscore.txt", "w") as f:
                f.write(str(score))
        if score > high_score:
            stdscr.addstr(
                0, left_boundary, f" Score: {score} {new_high_score}", curses.A_REVERSE
            )
        else:
            stdscr.addstr(
                0,
                left_boundary,
                f" Score: {score} High Score: {high_score}",
                curses.A_REVERSE,
            )
            new_high_score = ""

    def spawn_food():
        nonlocal food
        food = (
            random.randint(left_boundary + 1, right_boundary - 1),
            random.randint(top_boundary + 1, bottom_boundary - 1),
        )
        while food in snake:
            food = (
                random.randint(left_boundary + 1, right_boundary - 1),
                random.randint(top_boundary + 1, bottom_boundary - 1),
            )

    def print_walls():
        for wall in horizontal_walls:
            stdscr.addstr(wall[1], wall[0], "_", curses.color_pair(3))
        for wall in vertical_walls:
            stdscr.addstr(wall[1], wall[0], "|", curses.color_pair(3))

    def print_snake():
        for pos in snake:
            if pos == snake[0]:
                stdscr.addstr(pos[1], pos[0], "#", curses.color_pair(4))
            else:
                stdscr.addstr(pos[1], pos[0], "#", curses.color_pair(1))

    print_score()
    print_walls()
    print_snake()
    spawn_food()
    curses.halfdelay(1)
    stdscr.nodelay(True)

    stdscr.refresh()
    curses.noecho()

    stdscr.keypad(True)

    def advance_snake(next_head):
        snake.insert(0, next_head)
        snake.pop()

    def check_collision(next_head):
        if next_head in snake:
            return True
        if next_head[0] < left_boundary or next_head[0] >= right_boundary:
            return True
        if next_head[1] < top_boundary + 1 or next_head[1] >= bottom_boundary:
            return True
        return False

    def render():
        stdscr.clear()
        print_snake()
        print_walls()
        print_score()
        stdscr.addstr(food[1], food[0], "*", curses.color_pair(2))
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
            case "q" | "Q":
                break

        next_head = (snake[0][0] + movement[0], snake[0][1] + movement[1])
        if check_collision(next_head):
            break
        if next_head == food:
            snake.insert(0, next_head)
            curses.beep()
            spawn_food()
        else:
            advance_snake(next_head)

        render()

    stdscr.keypad(False)
    curses.echo()


wrapper(main)
