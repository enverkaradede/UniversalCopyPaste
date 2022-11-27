from pynput import keyboard

class Keyboard:
    def __init__(self):
        self._key = None

    def setKey(self, key):
        self._key = key

    def getKey(self):
        return self._key

    def __onActivate(self):
        # TODO: Add send content copied functionality
        import clipboard
        cp = clipboard.Clipboard()

        print(cp.checkIfTextOrImage())
        msg = cp.copyTextOrImage()
        cp.setCopiedData(msg)
        print(f'COPIED DATA --> {cp.getCopiedData()}')
        cp.setWaitTime(5)
        # msg = cp.PasteText()
        # print(f'COPIED DATA --> {msg}')
        # msg = cp.CopyImage()
        # print(f'COPIED DATA --> {msg}')

        import sender

        s = sender.TCPSender()
        s.setHost('127.0.0.1')
        s.setPort(12345)
        s.connectSocket()
        s.setData(msg)
        s.sendCopiedTextToDevice()
        s.receiveResponse()
        s.closeSocket()

        # print("Add copy function")

    def __onExit(self):
        print('Exit combination is detected. Exiting from key logger.')
        exit(1)

    def listen(self):
        with keyboard.GlobalHotKeys({
            '<ctrl>+<alt>+c': self.__onActivate,
            '<ctrl>+<alt>+x': self.__onExit}) as listener:
            listener.join()

    def __getKeycode(self):
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

        return switcher.get(self._key, self._key)

    def TestKey(self):
        return self.__getKeycode()