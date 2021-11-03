from tkinter import *
from tkinter import filedialog
import configparser
import ctypes
import os
import main
from multiprocessing import Process
from subprocess import Popen
import time

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




def programSearch():
    config = configparser.ConfigParser(allow_no_value=True)
    if not os.path.exists('config/config.ini'):
        config['SETTINGS'] = {'stelladirectory': '', 'romdirectory': ''}
        with open('config/config.ini', 'w') as configfile:
            config.write(configfile)
    config.read('config/config.ini')
    if not config['SETTINGS']['stelladirectory'].endswith('Stella.exe'):
        stelladirectory = filedialog.askdirectory(title='Please locate your Stella directory')
        config.set('SETTINGS', 'stelladirectory', stelladirectory + '/Stella.exe')
        with open('config/config.ini', 'w') as configfile:
            config.write(configfile)
        programSearch()




    

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
    if config['SETTINGS']['romdirectory'] != '':
        try:
            roms = romSearch(config['SETTINGS']['ROMDirectory'])
            l.config(height=len(roms))
            i = 0
            while i < len(roms):
                l.insert(i, roms[i])
                i += 1
        except:
            config.set('SETTINGS', 'romdirectory', '')
            with open('config/config.ini', 'w') as configfile:
                config.write(configfile)
            romList()
    else:
        romfolder = filedialog.askdirectory(title='Please Select a ROM folder')
        config.set('SETTINGS', 'romdirectory', romfolder)
        with open('config/config.ini', 'w') as configfile:
            config.write(configfile)
        romList()
        try:
            roms = romSearch(config['SETTINGS']['ROMDirectory'])
            l.config(height=len(roms))
            i = 0
            while i < len(roms):
                l.insert(i, roms[i])
                i += 1
        except:
            romList()
    return l

programSearch()
# create ROM list box
lb = romList()
lb.pack(side=LEFT)

# button logic


def playButton(listbox):
    p = None;
    config = configparser.ConfigParser(allow_no_value=True)
    config.read('config/config.ini')

    romFolder = config['SETTINGS']['romdirectory']
    programFolder = config['SETTINGS']['stelladirectory']
    fileNameA26 = "/" + lb.get(ACTIVE) + ".A26"
    fileNameBin = "/" + lb.get(ACTIVE) + ".bin"
    romStringA26 = f'"{romFolder}/{lb.get(ACTIVE)}.A26"'
    romStringBin = f'"{romFolder}/{lb.get(ACTIVE)}.bin"'
    programFolder = f'"{programFolder}"'

    # no logic yet

    
    print(f'"{programFolder}" "{romFolder + fileNameA26}"-checking')

    try: 
        
        #p = Popen(f'"{programFolder} {romStringA26}"', shell=False, stdin=None, stdout=None, stderr=None, close_fds=True)
        p = os.system(f'"{programFolder} {romStringA26}"')
    except:
            
        #p = Popen(f'"{programFolder} {romStringBin}"', shell=False, stdin=None, stdout=None, stderr=None, close_fds=True)
        p = os.system(f'"{programFolder} {romStringBin}"')

    #global mainmethodProcess
    #mainmethodProcess = Process(target=main.main())
    #mainmethodProcess.start()

    time.sleep(3)
    main.main()


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
