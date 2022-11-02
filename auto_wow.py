import pyautogui  as pg
import time
pg.FAILSAFE = True #
import numpy as np

np.random.seed(35)
a = np.random.randint(1,6,400)
# a
b=0


for i in a:
    time.sleep(i)
    pg.click(1105,505+i)
    pg.press('tab')
    time.sleep(1)
    pg.press('q')
    if i <= 3:
        pg.press('tab')
        pg.press('e')
        pg.press('s')

    elif i <= 7:
        pg.press('tab')
        pg.press('q')
    else:
        pg.press('w')
        pg.press('tab')
        pg.press('f')
    time.sleep(i)    
    pg.click(1005,505-i)
    time.sleep(i)

    pg.press('q')
    pg.press('4')
    pg.click(1105,505+i)
    b+=i
    if b >= 55:
        pg.keyDown('shift')    
        pg.press('1')  
        pg.keyUp('shift')