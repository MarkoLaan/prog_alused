from tkinter import *

#base
frame = Tk()
frame.title("Malelaud")

board = Canvas(frame, width=800, height=800)

# x y values
x0= 0
y0= 0
x1= 100
y1= 100

rida = 1
while rida <= 8:
    if rida % 2 == 1:
        varv1 = "black"
        varv2 = "lightyellow"
    else:
        varv1 = "lightyellow"
        varv2 = "black"
    veerg = 1
    while veerg <= 8:
        if veerg % 2 == 1:
            board.create_rectangle(x0,y0,x1,y1, fill=varv1)
        else: 
            board.create_rectangle(x0,y0,x1,y1, fill=varv2)
        x0 = x0 + 100
        x1 = x1 + 100
        veerg = veerg + 1
    x0= 0
    y0 = y0 + 100
    y1 = y1 + 100
    rida = rida + 1

#end
board.pack()
frame.mainloop()