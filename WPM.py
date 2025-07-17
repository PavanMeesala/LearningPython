# must be run through the terminal

import curses
import time
from curses import wrapper
import time
import random
def start_screen(stdscr):
    stdscr.clear()
    # stdscr.addstr("Hello world! ",curses.color_pair(2))
    stdscr.addstr("Welcome to the Speed Typing Test!")  # (0,2,"hello") position row, column
    stdscr.addstr("\nPress any key to befgin!")
    stdscr.refresh()
    key = stdscr.getkey()
def display_text(stdscr,target_text, current_text,wpm = 0):
    stdscr.addstr(target_text)
    stdscr.addstr(1,0,f"WPM:{wpm}")

    for i,char in enumerate(current_text):
        current_char = target_text[i]
        color = curses.color_pair(1)
        if char != current_char:
            color = curses.color_pair(2)
        stdscr.addstr(0, i ,char, color)
def load_text():
    with open('wpm.txt','r') as f:
        lines = f.readlines()
        return random.choice(lines).strip()  #strip() removes white space character like \n

def wpm_test(stdscr):
    target_text = load_text()#"Hello world this is some test text for this app!"
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time,1)
        wpm = round((len(current_text) / (time_elapsed/60)) / 5)
        stdscr.clear()
        display_text(stdscr,target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()  #print(repr(key))
        except:
            continue


        if key == '\x1b':  # for escape key repr(key) = "\x1b"
            break
        if key in ("KEY_BACKSPACE","\b","\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)



def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN, curses.COLOR_BLACK)  # ID, foreground, background
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_BLACK)
    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2,0,"You completed the text! Press any key to continue.....")
        key = stdscr.getkey()

        if key == '\x1b':
            break

wrapper(main)