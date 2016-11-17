from tkinter import *

class Application(Frame):            #passing in frame from tkinter
    def __init__(self, master):       #main window
        Frame.__init__(self, master)
        self.create_widgets()

def openGame():
   gameWn = Toplevel(root)     #add grid window later and replace with exisiting window

def openScoreb():
   scorebWn = Toplevel(root)      #add scoreboard window later and replace exisiting window

root = Tk()                       #can later add more windows within
root.geometry("450x450+500+300")
root.title("Grid Game Name(TBD)")


menuLabel = Label(root, text = "GAME NAME", font = ("Helvetica", 30, "bold"))
menuLabel.place(x=100, y=50)

startButton = Button(root, text = "Start", fg = "green", font = ("Helvetica", 15, "bold" ), command = openGame)
scoreboardButton = Button(root, text = "Score Board", fg = "blue", font = ("Helvetica", 15, "bold"), command = openScoreb)
startButton.place(x=100, y=150)
scoreboardButton.place(x=200, y = 150)

root.mainloop()
