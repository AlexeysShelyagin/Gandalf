import keyboard
import win32api, win32con

print('Please stand by')

for i in range(150):
    keyboard.block_key(i)

while True:
#    None
    win32api.SetCursorPos( (0, int(win32api.GetSystemMetrics(1) / 2)) )
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)