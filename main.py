import tkinter as tk
import azure.cognitiveservices.speech as speechsdk
from tkinter import *
from tkinter import messagebox

def main():
    r = tk.Tk()
    r.geometry('300x200')
    r.title('AppGenie Bot')
    button = tk.Button(r, text='Speak', width=25, command=recognize_from_mic())
    button.pack(ipadx=5,
    ipady=5,
    expand=True)
    r.mainloop()

def recognize_from_mic():
	#Find your key and resource region under the 'Keys and Endpoint' tab in your Speech resource in Azure Portal
	#Remember to delete the brackets <> when pasting your key and region!
    speech_config = speechsdk.SpeechConfig(subscription="3db91ff466f145f7af6493edd6abf2a1", region="centralindia")
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    
    #Asks user for mic input and prints transcription result on screen
    print("Speak into your microphone.")
    result = speech_recognizer.recognize_once_async().get()
    print(result.text)
    messagebox.showinfo(result.text)

def displayonwindow(msg):
   messagebox.showinfo(msg)


if __name__=="__main__":
    main()