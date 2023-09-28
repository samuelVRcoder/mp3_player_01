import PySimpleGUI as sg

import pygame

import os

from tkinter import messagebox as msg

layout = [
[sg.Combo([files for files in os.listdir(".") if files.endswith(".mp3")] ,key = "ei", size = (30,1)) ],
[sg.Button("Play")]

    ]

janela = sg.Window("Lista Sons", layout = layout)

while True:
            
        
            eventos, valores = janela.read()
            

            if eventos == sg.WIN_CLOSED:
                break
                exit()
            elif eventos == "Play":
                try:
                
                
                    pygame.init()
                    pygame.mixer.music.load(valores["ei"])
                    pygame.mixer.music.play()
                    msg.showinfo("Tocando...", "Tocando...")
                except:
                    msg.showerror("erro","algo deu errado")
            else:
                break
                exit()
                
                
            
            
    
