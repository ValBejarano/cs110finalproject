from tkinter import *

class mainMenu:     

    def __init__(self, master):       #main window

        self.menuLabel = Label(master, text = "GAME NAME", font = ("Helvetica", 40, "bold"))
        self.menuLabel.place(x=165, y=100)
        
        self.startButton = Button(master, text = "Start", fg = "green", font = ("Helvetica", 17, "bold" ), command = self.openGame)
        self.startButton.place(x=200, y=300)

        scoreboardButton = Button(master, text = "Score Board", fg = "blue", font = ("Helvetica", 17, "bold"), command = self.openScoreb)
        scoreboardButton.place(x=300, y = 300)
    
    def openGame():
        self.gameWn = Toplevel(root)
        

    def openScoreb():
        self.scorebWn = Toplevel(root)     	
		
def main():
		root = Tk()                       
		menuWn = mainMenu(root)
		root.geometry("650x650+500+300")
		root.title("Grid Game Name(TBD)")
		root.resizable(width=False, height=False)
		root.mainloop()
		
main()
