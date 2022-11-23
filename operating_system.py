import platform

class OperatingSystem:
    def __init__(self):
        self.os = platform.system()
    
    def GetOS(self):
        return self.os