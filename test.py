import os
import curses

def loetleFailid(path="."):
    sisu = os.listdir(path)
    x = ""
    for a in sisu:
        x += a.strip("\n") + " "
    print(x)
    return x

screen = curses.initscr()
x = loetleFailid()
screen.addstr(0,0,x)

loetleFailid()
screen.refresh()
curses.napms(2000)
curses.endwin()