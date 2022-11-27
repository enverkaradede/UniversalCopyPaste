import pyperclip
from PIL import Image, ImageGrab
import io

class Clipboard:
    def __init__(self):
        self._clipboard = pyperclip
        self._grabImage = ImageGrab
        self._waitTime = 5
        self._text = None
        self._image = None
        self._copiedData = None

    def setWaitTime(self, wait_time):
        self._waitTime = wait_time

    def getWaitTime(self):
        return self._waitTime

    def _setText(self, text):
        self._text = text

    def _getText(self):
        return self._text
    
    def _copyText(self):
        self._clipboard.copy(self._text)
    
    def _pasteText(self):
        return self._clipboard.paste()

    def _setImage(self, image):
        self._image = image

    def _getImage(self):
        return self._image

    def waitBeforePaste(self):
        self._clipboard.waitForPaste(self._waitTime)

    def _pasteImage(self):
        self._image = ImageGrab.grabclipboard()

    def setCopiedData(self, copiedData):
        self._copiedData = copiedData

    def getCopiedData(self):
        return self._copiedData

    def checkIfTextOrImage(self):
        if isinstance(self._clipboard.paste(), str):
            return 'text'
        elif isinstance(self._grabImage.grabclipboard(), Image.Image):
            return 'image'

    def copyTextOrImage(self):
        if isinstance(self._clipboard.paste(), str):
            self._setText(self._clipboard.paste())
            return self._text
        elif isinstance(self._grabImage.grabclipboard(), Image.Image):
            #! Image Copy function hits error while converting to bytes.
            # TODO: Fix it
            self._setImage(self._grabImage.grabclipboard())
            buf = io.BytesIO()
            self._getImage().save(buf, format="JPEG")
            buf.seek(0)
            self._setImage(buf.read())
            return self._image