import turtle, math, time, random
from utils import *
# goal: make a cardinal move around the screen
# Section 1: Setup
s1 = create_sprite ("cardinal", 0, -200)
create_sprite("alien")
set_background("saas")
# TODO - set the starting value for your variables
cardinal = []
food = 10
age = 0
happiness = 0
grown = False 

# Section 2: Controls
def move_up_1():
    x = s1.xcor()
    y = s1.ycor() + 10 
    s1.goto(x, y)
window.onkeypress(move_up_1, "Up")

def move_down_1():
    x = s1.xcor() 
    y = s1.ycor() -10
    s1.goto(x, y)
window.onkeypress(move_down_1, "Down") 

def move_right_1(): 
    x = s1.xcor() + 10
    y = s1.ycor() 
    s1.goto(x, y)
window.onkeypress(move_right_1, "Right")

def move_left_1(): 
    x = s1.xcor() -10
    y = s1.ycor() 
    s1.goto(x, y)
window.onkeypress(move_left_1, "Left")

# Section 3: Game Loop
window.listen()
for i in range(10000000000):
    
    # cardinal_sprite.goto(x,y)


    # TODO - make an if statement for ending the game

    
    time.sleep(0.01)
    window.update()
    

	
print("Game Over")