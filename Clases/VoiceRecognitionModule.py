import speech_recognition as sr

#Reconocimiento
class VoiceRecognitionModule:

    def __init__(self, key=None):

        self.key = key
        self.r = sr.Recognizer()

    def recognize(self,index,times):

        try:
            with sr.Microphone(device_index=index) as source:
                # Reducir el ruido ambiental
                sr.Recognizer().adjust_for_ambient_noise(source)
                audio = self.r.listen(source,timeout=times)

                text = self.r.recognize_google(audio, key=self.key, language="es")
                return text
        except sr.WaitTimeoutError:
            print("")
            return None
        except sr.UnknownValueError:
            print("No se pudo reconocer el texto, reintentando...")
            return None

