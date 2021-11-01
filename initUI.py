from tkinter import *
from tkinter import filedialog
import configparser
import ctypes
import os

# setting tkinter main window size
winwidth = 500
winheight = 450
user = ctypes.windll.user32
# SETTING
# GetSystemMetrics grabs the screen size, set winwidth and winheight to the window size you'd like, w and h return the right x and y locations for the window
w = int(user.GetSystemMetrics(0)/2 - winwidth/2)
h = int(user.GetSystemMetrics(1)/2 - winheight/2)

# tkinter main window creation
root = Tk()
root.title('Atari AI Team Project')
root.iconbitmap('resources/images/atarilogo.ico')


root.geometry(f'{winwidth}x{winheight}+{w}+{h}')

# used by romlist()


def romSearch(conf):
    count = 0
    filearray = []
    for file in os.listdir(conf):
        if file.endswith(".A26") or file.endswith(".bin"):
            gamename = file.split('.')
            filearray.append(gamename[0])
    return filearray

# use to initialize the main window listbox


def romList():
    l = Listbox(root)
    config = configparser.ConfigParser(allow_no_value=True)
    config.read('config/config.ini')
    if config['SETTINGS']['RomDirectory'] != '':
        roms = romSearch(config['SETTINGS']['ROMDirectory'])
        l.config(height=len(roms))
        i = 0
        while i < len(roms):
            l.insert(i, roms[i])
            i += 1
    else:
        romfolder = filedialog.askdirectory(title='Please Select a ROM folder')
        config.set('SETTINGS', 'RomDirectory', romfolder)
        with open('config/config.ini', 'w') as configfile:
            config.write(configfile)
        romList()
    return l


# create ROM list box
lb = romList()
lb.pack(side=LEFT)

# button logic


def playButton(listbox):
    # no logic yet
    print("no play logic yet")
def quit():
    print("no quit logic yet")

# create BUTTON
playbutton = Button(root, text='Play', font=("Helvetica", 18, "bold"))
playbutton.pack(side=RIGHT)
playbutton['command'] = lambda arg1= lb : playButton(lb) #used lambda to properly call commands with arguments on click
quitbutton = Button(root, text = 'Quit',command = quit,font =("helvetica",18,"bold"))
quitbutton.pack(side = RIGHT)


#
root.mainloop()
