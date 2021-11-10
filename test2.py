import os
import imghdr
import curses
from curses import wrapper
import random
from time import sleep


def files(path="."):
    ls = os.listdir(path)

    # Sõnastik failitüüpide jaoks
    contents = {}
    imgs = set()
    dirs = set()
    for el in ls:
        is_img = imghdr.what(el)
        if is_img:
            imgs.add(el)
        else:
            dirs.add(el)
    
    contents[0] = dirs
    contents[1] = imgs
    return contents       

screen = curses.initscr()
# Värvide jaoks, default_colors võimaldab kasutada transparent väärtust.
curses.start_color()
curses.use_default_colors()
curses.init_pair(2, curses.COLOR_RED, -1)

# Terminali suurus
num_rows, num_cols = screen.getmaxyx()

current_files = files()

print(current_files[0])
# lines, columns, start line, start column
main_window = curses.newwin((len(current_files[0]) + len(current_files[1])), 60, 2, 15)
j = 0
for i in range(0,2):
    if i == 0:
        for el in current_files[i]:
            main_window.addstr(j, 10, str(el))
            j += 1
    else:
        for el in current_files[i]:
            main_window.addstr(j, 10, str(el), curses.color_pair(2))
            j += 1

main_window.refresh()
sleep(4)

curses.endwin()
