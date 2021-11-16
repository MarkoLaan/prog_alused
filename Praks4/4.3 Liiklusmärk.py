from tkinter import *

#base
frame = Tk()
frame.title("Liiklusmärk")

board = Canvas(frame, width=600, height=600)

# x0 y0 x1 y1
board.create_oval(5,5,600,600, fill="red", width=1, outline="red")

board.create_rectangle(25,250,575,350, fill="white", outline="white")

#end
board.pack()
frame.mainloop()