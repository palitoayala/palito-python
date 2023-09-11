from tkinter import *
from tkinter.ttk import *
from reproductor import *

musica = Reproductor('musica.mp3')

def play_musica():
    musica.volumen(0.8)
    musica.play()

def pause_musica():
    musica.pause()


master = Tk()
master.geometry("200x200")


label = Label(master,text="Reproductor de música")

label.pack(pady=10)

btn_play = Button(master, text="Reproducir", command= play_musica)
btn_play.pack(pady=10)
btn_pause =Button(master, text="Pausar", command= pause_musica)
btn_pause.pack(pady=20)

mainloop()