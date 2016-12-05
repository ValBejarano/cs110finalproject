from tkinter import *
from random import randint
from gameover import Game_over


class Square():
	
	def __init__(self):
	
		self.root = Tk()
		self.root.resizable(width=False, height=False)
		self.w = Canvas(self.root, width=1040, height=500)
		self.w.pack()
		self.create_buttons()
		self.score = 0
		self.yourscoreis = Label(self.root, text="Your score is:")
		self.yourscoreis.place(x=400,y=10)
		self.scorelabel = Label(self.root, text=str(self.score))
		self.scorelabel.place(x=400,y=30)
		self.scorelabel.after(2000, self.lower_score)
		self.time = 0
		self.timeLabel = Label(self.root, text=str(self.time))
		self.timeLabel.pack(side=RIGHT, anchor=N)
		self.timeLabel.after(100, self.update_time)

		self.root.mainloop()
		

	def create_buttons(self):
	
		self.bluesquare = PhotoImage(file="bluesquare.png") 
		self.btnblue = Button(self.root, image = self.bluesquare, command = self.bluesquare_clicked)
		self.btnblue.image = self.bluesquare
		self.btnblue_xcoord = 350
		self.btnblue_ycoord = 150
		self.btnblue.place(x = self.btnblue_xcoord, y = self.btnblue_ycoord)
		
		self.whitesquare1 = PhotoImage(file="whitesquare.png") 
		self.btnwhite1 = Button(self.root, image = self.whitesquare1, command = self.white)
		self.btnwhite1.image = self.whitesquare1
		self.btnwhite1_xcoord = 420
		self.btnwhite1_ycoord = 150
		self.btnwhite1.place(x = self.btnwhite1_xcoord, y = self.btnwhite1_ycoord)
		
		self.whitesquare2 = PhotoImage(file="whitesquare.png") 
		self.btnwhite2 = Button(self.root, image = self.whitesquare2, command = self.white)
		self.btnwhite2.image = self.whitesquare2
		self.btnwhite2_xcoord = 490
		self.btnwhite2_ycoord = 150
		self.btnwhite2.place(x = self.btnwhite2_xcoord, y = self.btnwhite2_ycoord)
		
		self.whitesquare3 = PhotoImage(file="whitesquare.png") 
		self.btnwhite3 = Button(self.root, image = self.whitesquare3, command = self.white)
		self.btnwhite3.image = self.whitesquare3
		self.btnwhite3_xcoord = 350
		self.btnwhite3_ycoord = 220
		self.btnwhite3.place(x = self.btnwhite3_xcoord, y = self.btnwhite3_ycoord)
		
		self.whitesquare4 = PhotoImage(file="whitesquare.png") 
		self.btnwhite4 = Button(self.root, image = self.whitesquare4, command = self.white)
		self.btnwhite4.image = self.whitesquare4
		self.btnwhite4_xcoord = 420
		self.btnwhite4_ycoord = 220
		self.btnwhite4.place(x = self.btnwhite4_xcoord, y = self.btnwhite4_ycoord)
		
		self.redsquare = PhotoImage(file="redsquare.png") 
		self.btnred = Button(self.root, image = self.redsquare, command = self.gameover)
		self.btnred.image = self.redsquare
		self.btnred_xcoord = 490
		self.btnred_ycoord = 220
		self.btnred.place(x = self.btnred_xcoord, y = self.btnred_ycoord)
		
		self.whitesquare5 = PhotoImage(file="whitesquare.png") 
		self.btnwhite5 = Button(self.root, image = self.whitesquare5, command = self.white)
		self.btnwhite5.image = self.whitesquare5
		self.btnwhite5_xcoord = 350
		self.btnwhite5_ycoord = 290
		self.btnwhite5.place(x = self.btnwhite5_xcoord, y = self.btnwhite5_ycoord)
		
		self.whitesquare6 = PhotoImage(file="whitesquare.png") 
		self.btnwhite6 = Button(self.root, image = self.whitesquare6, command = self.white)
		self.btnwhite6.image = self.whitesquare6
		self.btnwhite6_xcoord = 420
		self.btnwhite6_ycoord = 290
		self.btnwhite6.place(x = self.btnwhite6_xcoord, y = self.btnwhite6_ycoord)
		
		self.whitesquare7 = PhotoImage(file="whitesquare.png") 
		self.btnwhite7 = Button(self.root, image = self.whitesquare7, command = self.white)
		self.btnwhite7.image = self.whitesquare7
		self.btnwhite7_xcoord = 490
		self.btnwhite7_ycoord = 290
		self.btnwhite7.place(x = self.btnwhite7_xcoord, y = self.btnwhite7_ycoord)
		
		self.redsquare2 = PhotoImage(file="redsquare.png") 
		self.btnred2 = Button(self.root, image = self.redsquare2, command = self.gameover)
		self.btnred2.image = self.redsquare2
		
		self.redsquare3 = PhotoImage(file="redsquare.png") 
		self.btnred3 = Button(self.root, image = self.redsquare3, command = self.gameover)
		self.btnred3.image = self.redsquare3
		
		self.redsquare4 = PhotoImage(file="redsquare.png") 
		self.btnred4 = Button(self.root, image = self.redsquare4, command = self.gameover)
		self.btnred4.image = self.redsquare4
		
		self.redsquare5 = PhotoImage(file="redsquare.png") 
		self.btnred5 = Button(self.root, image = self.redsquare5, command = self.gameover)
		self.btnred5.image = self.redsquare5
		
	def lower_score(self):
		self.score-=1
		self.scorelabel.config(text=str(self.score))
		self.scorelabel.place(x=400,y=30)
		self.scorelabel.after(2000, self.lower_score)
		
		
	def update_time(self):
		self.time+=.1
		self.timeLabel.config(text=str(self.time))
		'''
		if self.time<0.01: # Account for rounding errors
			self.timeLabel.config(text='Seconds: 0')
			#self.bluesquare.place(x=3000,y=3000)
			Label(self.root, text='You scored {}'.format(self.score), font=('Helvetica', 20, 'bold')).pack()
		
		else:
		'''
		self.timeLabel.after(100, self.update_time)
	
			
	def white(self):
		print("im a white square")
		
	def bluesquare_clicked(self):
		self.increase_score()
		self.move_whitesquares()
		self.move_redsquare()
		self.move_bluesquare()
		
	def increase_score(self):
		self.score+=1
		self.scorelabel.config(text=str(self.score))
		self.scorelabel.place(x=400,y=30)
		
	def move_redsquare(self):
		if(self.time<1):
			self.btnred_xcoord += randint(-30,30)
			self.btnred_ycoord -= randint(-30,30)
			self.btnred.place(x = self.btnred_xcoord, y = self.btnred_ycoord)
			
		elif(self.time<2.5 and self.time>1):
			self.btnred_xcoord -= randint(-40,40)
			self.btnred_ycoord += randint(-40,40)
			self.btnred.place(x = self.btnred_xcoord, y = self.btnred_ycoord)
			
		elif(self.time<5 and self.time>2.5):
			self.btnred_xcoord = randint(0,500)
			self.btnred_ycoord = randint(0,200)
			self.btnred.place(x = self.btnred_xcoord, y = self.btnred_ycoord)
			
		elif(self.time<10 and self.time>5):

			self.btnred2_xcoord = randint(0,750)
			self.btnred2_ycoord = randint(0,300)
			self.btnred2.place(x = self.btnred2_xcoord, y = self.btnred2_ycoord) 
			
			self.btnred_xcoord = randint(0,750)
			self.btnred_ycoord = randint(0,300)
			self.btnred.place(x = self.btnred_xcoord, y = self.btnred_ycoord)
			
		elif(self.time<20 and self.time>10):

			self.btnred3_xcoord = randint(0,1000)
			self.btnred3_ycoord = randint(0,475)
			self.btnred3.place(x = self.btnred3_xcoord, y = self.btnred3_ycoord) 
		
			self.btnred2_xcoord = randint(0,1000)
			self.btnred2_ycoord = randint(0,475)
			self.btnred2.place(x = self.btnred2_xcoord, y = self.btnred2_ycoord)
		
			self.btnred_xcoord = randint(0,1000)
			self.btnred_ycoord = randint(0,475)
			self.btnred.place(x = self.btnred_xcoord, y = self.btnred_ycoord)
			
		elif(self.time<30 and self.time>20):
			
			self.btnred4_xcoord = randint(0,1000)
			self.btnred4_ycoord = randint(0,475)
			self.btnred4.place(x = self.btnred4_xcoord, y = self.btnred4_ycoord) 

			self.btnred3_xcoord = randint(0,1000)
			self.btnred3_ycoord = randint(0,475)
			self.btnred3.place(x = self.btnred3_xcoord, y = self.btnred3_ycoord) 
		
			self.btnred2_xcoord = randint(0,1000)
			self.btnred2_ycoord = randint(0,475)
			self.btnred2.place(x = self.btnred2_xcoord, y = self.btnred2_ycoord)
		
			self.btnred_xcoord = randint(0,1000)
			self.btnred_ycoord = randint(0,475)
			self.btnred.place(x = self.btnred_xcoord, y = self.btnred_ycoord)
			
		else:
			
			self.btnred5_xcoord = randint(0,1000)
			self.btnred5_ycoord = randint(0,475)
			self.btnred5.place(x = self.btnred5_xcoord, y = self.btnred5_ycoord) 
			
			self.btnred4_xcoord = randint(0,1000)
			self.btnred4_ycoord = randint(0,475)
			self.btnred4.place(x = self.btnred4_xcoord, y = self.btnred4_ycoord) 

			self.btnred3_xcoord = randint(0,1000)
			self.btnred3_ycoord = randint(0,475)
			self.btnred3.place(x = self.btnred3_xcoord, y = self.btnred3_ycoord) 
		
			self.btnred2_xcoord = randint(0,1000)
			self.btnred2_ycoord = randint(0,475)
			self.btnred2.place(x = self.btnred2_xcoord, y = self.btnred2_ycoord)
		
			self.btnred_xcoord = randint(0,1000)
			self.btnred_ycoord = randint(0,475)
			self.btnred.place(x = self.btnred_xcoord, y = self.btnred_ycoord)
		
	def move_whitesquares(self):
		if (self.time<2):
		
			self.btnwhite1_xcoord += randint(-9,9)
			self.btnwhite1_ycoord -= randint(-9,9)
			self.btnwhite1.place(x = self.btnwhite1_xcoord, y = self.btnwhite1_ycoord)
			
			self.btnwhite2_xcoord -= randint(-9,9)
			self.btnwhite2_ycoord += randint(-9,9)
			self.btnwhite2.place(x = self.btnwhite2_xcoord, y = self.btnwhite2_ycoord)
			
			self.btnwhite3_xcoord += randint(-9,9)
			self.btnwhite3_ycoord -= randint(-9,9)
			self.btnwhite3.place(x = self.btnwhite3_xcoord, y = self.btnwhite3_ycoord)
			
			self.btnwhite4_xcoord += randint(-9,9)
			self.btnwhite4_ycoord -= randint(-9,9)
			self.btnwhite4.place(x = self.btnwhite4_xcoord, y = self.btnwhite4_ycoord)
			
			self.btnwhite5_xcoord -= randint(-9,9)
			self.btnwhite5_ycoord -= randint(-9,9)
			self.btnwhite5.place(x = self.btnwhite5_xcoord, y = self.btnwhite5_ycoord)
			
			self.btnwhite6_xcoord += randint(-9,9)
			self.btnwhite6_ycoord -= randint(-9,9)
			self.btnwhite6.place(x = self.btnwhite6_xcoord, y = self.btnwhite6_ycoord)
			
			self.btnwhite7_xcoord += randint(-9,9)
			self.btnwhite7_ycoord -= randint(-9,9)
			self.btnwhite7.place(x = self.btnwhite7_xcoord, y = self.btnwhite7_ycoord)
			
		elif(self.time<4 and self.time>2):
		
			self.btnwhite1_xcoord += randint(-19,19)
			self.btnwhite1_ycoord -= randint(-19,19)
			self.btnwhite1.place(x = self.btnwhite1_xcoord, y = self.btnwhite1_ycoord)
			
			self.btnwhite2_xcoord -= randint(-19,19)
			self.btnwhite2_ycoord += randint(-19,19)
			self.btnwhite2.place(x = self.btnwhite2_xcoord, y = self.btnwhite2_ycoord)
			
			self.btnwhite3_xcoord += randint(-19,19)
			self.btnwhite3_ycoord -= randint(-19,19)
			self.btnwhite3.place(x = self.btnwhite3_xcoord, y = self.btnwhite3_ycoord)
			
			self.btnwhite4_xcoord += randint(-19,19)
			self.btnwhite4_ycoord -= randint(-19,19)
			self.btnwhite4.place(x = self.btnwhite4_xcoord, y = self.btnwhite4_ycoord)
			
			self.btnwhite5_xcoord -= randint(-19,19)
			self.btnwhite5_ycoord -= randint(-19,19)
			self.btnwhite5.place(x = self.btnwhite5_xcoord, y = self.btnwhite5_ycoord)
			
			self.btnwhite6_xcoord += randint(-19,19)
			self.btnwhite6_ycoord -= randint(-19,19)
			self.btnwhite6.place(x = self.btnwhite6_xcoord, y = self.btnwhite6_ycoord)
			
			self.btnwhite7_xcoord += randint(-19,19)
			self.btnwhite7_ycoord -= randint(-19,19)
			self.btnwhite7.place(x = self.btnwhite7_xcoord, y = self.btnwhite7_ycoord)
			
		elif(self.time<6 and self.time>4):
		
			self.btnwhite1_xcoord += randint(-30,30)
			self.btnwhite1_ycoord -= randint(-30,30)
			self.btnwhite1.place(x = self.btnwhite1_xcoord, y = self.btnwhite1_ycoord)
			
			self.btnwhite2_xcoord -= randint(-30,30)
			self.btnwhite2_ycoord += randint(-30,30)
			self.btnwhite2.place(x = self.btnwhite2_xcoord, y = self.btnwhite2_ycoord)
			
			self.btnwhite3_xcoord -= randint(-30,30)
			self.btnwhite3_ycoord += randint(-30,30)
			self.btnwhite3.place(x = self.btnwhite3_xcoord, y = self.btnwhite3_ycoord)
			
			self.btnwhite4_xcoord += randint(-30,30)
			self.btnwhite4_ycoord -= randint(-30,30)
			self.btnwhite4.place(x = self.btnwhite4_xcoord, y = self.btnwhite4_ycoord)
			
			self.btnwhite5_xcoord += randint(-30,30)
			self.btnwhite5_ycoord -= randint(-30,30)
			self.btnwhite5.place(x = self.btnwhite5_xcoord, y = self.btnwhite5_ycoord)
			
			self.btnwhite6_xcoord -= randint(-30,30)
			self.btnwhite6_ycoord += randint(-30,30)
			self.btnwhite6.place(x = self.btnwhite6_xcoord, y = self.btnwhite6_ycoord)
			
			self.btnwhite7_xcoord -= randint(-30,30)
			self.btnwhite7_ycoord += randint(-30,30)
			self.btnwhite7.place(x = self.btnwhite7_xcoord, y = self.btnwhite7_ycoord)
			
		elif(self.time<8 and self.time>6):
		
			self.btnwhite1_xcoord += randint(-40,40)
			self.btnwhite1_ycoord -= randint(-40,40)
			self.btnwhite1.place(x = self.btnwhite1_xcoord, y = self.btnwhite1_ycoord)
			
			self.btnwhite2_xcoord -= randint(-40,40)
			self.btnwhite2_ycoord += randint(-40,40)
			self.btnwhite2.place(x = self.btnwhite2_xcoord, y = self.btnwhite2_ycoord)
			
			self.btnwhite3_xcoord -= randint(-40,40)
			self.btnwhite3_ycoord += randint(-40,40)
			self.btnwhite3.place(x = self.btnwhite3_xcoord, y = self.btnwhite3_ycoord)
			
			self.btnwhite4_xcoord += randint(-40,40)
			self.btnwhite4_ycoord -= randint(-40,40)
			self.btnwhite4.place(x = self.btnwhite4_xcoord, y = self.btnwhite4_ycoord)
			
			self.btnwhite5_xcoord += randint(-40,40)
			self.btnwhite5_ycoord -= randint(-40,40)
			self.btnwhite5.place(x = self.btnwhite5_xcoord, y = self.btnwhite5_ycoord)
			
			self.btnwhite6_xcoord -= randint(-40,40)
			self.btnwhite6_ycoord += randint(-40,40)
			self.btnwhite6.place(x = self.btnwhite6_xcoord, y = self.btnwhite6_ycoord)
			
			self.btnwhite7_xcoord -= randint(-40,40)
			self.btnwhite7_ycoord += randint(-40,40)
			self.btnwhite7.place(x = self.btnwhite7_xcoord, y = self.btnwhite7_ycoord)
			
		elif(self.time<10 and self.time>8):
		
			self.btnwhite1_xcoord += randint(-50,50)
			self.btnwhite1_ycoord -= randint(-50,50)
			self.btnwhite1.place(x = self.btnwhite1_xcoord, y = self.btnwhite1_ycoord)
			
			self.btnwhite2_xcoord -= randint(-50,50)
			self.btnwhite2_ycoord += randint(-50,50)
			self.btnwhite2.place(x = self.btnwhite2_xcoord, y = self.btnwhite2_ycoord)
			
			self.btnwhite3_xcoord -= randint(-50,50)
			self.btnwhite3_ycoord += randint(-50,50)
			self.btnwhite3.place(x = self.btnwhite3_xcoord, y = self.btnwhite3_ycoord)
			
			self.btnwhite4_xcoord += randint(-50,50)
			self.btnwhite4_ycoord -= randint(-50,50)
			self.btnwhite4.place(x = self.btnwhite4_xcoord, y = self.btnwhite4_ycoord)
			
			self.btnwhite5_xcoord += randint(-50,50)
			self.btnwhite5_ycoord -= randint(-50,50)
			self.btnwhite5.place(x = self.btnwhite5_xcoord, y = self.btnwhite5_ycoord)
			
			self.btnwhite6_xcoord -= randint(-50,50)
			self.btnwhite6_ycoord += randint(-50,50)
			self.btnwhite6.place(x = self.btnwhite6_xcoord, y = self.btnwhite6_ycoord)
			
			self.btnwhite7_xcoord -= randint(-50,50)
			self.btnwhite7_ycoord += randint(-50,50)
			self.btnwhite7.place(x = self.btnwhite7_xcoord, y = self.btnwhite7_ycoord)
			
		elif(self.time<12 and self.time>10):
		
			self.btnwhite1_xcoord = randint(0,600)
			self.btnwhite1_ycoord = randint(0,300)
			self.btnwhite1.place(x = self.btnwhite1_xcoord, y = self.btnwhite1_ycoord)
			
			self.btnwhite2_xcoord = randint(0,600)
			self.btnwhite2_ycoord = randint(0,300)
			self.btnwhite2.place(x = self.btnwhite2_xcoord, y = self.btnwhite2_ycoord)
			
			self.btnwhite3_xcoord = randint(0,600)
			self.btnwhite3_ycoord = randint(0,300)
			self.btnwhite3.place(x = self.btnwhite3_xcoord, y = self.btnwhite3_ycoord)
			
			self.btnwhite4_xcoord = randint(0,600)
			self.btnwhite4_ycoord = randint(0,300)
			self.btnwhite4.place(x = self.btnwhite4_xcoord, y = self.btnwhite4_ycoord)
			
			self.btnwhite5_xcoord = randint(0,600)
			self.btnwhite5_ycoord = randint(0,300)
			self.btnwhite5.place(x = self.btnwhite5_xcoord, y = self.btnwhite5_ycoord)
			
			self.btnwhite6_xcoord = randint(0,600)
			self.btnwhite6_ycoord = randint(0,300)
			self.btnwhite6.place(x = self.btnwhite6_xcoord, y = self.btnwhite6_ycoord)
			
			self.btnwhite7_xcoord = randint(0,600)
			self.btnwhite7_ycoord = randint(0,300)
			self.btnwhite7.place(x = self.btnwhite7_xcoord, y = self.btnwhite7_ycoord)
			
		elif(self.time<14 and self.time>12):
		
			self.btnwhite1_xcoord = randint(0,600)
			self.btnwhite1_ycoord = randint(0,300)
			self.btnwhite1.place(x = self.btnwhite1_xcoord, y = self.btnwhite1_ycoord)
			
			self.btnwhite2_xcoord = randint(0,600)
			self.btnwhite2_ycoord = randint(0,300)
			self.btnwhite2.place(x = self.btnwhite2_xcoord, y = self.btnwhite2_ycoord)
			
			self.btnwhite3_xcoord = randint(0,600)
			self.btnwhite3_ycoord = randint(0,300)
			self.btnwhite3.place(x = self.btnwhite3_xcoord, y = self.btnwhite3_ycoord)
			
			self.btnwhite4_xcoord = randint(0,600)
			self.btnwhite4_ycoord = randint(0,300)
			self.btnwhite4.place(x = self.btnwhite4_xcoord, y = self.btnwhite4_ycoord)
			
			self.btnwhite5_xcoord = randint(0,600)
			self.btnwhite5_ycoord = randint(0,300)
			self.btnwhite5.place(x = self.btnwhite5_xcoord, y = self.btnwhite5_ycoord)
			
			self.btnwhite6_xcoord = randint(0,600)
			self.btnwhite6_ycoord = randint(0,300)
			self.btnwhite6.place(x = self.btnwhite6_xcoord, y = self.btnwhite6_ycoord)
			
			self.btnwhite7_xcoord = randint(0,600)
			self.btnwhite7_ycoord = randint(0,300)
			self.btnwhite7.place(x = self.btnwhite7_xcoord, y = self.btnwhite7_ycoord)
			
		elif(self.time<21 and self.time>14):
			self.btnwhite1_xcoord = randint(0,600)
			self.btnwhite1_ycoord = randint(0,300)
			self.btnwhite1.place(x = self.btnwhite1_xcoord, y = self.btnwhite1_ycoord)
			
			self.btnwhite2_xcoord = randint(0,600)
			self.btnwhite2_ycoord = randint(0,300)
			self.btnwhite2.place(x = self.btnwhite2_xcoord, y = self.btnwhite2_ycoord)
			
			self.btnwhite3_xcoord = randint(0,600)
			self.btnwhite3_ycoord = randint(0,300)
			self.btnwhite3.place(x = self.btnwhite3_xcoord, y = self.btnwhite3_ycoord)
			
			self.btnwhite4_xcoord = randint(0,600)
			self.btnwhite4_ycoord = randint(0,300)
			self.btnwhite4.place(x = self.btnwhite4_xcoord, y = self.btnwhite4_ycoord)
			
			self.btnwhite5_xcoord = randint(0,600)
			self.btnwhite5_ycoord = randint(0,300)
			self.btnwhite5.place(x = self.btnwhite5_xcoord, y = self.btnwhite5_ycoord)
			
			self.btnwhite6_xcoord = randint(0,600)
			self.btnwhite6_ycoord = randint(0,300)
			self.btnwhite6.place(x = self.btnwhite6_xcoord, y = self.btnwhite6_ycoord)
			
			self.btnwhite7_xcoord = randint(0,600)
			self.btnwhite7_ycoord = randint(0,300)
			self.btnwhite7.place(x = self.btnwhite7_xcoord, y = self.btnwhite7_ycoord)
			
		else:
			self.btnwhite1_xcoord = randint(0,1000)
			self.btnwhite1_ycoord = randint(0,450)
			self.btnwhite1.place(x = self.btnwhite1_xcoord, y = self.btnwhite1_ycoord)
			
			self.btnwhite2_xcoord = randint(0,1000)
			self.btnwhite2_ycoord = randint(0,450)
			self.btnwhite2.place(x = self.btnwhite2_xcoord, y = self.btnwhite2_ycoord)
			
			self.btnwhite3_xcoord = randint(0,1000)
			self.btnwhite3_ycoord = randint(0,450)
			self.btnwhite3.place(x = self.btnwhite3_xcoord, y = self.btnwhite3_ycoord)
			
			self.btnwhite4_xcoord = randint(0,1000)
			self.btnwhite4_ycoord = randint(0,450)
			self.btnwhite4.place(x = self.btnwhite4_xcoord, y = self.btnwhite4_ycoord)
			
			self.btnwhite5_xcoord = randint(0,1000)
			self.btnwhite5_ycoord = randint(0,450)
			self.btnwhite5.place(x = self.btnwhite5_xcoord, y = self.btnwhite5_ycoord)
			
			self.btnwhite6_xcoord = randint(0,1000)
			self.btnwhite6_ycoord = randint(0,450)
			self.btnwhite6.place(x = self.btnwhite6_xcoord, y = self.btnwhite6_ycoord)
			
			self.btnwhite7_xcoord = randint(0,1000)
			self.btnwhite7_ycoord = randint(0,450)
			self.btnwhite7.place(x = self.btnwhite7_xcoord, y = self.btnwhite7_ycoord)
		
		
		
	def move_bluesquare(self):
		if (self.time<2):
		
			move_x = randint(0,9)
			move_y = randint(0,9)
			self.btnblue_xcoord-=move_x
			self.btnblue_ycoord+=move_y
			self.btnblue.place(x = self.btnblue_xcoord, y = self.btnblue_ycoord)
			
		elif(self.time<4 and self.time>2):
		
			move_x = randint(5,16)
			move_y = randint(5,16)
			self.btnblue_xcoord+=move_x
			self.btnblue_ycoord-=move_y
			self.btnblue.place(x = self.btnblue_xcoord, y = self.btnblue_ycoord)
			
		elif(self.time<6 and self.time>4):
		
			move_x = randint(10,25)
			move_y = randint(10,25)
			self.btnblue_xcoord-=move_x
			self.btnblue_ycoord+=move_y
			self.btnblue.place(x = self.btnblue_xcoord, y = self.btnblue_ycoord)
			
		elif(self.time<8 and self.time>6):
		
			move_x = randint(10,35)
			move_y = randint(10,35)
			self.btnblue_xcoord+=move_x
			self.btnblue_ycoord-=move_y
			self.btnblue.place(x = self.btnblue_xcoord, y = self.btnblue_ycoord)
			
		elif(self.time<10 and self.time>8):
		
			self.btnblue_xcoord = randint(10,300)
			self.btnblue_ycoord = randint(10,100)
			self.btnblue.place(x = self.btnblue_xcoord, y = self.btnblue_ycoord)
			
		elif(self.time<12 and self.time>10):
		
			self.btnblue_xcoord = randint(10,500)
			self.btnblue_ycoord = randint(10,200)
			self.btnblue.place(x = self.btnblue_xcoord, y = self.btnblue_ycoord)
			
		elif(self.time<14 and self.time>12):
		
			self.btnblue_xcoord = randint(10,1000)
			self.btnblue_ycoord = randint (10,300)
			self.btnblue.place(x = self.btnblue_xcoord, y = self.btnblue_ycoord)
			
		else:
			self.btnblue_xcoord = randint(10,1000)
			self.btnblue_ycoord = randint (10,450)
			self.btnblue.place(x = self.btnblue_xcoord, y = self.btnblue_ycoord)
			
		
	def gameover(self):
		Game_over()

def main():

	Square()
	
main()

