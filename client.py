import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from playsound import playsound
import pygame
from pygame import mixer
import os
import time
import ntpath


song_counter = 0
song_selected = None

SERVER = None
PORT = 8050
IP_ADDRESS = '127.0.0.1'
BUFFER_SIZE = 4096

selectSongLabel = None
listbox = None
playButton = None
stopButton = None
uploadButton = None
downloadButton = None
infoLabel = None

def stop():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()
    infoLabel.configure(text = "")

def play():
    global song_selected
    
    song_selected = listbox.get(ANCHOR)

    pygame
    mixer.init()
    mixer.music.load('shared_files/' + song_selected)
    mixer.music.play()
    if(song_selected != ""):
        infoLabel.configure(text = "Now Playing: " + song_selected)
    else:
        infoLabel.configure(text="")


def musicWindow():    
    window = Tk()
    window.title('MUSIC WINDOW')
    window.geometry("300x300")
    window.configure(bg="black")

    global selectSongLabel
    global listBox
    global playButton
    global stopButton
    global uploadButton
    global downloadButton
    global infoLabel
    global song_counter

    selectSongLabel = Label(window, text = "Select Song", bg = 'white', font = ('Calibri', 8))
    selectSongLabel.place(x=120,y=1)

    listBox = Listbox(window, height = 10, width = 39, activestyle="dotbox",bg = "LightSkyBlue", borderwidth=2, font = ("Calibri", 10))
    listBox.place(x=10,y=18)

    for file in os.listdir('shared_files'):
        filename = os.fsdecode(file)
        listbox.insert(song_counter, filename)
        song_counter = song_counter + 1

    scrollBar1 = Scrollbar(listBox)
    scrollBar1.place(relheight = 1,relx=1)
    scrollBar1.config(command = listBox.yview)

    playButton = Button(window, text = "Play", width = 10, bd = 1, bg = "purple", font = ("Calibri", 10),command = play)
    playButton.place(x=30,y=200)

    stopButton = Button(window, text = "Stop", bd = 1, width = 10, bg = "red", font = ("Calibri",10), command = stop)
    stopButton.place(x=200,y=200)

    uploadButton = Button(window, text = "Upload", width = 10, bd = 1, bg = "yellow", font = ("Calibri", 10))
    uploadButton.place(x=30,y=250)

    downloadButton = Button(window, text = "Download", bd = 1, width = 10,bg = "green", font = ("Calibri",10))
    downloadButton.place(x=200,y=250)

    infoLabel = Label(window, text = "", fg = "blue", font = ("Calibri",8))
    infoLabel.place(x=4,y=280)

    window.mainloop()

def setup():

    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS,PORT))

    musicWindow()

setup()
