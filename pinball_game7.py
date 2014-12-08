# Katelyn and Lauren's CS final project
#
#
#
#

import time
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
     mouth = curve(pos=[(23,3, 10),(18,2.5, 15),(12,2,20),(7,.5,21),(0,0,23),(-7,.5,21),(-12,2,20),(-18,2.5,15),(-23,3,10)], radius= 2, color=color.black)
     T_hat = box(pos=(26.5,2.5,-43.5), axis=(-.5,0,1), length=1, width=40, height=2, color=color.magenta)
     L_hat = box(pos=(6,2.5,-46), axis=(-.5,0,1), length=14, width=1, height=2, color=color.magenta)
     R_hat = box(pos=(40,2.5,-26), axis=(-.5,0,1), length=20, width=1, height=2, color=color.magenta)
     L_side = curve(pos=[(-35,2.5,20),(-41.5,2.5,3),(-41,2.5,-8),(-37,2.5,-18),(-33,2.5,-24),(-28,2.5,-30),(-20,2.5,-36),(-12,2.5,-40),(3,2.5,-41)], radius=2, color=color.green)
     R_side = curve(pos=[(35,2.5,20),(41.5,2.5,3),(41,2.5,-8),(37,2.5,-18)], radius=2,color=color.green)

     list_of_barriers = [mouth, T_hat, L_hat, R_hat, L_side, R_side]
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
    L_shirt_top = box(pos=(37,2.5,20), axis=(1,0,0), 
             length=6, width=1, height = 2, color=color.red)
    R_shirt_top = box(pos=(-37,2.5,20), axis=(1,0,0), 
             length=6, width=1, height = 2, color=color.red)
    
    list_of_walls = [ w1, w2, w3 ]
    return list_of_walls
    
def make_arms():
    """ makes arms aka flippers
    """
    f1 = box(pos=(-22,2.5,58), axis=(1,0,0),
                length=35, width=5, height=2, color=color.green)
    f2 = box(pos=(22,2.5,58), axis=(1,0,0),
                length=35, width=5, height=2, color=color.green)
    list_of_arms = [ f1, f2 ]
    return list_of_arms
      
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
    alien = frame( pos=(10,2.5,-10) )  # makes a new "frame" == a container
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
     
     ball.vel = vector(5,0,0)
     RATE = 30
     dt = 1.0/RATE
     ShirtWalls = shirt_box()
     aL, aR = make_arms()
     aR.vel = 0.0
     aR.time = 0
     aL.vel = 0.0
     aL.time = 0
     print aR.pos, aR.axis, aR.length
     print aL.pos, aL.axis, aL.length
     while True:
            rate(RATE)

            #physics!
            ball.pos = ball.pos + ball.vel*dt
            aR.rotate(angle=aR.vel, axis=vector(0,1,0), origin=vector(39.5,2.5,58))
            aL.rotate(angle=aL.vel, axis=vector(0,1,0), origin=vector(-39.5,2.5,58))


            #end physics

            # collisions and timers
            t = time.time()
            if t > aR.time+.2:
                if t < aR.time+.3:
                    aR.vel = .28
                    #aR.time = time.time()
                else:
                    aR.vel = 0
                    aR.pos = vector(22,2.5,58); aR.axis=vector(1,0,0); aR.length=35
            if t > aL.time+.2:
                if t < aL.time+.3:
                    aL.vel = -.28
                    #aL.time = time.time()
                else:
                    aL.vel = 0
                    aL.pos = vector(-22,2.5,58); aL.axis=vector(1,0,0); aL.length=35

            if mag(ball.pos) > 40:
                #print ball.pos
                if ball.pos.x < 3 and ball.pos.z < 20:
                   ball.vel = rotate(-1.2*ball.vel, angle=.5*pi, axis=(1,0,1))
                   print ball.vel
                elif ball.pos.x > 35 and ball.pos.z < 20:
                   ball.vel = rotate(-1.2*ball.vel, angle=.5*pi, axis=(1,0,1))
                   print ball.vel
#                   ball.vel = -rotate(ball.vel, angle=-pi, axis=(1,0,1))
#                   print ball.vel
            
            elif ball.pos.x > 40:
                ball.pos.x = 39.5
                ball.vel.x = -1*ball.vel.x

            elif ball.pos.x < -40:
                ball.pos.x = -39.5
                ball.vel.x = -1*ball.vel.x

            #end coll


            if scene.kb.keys: #any keypress to be handled
                s = scene.kb.getkey()
                #left and right keys flap flippers!
                if aR.pos == vector(22,2.5,58):
                    if s == "right":
                        aR.vel = -.14
                        aR.time = time.time()
                if aL.pos == vector(-22,2.5,58):
                    if s == "left":
                        aL.vel = .14
                        aL.time = time.time()



            
           # print ball.vel, ball.pos


        

        


# start things!
if __name__ == "__main__":
    main()
