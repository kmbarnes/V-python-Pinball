# Katelyn and Lauren's CS final project
#
#
#
#


import random
from visual import *

def make_board():
     """ makes the pinball board, it should be shaped like the three eyed alien
     """
     cylinder(pos=(0,1,0), axis=(0,1,0), radius=40, height=0.5, color=color.green)
     box(pos=(0,1.5,40), axis=(0,0,1), length=40, width=80, height=0.5, color=color.orange)
     box(pos=(20,1.5,-30), axis=(-.5,0,1), length=30, width=40, height=0.5, color=color.magenta)
     box(pos=(-5,2,22), axis=(1,0,.25), length=11, width=3, height=0.5, color=color.black)
     box(pos=(5,2,22), axis=(1,0,-.25), length=11, width=3, height=0.5, color=color.black)
def make_barriers():
     """ makes barriers, the stuff you run into that doesn't give you points
     """
     mouth_barrier = curve(pos=[(23,3, 10),(18,2.5, 15),(12,2,20),(7,.5,21),(0,0,23),(-7,.5,21),(-12,2,20),(-18,2.5,15),(-23,3,10)], radius= 2, color=color.black)
 #    left_side =
#     right_side =

     list_of_barriers = [mouth_barrier]
     return list_of_barriers
def shirt_box():
    """ makes barriers that will be game over if hit
    """
    
    w1 = box(pos=(-40,2.5,40), axis=(0,0,1), 
             length=40, width=1, height = 2, color=color.red)
    w2 = box(pos=(0,2.5,60), axis=(1,0,0), 
             length=80, width=1, height = 2, color=color.red)
    w3 = box(pos=(40,2.5,40), axis=(0,0,1), 
             length=40, width=1, height = 2, color=color.red)
    list_of_walls = [ w1, w2, w3 ]
    return list_of_walls
      
def make_bumpers():
     """ this function makes the bumpers, they should look like eyes
     """
     b1 = cylinder(pos=(-23,1,-8), axis=(0,1,0), radius=10, length=5, color=color.white)

     b1_pupil = cylinder(pos=(-23,1,-8), axis=(0,1,0), radius=3, length=5.5, color=color.black)

     b2 = cylinder(pos=(23,1,-8), axis=(0,1,0), radius=10, length=5, color=color.white)

     b2_pupil = cylinder(pos=(23,1,-8), axis=(0,1,0), radius=3, length=5.5, color=color.black)

     b3 = cylinder(pos=(0,1,-8), axis=(0,1,0), radius=10, length=5, color=color.white)

     b3_pupil = cylinder(pos=(0,1,-8), axis=(0,1,0), radius=3, length=5.5, color=color.black)

     list_of_bumpers = [b1, b2, b3, b1_pupil, b2_pupil, b3_pupil]
     return list_of_bumpers

def make_launchers():
     """ makes the ball launchers, a key part of pinball
     """

def make_alien():
    """ makes an alien! -- in the process, this shows how to
        group many objects into a single coordinate system ("frame")
        and treat that as a single object
        Docs here:  http://vpython.org/contents/docs/frame.html
    """
    alien = frame( pos=(10,100,-10) )  # makes a new "frame" == a container
    # with a local coordinate system that can hanve any number of parts...
    sphere( frame=alien, radius=1, color=color.green )
    sphere( frame=alien, radius=0.3, pos=(.7,.5,.2), color=color.white )
    sphere( frame=alien, radius=0.3, pos=(.2,.5,.7), color=color.white )
    sphere( frame=alien, radius=0.3, pos=(.5,.5,.5), color=color.white )
    cylinder( frame=alien, pos=(0,.9,-.2), axis=(.02,.2,-.02), 
              radius=.7, color=color.magenta)
    return alien   # always use the _frame_, not any of its parts...

def main():
     """ the main part of the game!
     """
     floor = make_board()
     
     ball = make_alien()

     bumpers = make_bumpers()

     barriers = make_barriers()
     
     ball.vel = vector(0,-1,0)
     RATE = 30
     dt = 1.0/RATE
     ShirtWalls = shirt_box()
     while True:
            rate(RATE)

            ball.pos = ball.pos + ball.vel*dt

            if ball.pos.y < 1.5:
                ball.vel.y = -.95*ball.vel.y
                ball.color = color.green
                #print 'splort'
            else:
                ball.vel.y = ball.vel.y - 19.6*dt
                ball.color = (1,0,1)
            #print ball.vel, ball.pos


# start things!
if __name__ == "__main__":
    main()
