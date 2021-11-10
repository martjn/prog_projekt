import os
import imghdr
import curses
from curses import wrapper
from time import sleep


def files(path="."):
    ls = os.listdir(path)

    # Sõnastik failitüüpide jaoks
    contents = {}
    imgs = set()
    dirs = set()
    etc = set()
    for el in ls:
        if os.path.isdir(el):
            dirs.add(el)
        elif imghdr.what(el):
            imgs.add(el)
        else: 
            etc.add(el)
    
    contents[0] = dirs
    contents[1] = imgs
    contents[2] = etc
    return contents       

def print_menu(main_window, current_row):
    main_window.clear()
    j = 0
    for i in range(0,3):
        if i == 0:
            for el in current_files[i]:
                if j == current_row:
                    main_window.addstr(j, 10, str(el), curses.color_pair(3))
                else:
                    main_window.addstr(j, 10, str(el), curses.color_pair(1))
                j += 1 
        elif i == 1:
            for el in current_files[i]:
                if j == current_row:
                    main_window.addstr(j, 10, str(el), curses.color_pair(3))
                else:
                    main_window.addstr(j, 10, str(el), curses.color_pair(2))
                j += 1
        elif i == 2:
            for el in current_files[i]:
                if j == current_row:
                    main_window.addstr(j, 10, str(el), curses.color_pair(3))
                else:
                    main_window.addstr(j, 10, str(el))
                j += 1
    main_window.refresh()

current_files = files()
def main(stdscr):
    # Värvide jaoks, default_colors võimaldab kasutada transparent väärtust.
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(2, curses.COLOR_GREEN, -1)
    curses.init_pair(1, curses.COLOR_RED, -1)
    curses.init_pair(3, curses.COLOR_YELLOW, -1)

    menu_len = len(current_files[0]) + len(current_files[1]) + len(current_files[2])

    # rows, text length, start line (lükkab alla), start column (lükkab paremale)
    main_window = curses.newwin(menu_len + 1, 100, 2, 10)

    current_row = 0

    stdscr.refresh()
    print_menu(main_window, current_row)


    while True:
        key = stdscr.getch()
        #key = main_window.getch(0, 19)

        if key == curses.KEY_UP or key == 107:
            if current_row > 0:
                current_row -= 1
            else:
                current_row = menu_len - 1

        elif key == curses.KEY_DOWN or key == 106:
            if current_row < menu_len - 1:
                current_row += 1
            else:
                current_row = 0

        elif key == 113:
            return

        elif key == curses.KEY_ENTER or key in [10, 13]:
            main_window.clear()
            main_window.addstr(current_row, 10, "enter")
            main_window.refresh()
            sleep(2)
            return

        print_menu(main_window, current_row)

curses.wrapper(main)
