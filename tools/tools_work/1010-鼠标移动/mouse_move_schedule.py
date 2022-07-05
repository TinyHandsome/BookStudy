import pyautogui
from random import randint
import random
import time

def get_random_loc():
    return randint(1, 1000)

def get_current_loc():
    return pyautogui.position()
    
def greedy(epsilon=0.8):
    if random.random() > epsilon:
        return True
    
    return False

flag = True
while flag:
    if greedy():
        pyautogui.click(10, 1070, clicks=1)
    else:
        pyautogui.moveTo(get_random_loc(), get_random_loc(), duration=0.3)
    time.sleep(2)
    
    x, y = get_current_loc()
    if x > 1000:
        flag=False

