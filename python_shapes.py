from turtle import *
import math

# Name your Turtle.
length = 20
t = Turtle()
#t.forward() vs forward()
t.width(length)


# Set Up your screen and starting position.
setup(500,300)
x_pos = -250
y_pos = -150
t.setposition(x_pos, y_pos)

### Write your code below:
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

#assignment left to right
# bleh = "style"
# angle = 90 #angle == 90
# angle = angle + 5 #angle == 95
# angle = angle + 5 #angle == 100

# Close window on click.
exitonclick()
