from tkinter import *
import time


def main():
	master = Tk()

	w = Canvas(master, width=600, height=500)
	w.pack()
	
	
	colors = ["blue", "red", "green", "orange", "yellow", "purple", "wheat2", "OliveDrab4", "IndianRed3"]
	
	seconds = 0
	


	rect1 = w.create_rectangle(150,150,220,220, fill= colors[seconds])
	rect2 = w.create_rectangle(220,150,290,220, fill= colors[seconds])
	rect3 = w.create_rectangle(290,150,360,220, fill= colors[seconds])  

	rect4 = w.create_rectangle(150,220,220,290, fill= colors[seconds])
	rect5 = w.create_rectangle(220,220,290,290, fill= colors[seconds])
	rect6 = w.create_rectangle(290,220,360,290, fill= colors[seconds])

	rect7 = w.create_rectangle(150,290,220,360, fill= colors[seconds])
	rect8 = w.create_rectangle(220,290,290,360, fill= colors[seconds])
	rect9 = w.create_rectangle(290,290,360,360, fill= colors[seconds])
	

	
	while seconds != 8:
		print(seconds)
		time.sleep(1)
		seconds += 1
	#w.itemconfig(rect2, fill="blue") # change color


	mainloop()
	
main()
