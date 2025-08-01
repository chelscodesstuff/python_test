import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
import random


def main(stdscr):
    curses.curs_set(0)
    height, width = stdscr.getmaxyx()
    win = curses.newwin(height, width, 0, 0)
    win.keypad(True)
    win.timeout(100)

    x = width // 4
    y = height // 2
    snake = [
        [y, x],
        [y, x - 1],
        [y, x - 2],
    ]

    food = [height // 2, width // 2]
    win.addch(food[0], food[1], curses.ACS_PI)

    key = KEY_RIGHT

    while True:
        next_key = win.getch()
        key = key if next_key == -1 else next_key

        if key == KEY_RIGHT:
            head = [snake[0][0], snake[0][1] + 1]
        elif key == KEY_LEFT:
            head = [snake[0][0], snake[0][1] - 1]
        elif key == KEY_UP:
            head = [snake[0][0] - 1, snake[0][1]]
        elif key == KEY_DOWN:
            head = [snake[0][0] + 1, snake[0][1]]
        else:
            continue

        if (
            head[0] in [0, height] or
            head[1] in [0, width] or
            head in snake
        ):
            break

        snake.insert(0, head)

        if head == food:
            food = None
            while food is None:
                nf = [
                    random.randint(1, height - 2),
                    random.randint(1, width - 2)
                ]
                food = nf if nf not in snake else None
            win.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            win.addch(tail[0], tail[1], ' ')

        win.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

    msg = "Game Over!"
    win.addstr(height // 2, width // 2 - len(msg) // 2, msg)
    win.nodelay(False)
    win.getch()


def run():
    curses.wrapper(main)


if __name__ == "__main__":
    run()
