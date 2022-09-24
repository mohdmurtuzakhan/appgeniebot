# Import the required libraries
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import azure.cognitiveservices.speech as speechsdk

# Create an instance of tkinter frame
win= Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Define a function to show the popup message
def show_msg():
    # messagebox.showinfo("Message","Hey There! I hope you are doing well.")
    #Find your key and resource region under the 'Keys and Endpoint' tab in your Speech resource in Azure Portal
	#Remember to delete the brackets <> when pasting your key and region!
    speech_config = speechsdk.SpeechConfig(subscription="3db91ff466f145f7af6493edd6abf2a1", region="centralindia")
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    
    #Asks user for mic input and prints transcription result on screen
    print("Speak into your microphone.")
    result = speech_recognizer.recognize_once_async().get()
    print(result.text)
    # messagebox.showinfo(result.text)
    Label(win, text= result.text, font= ('Aerial 17 bold italic')).pack(pady= 10)

# Add an optional Label widget
Label(win, text= "AppGenie Bot", font= ('Aerial 17 bold italic')).pack(pady= 30)
Label(win, text= "Converting natural language to code, please wait...", font= ('Aerial 17 bold italic')).pack(pady= 10)

# Create a Button to display the message
ttk.Button(win, text= "Speak", command=show_msg).pack(pady= 20)
win.mainloop()

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
    messagebox.showinfo("Message","Hey There! I hope you are doing well.")