from tkinter import *

#base
frame = Tk()
frame.title("Lipp")

board = Canvas(frame, width=600, height=300)

# x0 y0 x1 y1
board.create_rectangle(0,0,605,305, fill="white")

board.create_rectangle(175,125,605,175, fill="green", outline="green")

board.create_rectangle(0,0,175,125, fill="green", outline="green")

board.create_rectangle(0,175,175,305, fill="green", outline="green")

#end
board.pack()
frame.mainloop()