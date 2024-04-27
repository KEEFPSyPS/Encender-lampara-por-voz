import pyfirmata
import speech_recognition as sr
import pyttsx3

board = pyfirmata.Arduino('COM6')

cocina = board.get_pin('d:7:o')
baño = board.get_pin('d:6:o')
sala = board.get_pin('d:5:o')
comedor = board.get_pin('d:4:o')

def encender_focos():
    cocina.write(0)
    baño.write(0)
    sala.write(0)
    comedor.write(0)

def apagar_focos():
    cocina.write(1)
    baño.write(1)
    sala.write(1)
    comedor.write(1)

apagar_focos()
    
escuchar = sr.Recognizer()

inicializar = pyttsx3.init()
velocidad_de_voz = 160
inicializar.setProperty('rate', velocidad_de_voz)

nombre = "alexa"

def habla(texto):
    inicializar.say(texto)
    inicializar.runAndWait()

def tomar():
    command = None
    try:
        with sr.Microphone() as voz :
            escuchar.adjust_for_ambient_noise(voz)
            print("Escuchando...")
            voice = escuchar.listen(voz)
            command = escuchar.recognize_google(voice, language='es-ES')
            command = command.lower()
            print(command)
                   
    except Exception as e:
         print(f"Ocurrió un error: {e}")
         pass
    return command

def alexa():
    command = tomar()
    if command is not None:
        if 'enciende la cocina' in command:
            habla("Encendiendo el foco de la cocina")
            cocina.write(0)
        elif 'apaga la cocina' in command:
            habla("Apagando el foco de la cocina")
            cocina.write(1)
        elif 'enciende el baño' in command:
            habla("Encendiendo el foco del baño")
            baño.write(0)
        elif 'apaga el baño' in command:
            habla("Apagando el foco del baño")
            baño.write(1)
        elif 'enciende la sala' in command:
            habla("Encendiendo el foco de la sala")
            sala.write(0)
        elif 'apaga la sala' in command:
            habla("Apagando el foco de la sala")
            sala.write(1)
        elif 'enciende el comedor' in command:
            habla("Encendiendo el foco del comedor")
            comedor.write(0)
        elif 'apaga el comedor' in command:
            habla("Apagando el foco del comedor")
            comedor.write(1)
        elif 'enciende todos los focos' in command:
            habla("Encendiendo todos los focos")
            encender_focos()
        elif 'apaga todos los focos' in command:
            habla("Apagando todos los focos")
            apagar_focos()

while True:
     alexa()