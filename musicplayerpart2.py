#import modules
import pygame
import tkinter as tkr
#to read all the playli
import os
#Create a window
player = tkr.Tk()

#edit the window
player.title("Audio Playa")
player.geometry("205x340")

#Getsong, it only plays certain song extentions
file = "Song.mp3"

#Pygame Inits
pygame.init()
pygame.mixer.init()

#Action event, loaded the song in the function
def Play():
    
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    
#create a functions so that we can stop song anytime we want
def ExitPlayer():
    pygame.mixer.music.stop()
    
#Register buttons, play and stop buttons
button1 =tkr.Button(player, width = 5, height = 3, text = "PLAY THAT SONG!", command = Play)
button2 =tkr.Button(player, width = 5, height = 3, text = "STOP", command = ExitPlayer)


#Song Name we need to create something that would show us what song is playing

#crete the text that says the name of the song
contents1 =tkr.Label(label1, text = file)


#place widgets
button1.pack(fill = "x")
button2.pack(fill = "x")
contents1.pack()

#Activate , this will make it run
player.mainloop()

#Create our actions, where are songs and modules come into play


