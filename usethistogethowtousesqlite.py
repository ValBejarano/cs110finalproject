from tkinter import *
from random import randint

root = Tk()
root.geometry('600x470')
root.title('Catch The Button - Game')

clicks = 0
time = 20

def change():
    global clicks
    clicks += 1
    clicksLabel['text'] = 'Clicks: ' + str(clicks)
    rand = randint(1,5)

    if rand == 1:
        button.pack(side = LEFT, padx = randint(1, 220), pady = randint(1, 220))
    elif rand == 2:
        button.pack(side = RIGHT, padx = randint(1, 220), pady = randint(1, 220))
    elif rand == 3:
        button.pack(side = TOP, padx = randint(1, 220), pady = randint(1, 220))
    else:
        button.pack(side = BOTTOM, padx = randint(1, 220), pady = randint(1, 220))

def update_time():
    global time
    time = time-0.1
    timeLabel.config(text=str(time))
    if time<0.01: # Account for rounding errors
        timeLabel.config(text='0')
        button.pack_forget()
        Label(root, text='You scored {}'.format(clicks), font=('Helvetica', 20, 'bold')).pack()
    else:
        timeLabel.after(100, update_time)

clicksLabel = Label(root, text = 'Clicks: 0')
clicksLabel.pack(side=LEFT, anchor=N)

timeLabel = Label(root, text=str(time))
timeLabel.pack(side=RIGHT, anchor=N)
timeLabel.after(100, update_time)

button = Button(root, text = 'Catch me  :P', command = change)
button.pack(side = BOTTOM, padx = randint(1, 220), pady = randint(1, 220))

root.mainloop()
