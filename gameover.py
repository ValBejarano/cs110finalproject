from tkinter import *

class Game_over():   
         
	def __init__(self):  

		self.root = Tk()
		self.w = Canvas(self.root, width=640, height=540)
		self.w.pack()		  
		self.root.resizable(width=False, height=False)
		
        
		self.oldTopFive = [["val",250],["bob",220],["tom",215],["jim",190],["sam",150]]
		self.gOverLabel = Label(self.root, text="GAME OVER", font = ("Helvetica", 40, "bold"))
		self.gOverLabel.place(x=165, y= 100)

		self.scoreLabel = Label(self.root, text="Your Score", font= ("Helvetica", 12, "bold")) #add player score function
		self.scoreLabel.place(x=140, y= 250)

		self.nameLabel = Label(self.root, text="Enter your name below", font=("Helvetica", 12, "bold")) 
		self.nameLabel.place(x=325, y= 225)

		self.playerName = Entry(self.root)                    
		self.playerName.place(x=350, y = 250)
		self.enterButton = Button(self.root, text="Enter", font=("Helvetica", 10, "bold"), command= self.printNameAndScore)
		self.enterButton.place(x=475, y=245)

		self.playerScore = Label(self.root, text ="Your Game", font=("Helvetica", 12, "bold"))
		self.playerScore.place(x=300, y=280)

		self.scrBoardButton = Button(self.root, text="Score Board", font=("Helvetica", 10, "bold"), command= self.printTopFive)
		self.scrBoardButton.place(x=300, y=350)
		self.root.mainloop() 

        #self.retryButton = Button(master, text = "Retry", fg = "green", font =("Helvetica", 17, "bold"), command= lambda:controller.show_frame(mainMenu)) #replace openGame with actual game window
        #self.retryButton.place(x=275, y= 550)

	def printNameAndScore(self):
		name = self.playerName.get()
        #fullScore = name + str(score)
		self.namePlayer = Label(text = name, font=("Helvetica", 12, "bold")) 
		self.namePlayer.place(x=290, y=315)
        #self.playerScore = Label(text=score, font=("Helvetica", 12, "bold")) add score later
        #self.playerScore.place(x=250, y=300)
        #playerAndScore = [name, score]
        

	def topFive(playerAndScore, oldTopFive):
		topFive = []
		numOne = oldTopFive[0][1]
		playerScore = playerAndScore[1]

		if(numOne < playerScore):
			numberOne = playerScore
			topFive.append(playerAndScore)
			topFive += oldTopFive
			topFive.remove(topFive[5])
			oldTopFive = topFive
		elif(playerScore < oldTopFive[4][1]):
			oldtopFive = oldTopFive
		else:
			for i in range(5):
				if(playerScore < oldTopFive[i][1] and playerScore > oldTopFive[i+1][1]):
					oldTopFive[i+1:0] = [playerAndScore]
			oldTopFive.remove(oldTopFive[5])                       
		return oldTopFive

        
	def printTopFive(self):
		self.oldTopFive
		x_name = 290
		y_name = 400
		x_score = 360
		y_score = 400
		for i in range(5):
			name = self.oldTopFive[i][0]
			score = self.oldTopFive[i][1]
			self.playerScore = Label(text = name, font=("Helvetica", 12, "bold"))
			self.playerScore.place(x=x_name, y=y_name)
			self.playerName = Label(text = score, font=("Helvetica", 12, "bold")) 
			self.playerName.place(x=x_score, y=y_score)
			y_name += 25
			y_score +=25

