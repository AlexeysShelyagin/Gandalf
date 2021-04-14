import keyboard

for i in range(150):
    keyboard.block_key(i)

keyboard.unblock_key(33)

while True:
    None
