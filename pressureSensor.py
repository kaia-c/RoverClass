import turtle
from Arduino import Arduino

pin=14              #A0
startPressure=295   #the reading we get with no pressure
startSize=10        #which we will equate with drawing a radius of 10px
modifyFactor=10     #modified by a factor of 10
board=Arduino('9600', 'COM6')
board.pinMode(pin, 'INPUT')

#set up turtle pen
turtle.pen(fillcolor="purple", pencolor="black", pensize=10)
turtle.speed(0)     #don't delay drawing when called
turtle.penup()      #don't draw while we set up
turtle.right(90)    #degrees
turtle.forward(modifyFactor*startSize)
turtle.left(90)
turtle.pendown()    #start drawing
try:
    while True:
        pressure=board.analogRead(pin)
        adjustedPressure=pressure-(startPressure-startSize)
        print("pressure="+str(pressure)+
              " - adjustedPressure="+str(adjustedPressure))
        turtle.clear()
        turtle.begin_fill()
        turtle.circle(modifyFactor*adjustedPressure)
        turtle.end_fill()
except (KeyboardInterrupt, SystemExit):
    print('exiting')
    turtle.bye()
    exit()

