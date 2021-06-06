import turtle
def mainFunction(var1 , var2):
    if var1>0:
        turtle.forward(var1)
        turtle.right(var2)
        mainFunction(var1-5,var2)
turtle.shape('turtle')
turtle.reset()
turtle.pen(speed=100)
turtle.delay(1)
length=500
turnBy=121
turtle.penup()
turtle.setpos(-length/2,length/2)
turtle.pendown()
mainFunction(length,turnBy)
turtle.mainloop()