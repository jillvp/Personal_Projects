import os
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
from mutagen.mp3 import MP3
from pygame import mixer # use pygame to play music - import mixer class => responsible for audio + sound effects

root = Tk()

# Create the menubar (top bar)

menubar = Menu(root)            # create empty menu
root.config(menu=menubar)            # configuring menubar: 1. bar needs to be at the TOP + 2. get ready to receive submenus

# Create the submenu (drop down menu from top bar)

subMenu = Menu(menubar)


def browse_file():
    global filename             # create global variable of filename, so you can use it's value in play_music
    filename = filedialog.askopenfilename()


menubar.add_cascade(label="File", menu=subMenu) # dropdown menus = cascade menu. add 'File'
subMenu.add_command(label="Open", command = browse_file)
subMenu.add_command(label="Exit", command = root.destroy)   # will destroy root = Tk() window.


def about_us():
    tkinter.messagebox.showinfo('About SpaceWave', 'This is a music player build using Python Tkinter by @jillvp')
    # 'title of the messagebox window', 'information you want to display'


subMenu = Menu(menubar)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About Us", command = about_us)


mixer.init()  # initializing the mixer !

root.title("SpaceWave")
root.iconbitmap(r'images/data77_k4a_icon.ico')

filelabel = Label(root, text='SpaceWave Sound Wave Player!')
filelabel.pack(pady=10)

lengthlabel = Label(root, text='Total Length - --:--')
lengthlabel.pack()


def show_details():
    filelabel['text'] = "Playing" + ' - ' + os.path.basename(filename)

    file_data = os.path.splitext(filename)

    if file_data[1] == '.mp3':
        audio = MP3(filename)
        total_length = audio.info.length
    else:
        a = mixer.Sound(filename)
        total_length = a.get_length()

    # div - total_length / 60, mod - total_length % 60
    mins, secs = divmod(total_length, 60)
    mins = round(mins)
    secs = round(secs)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    lengthlabel['text'] = "Total Length" + ' - ' + timeformat



def play_music():
    """first load the file,
    then play the file """
    global paused

    if paused:
        mixer.music.unpause()
        statusbar['text'] = "Music Resumed"
        paused = FALSE
    else:
        try:
            mixer.music.load(filename)
            mixer.music.play()
            statusbar['text'] = "Playing music" + ' - ' + os.path.basename(filename)
            show_details()
        except:
            tkinter.messagebox.showerror('File not found', 'SpaceWave could not find the file. Please Check Again.')


def stop_music():
    mixer.music.stop()
    statusbar['text'] = "Music Stopped"

paused = FALSE

def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusbar['text'] = "Music Paused"


def rewind_music():
    play_music()
    statusbar['text'] = "Music Rewinded"


def set_vol(val):
    volume = int(val) / 100             # first convert it from a string into an int / 100 !
    mixer.music.set_volume(volume)
    # set_volume of mixer takes value only from 0 to 1. Example - 0, 0.1,0.55,0.54.0.99,1



muted = FALSE


def mute_music():
    global muted
    if muted:   # unmute the music
        mixer.music.set_volume(0.7)
        VolumeBtn.configure(image=VolumePhoto)
        scale.set(70)
        muted = FALSE
    else:       # mute the music
        mixer.music.set_volume(0)
        VolumeBtn.configure(image=MutePhoto)
        scale.set(0)
        muted = TRUE

middleframe = Frame(root)
middleframe.pack(pady=30, padx=30)

PlayPhoto = PhotoImage(file='images/play-3-128.png') # convert image into a button
PlayBtn = Button(middleframe, image=PlayPhoto, command=play_music) # add button
PlayBtn.grid(row=0, column=0, padx=10)


StopPhoto = PhotoImage(file='images/stop128.png')
StopBtn = Button(middleframe, image=StopPhoto, command=stop_music)
StopBtn.grid(row=0, column=1, padx=10)

PausePhoto = PhotoImage(file='images/pink-pause-128.png')
PauseBtn = Button(middleframe, image=PausePhoto, command=pause_music)
PauseBtn.grid(row=0, column=2, padx=10)


# Bottom frame for volume, rewind, mute etc.
bottomframe = Frame(root)
bottomframe.pack()

RewindPhoto = PhotoImage(file='images/rewind64.png')
RewindBtn = Button(bottomframe, image=RewindPhoto, command=rewind_music)
RewindBtn.grid(row=0, column=0)

MutePhoto = PhotoImage(file='images/mute64.png')
VolumePhoto = PhotoImage(file='images/volume64.png')
VolumeBtn = Button(bottomframe, image=VolumePhoto, command=mute_music)
VolumeBtn.grid(row=0, column=1)

scale = Scale(bottomframe, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(70)
mixer.music.set_volume(0.7)# set initial volume AUTOMATICALLY to 70
scale.grid(row=0, column=2, pady=15, padx=30)


statusbar = Label(root, text="Welcome to SpaceWave", relief = SUNKEN, anchor = W)   # creates border + anchor to West (left) side
statusbar.pack(side=BOTTOM, fill = X)   # add to bottom + fill x-as.

# root['bg'] = 'black'  
# TO DO: change background color of image buttons

root.mainloop()
