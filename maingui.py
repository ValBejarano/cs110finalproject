from tkinter import *


class Rectangles:
	
	def __init__(self,newname):
		self.x1 = 0
		self.move_x1 = 0
		
		self.y1 = 0
		self.move_y1 = 0
		
		self.x2 = 0
		self.move_x2 = 0
		
		self.y2 = 0
		self.move_y2 = 0
		
		self.color = ""
		self.rectname = newname

	def draw(self, canvas):
		self.rectname = canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill=self.color)
			

def main():
	root = Tk()
	
	w = Canvas(root, width=600, height=500)
	w.pack()

	rect1 = Rectangles("rect1")
	rect1.x1 = 150
	rect1.y1 = 150
	rect1.x2 = 220
	rect1.y2 = 220
	rect1.color = "blue"
	rect1.draw(w)
	
	
	rect2 = Rectangles("rect2")
	rect2.x1 = 220
	rect2.y1 = 150
	rect2.x2 = 290
	rect2.y2 = 220
	rect2.color = "red"
	rect2.draw(w)
	
	
	rect3 = Rectangles("rect3")
	rect3.x1 = 290
	rect3.y1 = 150
	rect3.x2 = 360
	rect3.y2 = 220
	rect3.color = "green"
	rect3.draw(w)
	
	
	rect4 = Rectangles("rect4")
	rect4.x1 = 150
	rect4.y1 = 220
	rect4.x2 = 220
	rect4.y2 = 290
	rect4.color = "orange"
	rect4.draw(w)
	
	
	rect5 = Rectangles("rect5")
	rect5.x1 = 220
	rect5.y1 = 220
	rect5.x2 = 290
	rect5.y2 = 290
	rect5.color = "yellow"
	rect5.draw(w)
	
	
	rect6 = Rectangles("rect6")
	rect6.x1 = 290
	rect6.y1 = 220
	rect6.x2 = 360
	rect6.y2 = 290
	rect6.color = "purple"
	rect6.draw(w)
	
	
	rect7 = Rectangles("rect7")
	rect7.x1 = 150
	rect7.y1 = 290
	rect7.x2 = 220
	rect7.y2 = 360
	rect7.color = "pink"
	rect7.draw(w)
	
	
	rect8 = Rectangles("rect8")
	rect8.x1 = 220
	rect8.y1 = 290
	rect8.x2 = 290
	rect8.y2 = 360
	rect8.color = "black"
	rect8.draw(w)
	
	
	rect9 = Rectangles("rect9")
	rect9.x1 = 290
	rect9.y1 = 290
	rect9.x2 = 360
	rect9.y2 = 360
	rect9.color = "white"
	rect9.draw(w)


	root.mainloop()

main()
