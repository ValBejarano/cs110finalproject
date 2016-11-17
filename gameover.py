from tkinter import *

class Application(Frame):            #passing in frame from tkinter
    def __init__(self,master):       #main window
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

def openGame():
   gameWn = Toplevel(root)

root = Tk()    
root.geometry("450x450+500+300")
root.title("Grid Game Name(TBD)")                   

gOverLabel = Label(root, text="GAME OVER", font = ("Helvetica", 30, "bold"))
gOverLabel.place(x=100, y= 50)

scoreLabel = Label(root, text="Your Score", font= ("Helvetica", 10, "bold")) #add player score function
scoreLabel.place(x=100, y= 150)
playerName = Entry(root)                    
playerName.place(x=200, y = 150)
retryButton = Button(text = "Retry", fg = "green", font =("Helvetica", 15, "bold"), command=openGame) #replace openGame with actual game window


retryButton.place(x=170, y= 250)

root.mainloop()
