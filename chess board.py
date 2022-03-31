# import turtle
import turtle

# create screen object
scrn = turtle.Screen()

# creates turtle object
pen = turtle.Turtle()

# method to draw square
def draw():
  
    for i in range(4):
        pen.forward(30)
        pen.left(90)

    pen.forward(30)

# Driver code 
if __name__ == "__main__" :

    # set screen
    scrn.setup(600, 600)

    # set turtle object speed
    pen.speed(100)

    for i in range(8):
        pen.up()
        pen.setpos(0, 30*i)

        pen.down()

        for j in range(8):
            if(i + j)%2 == 0:
                col = 'black'
            else:
                col = 'white'

            pen.fillcolor(col)
            pen.begin_fill()
            draw()
            pen.end_fill()

pen.hideturtle()
        #turtle ()