import turtle
import time
import random

WIDTH,HEIGHT = 500,500 # constants are in the capital letters
COLORS = ['red','green','blue','orange','yellow','black','purple','pink','brown','cyan']

def get_number_of_racers():
    racers = 0
    while True:
        racers = input('Enter the number of the racers(2-10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric... Try Again!")
            continue
        #print("")  neglected if continue is executed
        if 2 <= racers <= 10: # executed only if input is number. otherwise it will started again from while loop.
            return racers
        else:
            print("Number is not in the range 2-10")
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)  # center at the middle
    screen.title("Turtle Racing")

def race(colors):
    turtles = create_turtle(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)

            x,y = racer.pos()
            if y >= HEIGHT//2 -10:
                return colors[turtles.index(racer)]

def create_turtle(colors):
    turtles = []
    spacingx = WIDTH//(len(colors)+1)

    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90) # turn upwards
        racer.penup()  # don't show the path followed
        racer.setpos(-WIDTH//2 +(i+1)*spacingx, -HEIGHT//2+20)
        racer.pendown()
        turtles.append(racer)
    return turtles

racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)
print(f'The winner is the turtle with color {winner}.')
time.sleep(5)
#print(colors)


def func_turtle():
    racer = turtle.Turtle()
    racer.color('red')
    racer.penup() # removes the path  racer.pendown()
    racer.speed(1)
    racer.shape('turtle')
    #racer.forward(100)
    #racer.left(90)  # 90 degrees
    #racer.forward(100)
    #racer.right(90)
    time.sleep(15)
    print(racers)
