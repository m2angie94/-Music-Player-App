# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 17:59:55 2020

@author: m2ang
"""

#import modules
import pygame
import tkinter as tkr

#Create a window
player = tkr.Tk()

#edit the window
player.title("Audio Playa")
player.geometry("205x340")

#Getsong, it only plays certain song extentions
#Getsong, it only plays certain song extentions
user_input = input("Enter the name of the song you want to play: ")
user_input2 = user_input + ".mp3"
print("Okay! \nNow playing-------> " + user_input + "!")
file = user_input2

#Action event, loaded the song in the function
def Play():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    
#create a functions so that we can stop song anytime we want
def ExitPlayer():
    pygame.mixer.music.stop()
    
#Register buttons, play and stop buttons
button1 =tkr.Button(player, width = 5, height = 3, text = "PLAY THAT SONG!", bg='#ffb3fe', command = Play)
button1.pack(fill = "x")
button2 =tkr.Button(player, width = 5, height = 3, text = "STOP", bg='Red', command = ExitPlayer)
button2.pack(fill = "x")

#Song Name we need to create something that would show us what song is playing
label1 = tkr.LabelFrame(player, text = "Song Name")
label1.pack(fill = "both", expand = "yes")
#crete the text that says the name of the song
contents1 =tkr.Label(label1, text = file)
contents1.pack()

#Activate , this will make it run
player.mainloop()

#Create our actions, where are songs and modules come into play


