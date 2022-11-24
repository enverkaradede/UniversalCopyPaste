from pynput import keyboard

class Keyboard:
    def __init__(self):
        self.key = None

    def SetKey(self, key):
        self.key = key

    def GetKey(self):
        return self.key

    def __on_activate(self):
        # TODO: Add send content copied functionality
        print("Add copy function")

    def __on_exit(self):
        print('Exit combination is detected. Exiting from key logger.')
        exit(1)

    def listen(self):
        with keyboard.GlobalHotKeys({
            '<ctrl>+<alt>+c': self.__on_activate,
            '<ctrl>+<alt>+x': self.__on_exit}) as listener:
            listener.join()

    def __GetKeycode(self):
        switcher = {
            "ctrl": keyboard.Key.ctrl,
            "ctrl_l": keyboard.Key.ctrl_l,
            "ctrl_r": keyboard.Key.ctrl_r,
            "shift": keyboard.Key.shift,
            "shift_l": keyboard.Key.shift_l,
            "shift_r": keyboard.Key.shift_r,
            "alt": keyboard.Key.alt,
            "alt_gr": keyboard.Key.alt_gr,
            "alt_l": keyboard.Key.alt_l,
            "alt_r": keyboard.Key.alt_r,
            "cmd": keyboard.Key.cmd,
            "cmd_l": keyboard.Key.cmd_l,
            "cmd_r": keyboard.Key.cmd_r,
            "esc": keyboard.Key.esc,
            "enter": keyboard.Key.enter,
            "space": keyboard.Key.space,
            "backspace": keyboard.Key.backspace,
            "del": keyboard.Key.delete,
            "home": keyboard.Key.home,
            "end": keyboard.Key.end,
            "up": keyboard.Key.up,
            "down": keyboard.Key.down,
            "left": keyboard.Key.left,
            "right": keyboard.Key.right,
        }

        return switcher.get(self.key, self.key)

    def TestKey(self):
        return self.__GetKeycode()