import os
import eel

from engine.features import *
from engine.command import *
import eel

def ui(text):
    try:
        eel.showOnUI(text)
    except:
        pass

def start():
    eel.init("www")
    playAssistantSound()
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    eel.start('index.html', mode=None, host ='localhost', block = True)
