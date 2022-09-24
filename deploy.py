# Import the required libraries
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import webbrowser

# Create an instance of tkinter frame
win= Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Define a function to show the popup message
def deploy():
   messagebox.showinfo("Project is deployed to GitHub repo.")

def showResult():
  webbrowser.open("file:///home/vassar/Desktop/addition.html", new=2)

# Add an optional Label widget
Label(win, text= "Deplot it to Github!", font= ('Aerial 17 bold italic')).pack(pady= 30)

# Create a Button to display the message
ttk.Button(win, text= "Deploy to Github", command=deploy).pack(pady= 20)
ttk.Button(win, text= "Show in Browser", command=showResult).pack(pady= 20)
win.mainloop()