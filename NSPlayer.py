# Name of the Project : NSPlayer.py
# Written by NoobScience : https://github.com/newtoallofthis123
# Website : https://newtoallofthis123.github.io/NSPlayer
# Repository : https://github.com/newtoallofthis123/NSPlayer
# Modules Used : pyperclip, pyshorteners, tkinter
#Installation of modules: pip install pyperclip, pip install pyshorteners

'''
NSPlayer is a simple music player. It can play any audio file.
This is a simple music player with a minimal interface and takes up very less system resources.
This comes in the form of a one file executable, an executable with dependencies you can install and a python file.
You can find all of these at https://github.com/newtoallofthis123/NSPlayer/releases
To use the python file, just switch to the directory you stored it in and open the terminal there and type "python NSPlayer.py"
Available for Windows, Mac, Linux and written in python
By NoobScience.
 '''

#! /usr/bin/env python3

print("NSPlayer is a simple music player. It can play any audio file. This is a simple music player with a minimal interface and takes up very less system resources.This comes in the form of a one file executable, an executable with dependencies you can install and a python file. You can find all of these at https://github.com/newtoallofthis123/NSPlayer/releases. To use the python file, just switch to the directory you stored it in and open the terminal there and type python NSPlayer.py . Available for Windows, Mac, Linux and written in python. By NoobScience.")

# Import the Necessary Modules
import os
from tkinter.filedialog import askdirectory

# pygame is used in this program, you can install it by using pip install pygame
import pygame

# We will be using mtagrn.id3 also
from mutagen.id3 import ID3

# We will be using tkinter to build the gui
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.messagebox import askquestion
import tkinter.messagebox

# We will use the web Browser to open the web browser
import webbrowser

# Building the GUI
gui = Tk()
gui.minsize(546,580)
gui.configure(bg="#002240")
gui.title("NSPlayer")
gui.geometry('500x500')
gui.resizable(False,False)

# If you encounter error, change the path of the file in the comments and uncomment it to have a file icon (Remove the three quotes)

photo = PhotoImage(file = "pygame/NSPlayer.png")
gui.iconphoto(False, photo)




# Listing and reading names of the songs
listofsongs = []
realnames = []

# Defining a variable to hold song name
v = StringVar()
songlabel = Label(gui,textvariable=v,width=72, bg="#002240", fg="white", font=('Cascadia Code', 14))

# Song Indexing
index = 0

# Function to choose directory
def directorychooser():

    directory = askdirectory()
    os.chdir(directory)

# Types of files to import, change after comment to add more type of audio files
    for files in os.listdir(directory):
        if files.endswith(".mp3"):

# Files
            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            realnames.append(audio['TIT2'].text[0])


            listofsongs.append(files)

# Intiating pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    #pygame.mixer.music.play()

# Calling upon the directorychooser function
directorychooser()

# To update song labels
def updatelabel():
    global index
    global songname
    v.set(realnames[index])
    #return songname


# To get Next Song
def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

# To get Previous Song
def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

# To stop the song
def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")
    #return songname

# To Play Song in order
def playsong(event):
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    v.set("")
    updatelabel()

# To pause Song
def pausesong(event):
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.pause()
    v.set("")
    updatelabel()

# To unpause Song
def unpausesong(event):
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.unpause()
    v.set("")
    updatelabel()

# To rewind the Song
def rewindsong(event):
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.rewind()
    v.set("")
    updatelabel()

# To open a pop up window containing info
def NS_info(event):
    tkinter.messagebox.showinfo('About NoobScience', NS_text)
    webbrowser.open('https://newtoallofthis123.github.io/About')


# To ask if the user wants to visit the NSPlayer Website
def NS_title():
   result = tkinter.messagebox.askquestion('Fork', 'Do you want to go the NSPlayer Website?')
   if result=='yes':
       webbrowser.open('https://newtoallofthis123.github.io/NSPlayer')
   else:
        print("Okay")

        
# The Text Pop up box info
NS_text = "This Project is built by NoobScience using python and pygame. This is a beginner-friendly project and you can use this to learn pygame as well. This project is registered under MIT lisence (copy right NoobScience 2021), which makes it open-source. You are free to use it however you wish. Check out the code at my repo: https://github.com/newtoallofthis123 , Any issues, be sure to tell me at https://github.com/newtoallofthis123/issues , Check out the website at https://newtoallofthis123.github.io/NSPlayer, To troubleshoot any problems, check out the documentation at the website. Be sure to get pygame from 'pip install pygame'"

    #return songname

# The Title Button
titleButton = Button(gui,text='NSPlayer', bg="#FFE600", fg="#002240", font=("Cascadia Code", 20), command = NS_title)
titleButton.pack(padx=3, pady=12)

# The song list
listbox = Listbox(gui, bg="#002240", fg="white", width="76", font=("Cascadia Code", 12),)
listbox.pack(padx=5, pady=10)

#listofsongs.reverse()
realnames.reverse()

for items in realnames:
    listbox.insert(0,items)

realnames.reverse()
#listofsongs.reverse()

# Play Button
playbutton = Button(gui,text='|> Play Music', font=("Cascadia Code", 12), width=20, bg="#00FFC0")
playbutton.pack()
playbutton.place(x=34, y=330)

# Pause Button
pausebutton = Button(gui,text='|: Pause Music', font=("Cascadia Code", 12), width=20, bg="#00FFC0")
pausebutton.pack()
pausebutton.place(x=34, y=380)

# Unpause Button
unpausebutton = Button(gui,text=':: Unpause Music', font=("Cascadia Code", 12), width=20, bg="#00FFC0")
unpausebutton.pack()
unpausebutton.place(x=300, y=380)

# Rewind Button
rewindbutton = Button(gui,text='0 Rewind Music', font=("Cascadia Code", 12), width=20, bg="#00FFC0")
rewindbutton.pack()
rewindbutton.place(x=34, y=480)

# Next Song Button
nextbutton = Button(gui,text = '--> Next Song', font=("Cascadia Code", 12), width=20, bg="#00FFC0")
nextbutton.pack()
nextbutton.place(x=300, y=430)

# Previous Song Button
previousbutton = Button(gui,text = '<-- Previous Song', font=("Cascadia Code", 12), width=20, bg="#00FFC0")
previousbutton.pack()
previousbutton.place(x=34, y=430)

# Stop Song Button
stopbutton = Button(gui,text='|| Stop Music', font=("Cascadia Code", 12), width=20, bg="#00FFC0")
stopbutton.pack()
stopbutton.place(x=300, y=330)

# Rewind Button
version = Label(gui,text='v.0.1', font=("Cascadia Code", 8), width=20, bg="#00FFC0")
version.pack()
version.place(x=410, y=68)

# Info button
infobutton = Button(gui,text = "By NoobScience", font=("Cascadia Code", 12), width=20, bg="#00FFC0", fg="#002240")
infobutton.pack(padx=1, pady=1)
infobutton.place(x=300, y=480)

# Now Playing text
label = Label(gui, text = "------Now Playing------", font=("Cascadia Code", 12), width=25)
label.pack(pady=10)
label.place(x=144, y=524)

# Defining Button Commands
playbutton.bind("<Button-1>",playsong)
nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)
infobutton.bind("<Button-1>",NS_info)
pausebutton.bind("<Button-1>",pausesong)
unpausebutton.bind("<Button-1>",unpausesong)

# Song playing Name
songlabel.pack()
songlabel.place(x=-124, y=550)












# Loop Through
gui.mainloop()