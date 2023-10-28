import keyboard
import mouse
import time

Right = mouse.right_click
Left = mouse.click
Scroll = mouse.wheel
Move = mouse.move

while True:
    if keyboard.is_pressed("1"):
        Right()
        time.sleep(0.1)
    if keyboard.is_pressed("4"):
        Left()
        time.sleep(0.1)
    if keyboard.is_pressed("2"):
        Scroll(1)
        time.sleep(0.1)
    if keyboard.is_pressed("3"):
        Scroll(-1)
        time.sleep(0.1)
    if keyboard.is_pressed("9"):
        break
    if keyboard.is_pressed("5"):
        Move(0,1,absolute=False,duration=0)
        time.sleep(0.01)
    if keyboard.is_pressed("6"):
        Move(0,-1,absolute=False,duration=0)
        time.sleep(0.01)
    if keyboard.is_pressed("7"):
        Move(1,0,absolute=False,duration=0)
        time.sleep(0.01)
    if keyboard.is_pressed("8"):
        Move(-1,0,absolute=False,duration=0)
        time.sleep(0.01)
