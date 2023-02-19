# Librerias necesarias
import datetime
import os
import subprocess
import webbrowser
from signal import SIGTERM
import pywhatkit as pywhatkit
import wmi as wmi
#import openai
import ctypes
from gevent import subprocess
import cv2
import mediapipe as mp

# Importar clases
from Clases.Speechmodule import SpeechModule
from Clases.VoiceRecognitionModule import VoiceRecognitionModule

# Variables de uso
usu="seicros"
no="Funcion en desarrollo"
name = "limbo"
name1="L1MB0"
name0="Limbo"

recognition = VoiceRecognitionModule()
speech = SpeechModule()

def convertir(text):
    return text.lower()

# Funcion central
class ComandosI:
    def __int__(self,text):
        self.text=text

    def comando(self,text,index,times):
        text = text.replace(name + " ", "")
        text=convertir(text)

        if  "ejecuta" in text:
            if "deteccion" in text:
                ComandosO.ejecuta_deteccion()
            else:
                print("Error de ejecucion")

        elif  "busca" in text:
            ComandosO.busca()

        elif "hora" in text:
            ComandosO.hora()

        elif "reproduce" in text :
            ComandosO.reproduce(text)

        elif "pausa" in text or "despausa" in text:
            ComandosO.pausa_volumen(0xB3)

        elif "volumen" in text or "Volumen" in text:
            if "subir" in text or "aumenta" in text :
                ComandosO.subir_volumen()
            elif "bajar" in text or "reduce" in text :
                ComandosO.bajar_volumen()

        elif "muestrame" in text :
            ComandosO.muestrame(text)

        elif "cierra" in text :
            ComandosO.cierre(text)

        elif "apaga" in text:
            ComandosO.apagado()

        else:
            print("*" + name1 + " No reconocio ningun comando")
            speech.talk("Error de comando")

"""def chatBot(text):#Por ahora no lo voy a usar


    # Petición de respuesta a OpenAI GPT-3
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt= previous_context+text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.8,
    )

    # Imprimir respuesta
    speech.talk(response["choices"][0]["text"])"""

class ComandosO:

    def ejecuta_deteccion():
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose
        # cap = cv2.VideoCapture("video_0002.mp4")
        cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
        with mp_pose.Pose(
                static_image_mode=False) as pose:
            while True:
                ret, frame = cap.read()
                if ret == False:
                    break
                frame = cv2.flip(frame, 1)
                height, width, _ = frame.shape
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = pose.process(frame_rgb)
                if results.pose_landmarks is not None:
                    mp_drawing.draw_landmarks(
                        frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                        mp_drawing.DrawingSpec(color=(128, 0, 250), thickness=2, circle_radius=3),
                        mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2))
                cv2.imshow("Frame", frame)
                if cv2.waitKey(1) & 0xFF == 27:
                    break
        cap.release()
        cv2.destroyAllWindows()

    def busca(text):
        bus = text.replace("busca" + "", "")
        print("*Realizando busquedad.")
        webbrowser.open("https://www.google.com/search?client=opera-gx&q=" + bus)
        speech.talk("Aqui estan los resultado de " + bus + " ," + usu)

    def hora():
        hora = datetime.datetime.now().strftime('%I:%M %p')
        speech.talk("Son las " + hora + ", " + usu)
        print("*Reloj: " + hora)

    def reproduce(text):
        music = text.replace("reproduce" + "", "")
        speech.talk("Reproduciendo ")
        pywhatkit.playonyt(music)

    def pausa_volumen(key_code):
        ctypes.windll.user32.keybd_event(key_code, 0, 0, 0)
        ctypes.windll.user32.keybd_event(key_code, 0, 2, 0)

    # Desarrollo
    def subir_volumen():
        speech.talk(no)

    # Desarrollo
    def bajar_volumen():
        speech.talk(no)

    # Desarrollo
    def muestrame(text):
        text = text.replace("muestrame" + "", "")
        if "bonito" in text or "bonitas" in text:
            folder_path = r"C:\Users\SeicrosS\Desktop\L 02.2\Cosas_Bonitas"
            subprocess.Popen(f'explorer "{folder_path}"')

    def apagado():
        speech.talk("Apagando el ordenador")
        subprocess.run("shutdown -s")

    def cierre(text):
        text = text.replace("cierra" + "", "")
        c = wmi.WMI()
        text = text + ".exec"
        speech.talk("Buscando")
        for process in c.Win32_Process():
            print(process.ProcessId, process.Name)
            if process.Name in text:
                speech.talk("Ejecutando cerrado de " + text + "," + usu)
                print("*Cerrando", process.ProcessId, process.Name)
                os.kill(process.ProcessId, SIGTERM)
                return
        speech.talk("no logre encontrar " + text + " entre procesos")