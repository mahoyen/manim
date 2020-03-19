import tkinter
import turtle

sc = tkinter.Tk()
sc.geometry("1000x1000+100+100")

fr4 = tkinter.Frame(sc, height=500, width=600, bd=4, bg="light green", takefocus="", relief=tkinter.SUNKEN)

fr4.grid(row=2, column=2, sticky=(tkinter.N, tkinter.E, tkinter.W, tkinter.S))

# Canvas
canvas = tkinter.Canvas(fr4, width=750, height=750)
canvas.pack()

# Turtle
turtle1 = turtle.RawTurtle(canvas)
turtle1.color("red")
turtle1.shape("circle")

def drag_handler(x, y):
    turtle1.ondrag(None)  # disable event inside event handler
    (tx, ty) = turtle1.pos()
    max_distance = 2
    deltax = tx-x
    deltay = ty-y
    if deltax**2+deltay**2 > max_distance**2:
        x = tx - max_distance*deltax/abs(deltax+deltay)
        y = ty - max_distance*deltay/abs(deltax+deltay)
    turtle1.goto(x, y)
    turtle1.ondrag(drag_handler)  # reenable event on event handler exit

turtle1.ondrag(drag_handler)

sc.mainloop()