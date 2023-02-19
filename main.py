# Importar clases
from Clases.InputComandos import ComandosI
from Clases.Speechmodule import SpeechModule
from Clases.VoiceRecognitionModule import VoiceRecognitionModule

# Librerias necesarias
import time
import tkinter as tk
from tkinter import*
import threading
from PIL import Image,ImageTk

# Variables de uso
usu="seicros"
usu1="SeicroS"
no="Funcion en desarrollo"
name = "limbo"
name0="Limbo"
name1="L1MB0"

# Microfono
index=0
# Tiempo de escucha
times=5

# Declaracion de clases
speech = SpeechModule()
recognition = VoiceRecognitionModule()
comando= ComandosI()
text="ejecuta deteccion"
comando.comando(text,index,times)
# Funcion de actualizar la pantalla
def actualizar():
    raiz.update()
    time.sleep(1)

# Funcion central de funcionamiento
def stars():
    while True:
        state.set("ON")
        times=10
        L.set("*" + name1 + " escuchando")
        print("*" + name1 + " escuchando")
        text = recognition.recognize(index,times)
        if text:
            if name in text or name0 in text:
                speech.talk("Si, " + usu)
                print("*" + name1 + " En comandos")
                L.set("*" + name1 + " En comandos")
                comando.comando(text,index,times)
            else:
                print("*" + name1 + " En comandos")
                L.set("*" + name1 + " En comandos")
                comando.comando(text,index,times)

# Funcion de incio de scripts
def star1():
    speech.talk("Iniciando, " + usu)
    stars()

# Estructura de la interfaz grafica
raiz=Tk()
raiz.title("L1MB0")
raiz.resizable(0,0)
raiz.config(bg="black")
raiz.iconbitmap("1.ico")

state=StringVar()
state.set("OFF")
L=StringVar()
L.set("*ZZZ")

# Carga el gif animado
image = Image.open("n1.gif")
frames = []
for i in range(image.n_frames):
    image.seek(i)
    frames.append(ImageTk.PhotoImage(image.copy()))

# Crea un widget Canvas y coloca el gif animado en el fondo
canvas = tk.Canvas(raiz, width=image.width, height=image.height)
background = canvas.create_image(0, 0, image=frames[0], anchor=tk.NW)
canvas.pack()

# Actualiza el frame del gif cada 100 milisegundos
frame_number = 0

def update_frame():
    global frame_number
    frame_number = (frame_number + 1) % len(frames)
    canvas.itemconfigure(background, image=frames[frame_number])
    raiz.after(100, update_frame)

# Declarando hilos
thread1 = threading.Thread(target=actualizar)
thread2 = threading.Thread(target=star1)

etiqueta = tk.Label(raiz, textvariable=state, bg="black", fg="white",font=("",50))
etiqueta.place(x=210,y=160)
etiqueta1 = tk.Label(raiz, textvariable=L, bg="black", fg="white",font=("",35), bd=0)
etiqueta1.place(x=0, y=0)

boton=tk.Button(raiz, text="Iniciar", command=thread2.start, width=9, height=2, bg="red", fg="black",font=("",20)).place(x=180, y=300)

thread1.start()
raiz.after(100, update_frame)
raiz.mainloop()