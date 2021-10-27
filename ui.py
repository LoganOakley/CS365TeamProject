from tkinter import *
import configparser
import ctypes

root = Tk();
root.title('Atari AI Team Project')
root.iconbitmap('resources/images/atarilogo.ico')
#getting window size'
winwidth = 500
winheight = 450
user = ctypes.windll.user32
# GetSystemMetrics grabs the screen size, set winwidth and winheight to the window size you'd like, w and h return the right x and y locations for the window
w = int(user.GetSystemMetrics(0)/2 - winwidth/2)
h = int(user.GetSystemMetrics(1)/2 - winheight/2)

root.geometry(f'{winwidth}x{winheight}+{w}+{h}')

#
root.mainloop()