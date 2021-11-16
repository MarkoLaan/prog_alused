from tkinter import *

#base
frame = Tk()
frame.title("Maja")

board = Canvas(frame, width=600, height=450)

# x0 y0 x1 y1
board.create_rectangle(0,0,605,455, fill="lightblue")
board.create_oval(-215,300,700,600, fill="lightgreen", outline="lightgreen")

board.create_rectangle(340,340,300,370, fill="red", outline="red")
board.create_polygon(340,340,300,340,320,320, fill="gray")

board.create_rectangle(315,350,305,370, fill="brown", outline="black")
board.create_rectangle(335,350,325,360, fill="lightyellow", outline="black")

#end
board.pack()
frame.mainloop()