from pynput.mouse import Controller # type: ignore
from pynput.keyboard import Controller # type: ignore

def controlmouse():
    mouse=Controller()
    mouse.position=(10,20)# left to right from top of the bottom

controlmouse()

def controlkeyboard():
    keyboard=Controller()
    keyboard.type("I am freaking awesome")

controlkeyboard()   
