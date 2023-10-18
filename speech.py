# pip install SpeechRecognition
# pip install pyaudio
import speech_recognition as sr

rec = sr.Recognizer()
print(sr.Microphone().list_working_microphones())
#Selecione o index de acordo com sei microfone
with sr.Microphone(1) as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Fale alguma coisa")
    audio = rec.listen(mic)
    frase = rec.recognize_google(audio, language="pt-BR")
    print(frase)