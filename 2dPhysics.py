import turtle
import time
import math
turtle.delay(0)
turtle.hideturtle()
turtle.tracer(0)
turtle.pu()

debugWriter = turtle.Turtle()
debugWriter.pu()
debugWriter.forward(200)

# dict of collidable objects, points in key (relative to a hidden point that serves as 0,0), properties in values
# they connect in order of input, with the last one connecting to the first
# detection for if objects cross, close on detection and send message
# for now, dict only contains fixed objects that will not move

# vars
movementStep = 2
updateRate = 10

# def objects
listOfStaticObjects = []
staticObject1 = {
    "shape": [ [-25,130], [-25,140], [25,140], [25,130] ],
    "fixed": True
}
listOfStaticObjects.append(staticObject1)

playerObject = {
    "shape": [ [0,0], [-10,0], [-10,-10], [0,-10] ],
    "fixed": True
}

ballObject = {
    "radius": 5,
    "position": [0, 0],
    "velocityX": 0,
    "velocityY": 1
}

directionsBools = {
    "up" : False,
    "down" : False,
    "left" : False,
    "right" : False,
}

# secondary funcs

# main funcs
def move():
    movementY = 0
    if directionsBools.get("up") == True and directionsBools.get("down") == False:
        movementY = movementStep
    if directionsBools.get("down") == True and directionsBools.get("up") == False:
        movementY = -movementStep

    movementX = 0
    if directionsBools.get("right") == True and directionsBools.get("left") == False:
        movementX = movementStep
    if directionsBools.get("left") == True and directionsBools.get("right") == False:
        movementX = -movementStep
    
    for i in listOfStaticObjects: # move other things around player
        for point in i.get("shape"):
            point[0] -= movementX
            point[1] -= movementY
    ballObject.update({"position": [ballObject.get("position")[0] - movementX, ballObject.get("position")[1] - movementY]})

def ballPhysics():
    print("haha physics")
    # 2 big math things need to happen:
    # checking when the circle collides
    # determining its new velocity by doing some force calcs with support force kinda
    for i in listOfStaticObjects: # do for every static, to say for every set of points in a shape
        message = []
        for pointA in range(len(i.get("shape"))): # pointA and pointB represent a line in the shape, and the amount of points in a shape is the amount of lines due to how connections work
            pointB = pointA + 1
            if pointB >= len(i.get("shape")):
                pointB = 0 # this is 0 because it is an index
            
            pointA = i.get("shape")[pointA] # go from index to coordinates
            pointB = i.get("shape")[pointB]
            
            pointC = ballObject.get("position")

            # for every point pair (otherwise known as a "line")
            # define vector AB # wall
            # define vector AC # to ball from A
            # define vector BC # to ball from B
            
            # a*b = (|a|*|b| )*cosθ
            # θ = arccos( (a*b) / (|a|*|b|) ) # absolute of the vectors is just the magnitude, the distance of the 2 points
            #If vector a = < ax , ay > and b = < bx, by >,
            #Then the dot product between two vectors a and b is given as,
            #a.b  = <ax, ay > . < bx, by >
            #a.b = ax.bx + ay.by
            # the dot just means *

            vectorAB = (pointB[0] - pointA[0], pointB[1] - pointA[1]) # get relative values for the vectors (move up X amount rather than coordinates)
            vectorAC = (pointC[0] - pointA[0], pointC[1] - pointA[1])
            vectorBC = (pointC[0] - pointB[0], pointC[1] - pointB[1]) # completes the triangle
            # NOTE: NEXT TIME YOU WORK ON THIS, YOU NEED TO USE BC TO FIND ANGLEABC TO COMPLETE THE TRIANGLE, AND DRAW ANGLE HALF OF THE 3RD WORKED OUT ANGLE (it wont help but itll look cool)

            dotProduct =  vectorAB[0] * vectorAC[0] + vectorAB[1] * vectorAC[1] # find dot product

            turtle.goto(pointA) # get vector magnitudes
            vectorABmagnitude = turtle.distance(tuple(pointB))
            vectorACmagnitude = turtle.distance(tuple(pointC))

            # get angles in triangle
            angleBAC = math.acos( dotProduct / (vectorABmagnitude * vectorACmagnitude)) * 180 / math.pi
            angleABC = math.acos( dotProduct / (vectorABmagnitude * vectorACmagnitude)) * 180 / math.pi
            print(angleBAC, angleABC)

        # for now, commented
        # debugWriter.clear()
        # amount = 0
        # for j in i.get("shape"):
        #     debugWriter.pu()
        #     debugWriter.goto(j)
        #     debugWriter.write(round(message[amount], 1))
        #     debugWriter.pd()
        #     amount += 1


    ballObject.update({"position": [ballObject.get("position")[0] + ballObject.get("velocityX"), ballObject.get("position")[1] + ballObject.get("velocityY")]})


def renderObjects():
    turtle.clear()
    for i in listOfStaticObjects: # render statics
        for point in i.get("shape"):
            turtle.goto(point)
            turtle.pd()
        turtle.goto(i.get("shape")[0])
        turtle.pu()
    turtle.pu()
    for point in playerObject.get("shape"): # render player
        turtle.goto(point)
        turtle.pd()
    turtle.goto(playerObject.get("shape")[0])
    turtle.pu()

    turtle.goto(ballObject.get("position")) # render ball
    turtle.seth(90)
    turtle.forward(ballObject.get("radius"))
    turtle.pd()
    turtle.circle(ballObject.get("radius")) # this is NOT around the midpoint! this is from the bottom
    turtle.pu()
    turtle.seth(270)
    turtle.forward(ballObject.get("radius"))
    
    turtle.update()

def runFunctions(): # main loop
    move()
    ballPhysics()
    renderObjects()
    input("kjefdnuiseawbgfvijuerdasb")
    turtle.ontimer(runFunctions, updateRate)


runFunctions()
turtle.listen()


turtle.onkeypress(lambda:directionsBools.update({"up" : True}), "Up") # player controls
turtle.onkeyrelease(lambda:directionsBools.update({"up" : False}), "Up")
turtle.onkeypress(lambda:directionsBools.update({"down" : True}), "Down")
turtle.onkeyrelease(lambda:directionsBools.update({"down" : False}), "Down")
turtle.onkeypress(lambda:directionsBools.update({"left" : True}), "Left")
turtle.onkeyrelease(lambda:directionsBools.update({"left" : False}), "Left")
turtle.onkeypress(lambda:directionsBools.update({"right" : True}), "Right")
turtle.onkeyrelease(lambda:directionsBools.update({"right" : False}), "Right")

turtle.mainloop()

# physics calc

# collision detection and correction

# input script

# game-logic, possibly

# render object
