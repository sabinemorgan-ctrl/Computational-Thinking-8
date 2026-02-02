import turtle, time, random
from utils import *

# Section 1 - setup
# - set a background using set_background(summer)
set_background("summer")
 
# create at least two variables and set their starting value
cardinals = 0
points = 0


#  Section 2 - controls
# - define an action. ex: def my_control()
def get_points ():
    global points
    points += 1
# - choose a key to do the action. ex: window.onkeypress(my_control, "p")
window.onkeypress(get_points, "p")
# - make a second control



def get_cardinals ():
    global cardinals,points
    points += 1
    cardinals += 1
window.onkeypress(get_cardinals, "c" )
x = random.randint(-200,200)
y = random.randint(-200,200)


# Section 3 - game loop
window.listen()
for i in range(1000000000):
    
    # - put any automatic actions here

    time.sleep(0.01)
    window.update()