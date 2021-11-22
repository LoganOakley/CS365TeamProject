from DirectKeyInputs import ReleaseKey, PressKey, LEFT, RIGHT, UP, DOWN, SPACE
import time

for i in range(2):
    print(2-i)
    time.sleep(i)

print("up")
PressKey(UP)
time.sleep(.1)
ReleaseKey(UP)
print("down")
PressKey(DOWN)
time.sleep(.1)
ReleaseKey(DOWN)
print("left")
PressKey(LEFT)
time.sleep(.1)
ReleaseKey(LEFT)
print("right")
PressKey(RIGHT)
time.sleep(.1)
ReleaseKey(RIGHT)
print('space')
PressKey(SPACE)
time.sleep(.1)
ReleaseKey(SPACE)