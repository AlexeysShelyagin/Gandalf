from ctypes import *
import time

ok = windll.user32.BlockInput(True) #enable block

time.sleep(10)

ok = windll.user32.BlockInput(False) #disable block 
