import keyboard

f = open('Rec.txt', 'w')

recorded = keyboard.record(until='esc')

for i in recorded:
    f.write(str(i) + '\n')