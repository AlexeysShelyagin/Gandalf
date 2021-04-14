import keyboard
import win32api, win32con
import time

F_KEY = 33

print('Please stand by')

for i in range(150):
    keyboard.block_key(i)
keyboard.unblock_key(F_KEY)

while True:
#    None
    win32api.SetCursorPos( (0, int(win32api.GetSystemMetrics(1) / 2)) )
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    #win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    time.sleep(0.005)