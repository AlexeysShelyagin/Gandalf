import keyboard
import win32api, win32con
import time

F_KEY = 33                          #This key wan't be blocked for fullscreen mode

print('Please stand by')            #Stand by window)

for i in range(150):                #Keyboard blocking
    keyboard.block_key(i)
keyboard.unblock_key(F_KEY)

while True:
    win32api.SetCursorPos( (0, int(win32api.GetSystemMetrics(1) / 2)) )     #Cursor goes to half screen height and left side
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)              #Disabled mouse buttons holding, it cause bugs
    #win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    time.sleep(0.005)                                                       #Important delay, it will lag without it