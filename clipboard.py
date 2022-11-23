import pyperclip

class Clipboard:
    def __init__(self):
        self.clipboard = pyperclip
        self.wait_time = 5
        self.text = None

    def SetWaitTime(self, wait_time):
        self.wait_time = wait_time

    def GetWaitTime(self):
        return self.wait_time

    def SetText(self, text):
        self.text = text

    def GetText(self):
        return self.text
    
    def CopyText(self):
        self.clipboard.copy(self.text)
    
    def PasteText(self):
        return self.clipboard.paste()

    def WaitBeforePaste(self):
        self.clipboard.waitForPaste(self.wait_time)