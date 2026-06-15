# Importando as bibliotecas
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator

# Configuração
duration = 5 # seconds
sample_rate = 44100 # Hz

# Gravação de áudio
print("Gravando...")

recording = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype='int16'
)
sd.wait()

wav.write('output.wav', sample_rate, recording)
print("Gravação finalizada!! Vou começar o reconhecimento da voz")

# Reconhecendo a voz
recognizer = sr.Recognizer()

with sr.AudioFile("output.wav") as source:
    audio = recognizer.record(source)
    
try:
    text = recognizer.recognize_google(audio, language="pt-BR")
    print("Texto reconhecido: ", text)
except:
    print("Não consegui reconhecer o áudio!")


#Tradução
translator = Translator()

escolha = input("Para qual língua você deseja traduzir a sua fala? Lembre-se inglês=en, espanhol=es, Russo=ru, Português=pt, Indonésio=id, Polonês=pl, Italiano=it,Turco=tr")

translated = translator.translate(text, dest=escolha)  # O 'en' aqui é um código para inglês
print("Tradução para o",escolha, ":", translated.text)
