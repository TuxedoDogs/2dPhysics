import turtle
turtle.pu()
turtle.speed(5)


staticLine = [ (-50,20), (-40,70) ]

ballObject = {
    "radius": 10,
    "position": [0, 0],
    "velocityX": 0,
    "velocityY": 1
}

# do the stuff

# display line
turtle.goto(staticLine[0])
turtle.pd()
turtle.color("red")
turtle.goto(staticLine[1])
turtle.color("black")
turtle.pu()

# display ball
turtle.goto(ballObject.get("position"))
turtle.color("blue")
turtle.dot()
turtle.color("black")
turtle.seth(270)
turtle.forward(ballObject.get("radius"))
turtle.seth(0)
turtle.pd()
turtle.circle(ballObject.get("radius")) # this is NOT around the midpoint! this is from the bottom
turtle.pu()


# draw perp bounds
turtle.goto(staticLine[0])
turtle.seth(turtle.towards(staticLine[1]))
turtle.right(90) # arbitrary whether it is right or left, however i am defining turning right 90deg as our "front"

turtle.forward(100)
turtle.pd()
turtle.backward(200)
turtle.pu()

turtle.goto(staticLine[1])
turtle.forward(100)
turtle.pd()
turtle.backward(200)
turtle.pu()

# Find if ball is within the 2 line equations
    # EXCEPTION! If y1 = y2, make sure to use x=k for lines
    # 1. Define line equations
        # find m
        # find both c's

# shorten vars to easier to read versions
x1 = staticLine[0][0] # point 1
y1 = staticLine[0][1]
x2 = staticLine[1][0] # point 2
y2 = staticLine[1][1]

x0 = ballObject.get("position")[0] # ball vars
y0 = ballObject.get("position")[1]
r = ballObject.get("radius")

# define the formulaic variables for the equation of the line between the current points
m1 = (y2-y1) / (x2-x1)
c1 = y1 - (m1*x1)
# y = x*m1 + c1

if m1 != 0:
    m2 = -(1/m1)
else:
    m2 = "house we need to make the line vertical"
print(m2)


turtle.exitonclick()