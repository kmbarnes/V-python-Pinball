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
    #head
    cylinder(pos=(0,1,0), axis=(0,1,0), radius=40, height=0.5, color=color.green)
    #shirt
    box(pos=(0,1.5,40), axis=(0,0,1), length=40, width=80, height=0.5, color=color.orange)
    #hat
    box(pos=(20,1.5,-30), axis=(-.5,0,1), length=30, width=40, height=0.5, color=color.magenta)
    #bottom parts of mouth
    box(pos=(-5,2,22), axis=(1,0,.25), length=11, width=3, height=0.5, color=color.black)
    box(pos=(5,2,22), axis=(1,0,-.25), length=11, width=3, height=0.5, color=color.black)

def make_barriers():
    """ makes barriers, the stuff you run into that doesn't give you points
    """
    #barrier part of mouth
    mouth = curve(pos=[(23,3, 10),(18,2.5, 15),(12,2,20),(7,.5,21),(0,0,23),(-7,.5,21),(-12,2,20),(-18,2.5,15),(-23,3,10)], radius= 2, color=color.black)
    #left side of head
    L_side = curve(pos=[(-35,2.5,20),(-41.5,2.5,3),(-41,2.5,-8),(-37,2.5,-18),(-33,2.5,-24),(-28,2.5,-30),(-20,2.5,-36),(-12,2.5,-40),(3,2.5,-41)], radius=2, color=color.green)
    #right side of head
    R_side = curve(pos=[(35,2.5,20),(41.5,2.5,3),(41,2.5,-8),(37,2.5,-18)], radius=2,color=color.green)

    list_of_barriers = [mouth, L_side, R_side]
    return list_of_barriers

def make_hat():
    #top of hat
    T_hat = box(pos=(26.5,2.5,-43.5), axis=(-.5,0,1), length=2, width=40, height=2, color=color.magenta)
    #left of hat
    L_hat = box(pos=(6,2.5,-46), axis=(-.5,0,1), length=14, width=2, height=2, color=color.magenta)
    #right of hat
    R_hat = box(pos=(40,2.5,-26), axis=(-.5,0,1), length=20, width=2, height=2, color=color.magenta)
    list_of_hat = [T_hat, L_hat, R_hat]
    return list_of_hat
    
def shirt_box():
    """ makes barriers that will be game over if hit
    """
    #left side of shirt
    w1 = box(pos=(-40,2.5,40), axis=(0,0,1), 
             length=40, width=1, height = 2, color=color.red)
    #bottom of shirt
    w2 = box(pos=(0,2.5,60), axis=(1,0,0), 
             length=80, width=1, height = 2, color=color.red)
    #right side of shirt
    w3 = box(pos=(40,2.5,40), axis=(0,0,1), 
             length=40, width=1, height = 2, color=color.red)
    #top left of shirt
    L_shirt_top = box(pos=(37,2.5,20), axis=(1,0,0), 
             length=6, width=1, height = 2, color=color.red)
    #top right of shirt
    R_shirt_top = box(pos=(-37,2.5,20), axis=(1,0,0), 
             length=6, width=1, height = 2, color=color.red)
    
    list_of_walls = [ w1, w2, w3 ]
    return list_of_walls
    
def make_arms():
    """ makes arms aka flippers
    """
    #left flipper
    f1 = box(pos=(-22,2.5,58), axis=(1,0,0),
                length=35, width=5, height=2, color=color.green)
    #right flipper
    f2 = box(pos=(22,2.5,58), axis=(1,0,0),
                length=35, width=5, height=2, color=color.green)
    list_of_arms = [ f1, f2 ]
    return list_of_arms
      
def make_bumpers():
    """ this function makes the bumpers, they should look like eyes
    """
    # left eye
    b1 = cylinder(pos=(-23,2.5,-8), axis=(0,1,0), radius=10, length=2.5, color=color.white)

    b1_pupil = cylinder(pos=(-23,2.5,-8), axis=(0,1,0), radius=3, length=3, color=color.black)
    # right eye
    b2 = cylinder(pos=(23,2.5,-8), axis=(0,1,0), radius=10, length=2.5, color=color.white)

    b2_pupil = cylinder(pos=(23,2.5,-8), axis=(0,1,0), radius=3, length=3, color=color.black)
    # middle eye
    b3 = cylinder(pos=(0,2.5,-8), axis=(0,1,0), radius=10, length=2.5, color=color.white)

    b3_pupil = cylinder(pos=(0,2.5,-8), axis=(0,1,0), radius=3, length=3, color=color.black)

    list_of_bumpers = [b1, b2, b3, b1_pupil, b2_pupil, b3_pupil]
    return list_of_bumpers

#def make_launchers():
#     """ makes the ball launchers, a key part of pinball
#     """

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
    #make everything here
    floor = make_board()
     
    ball = make_alien()

    hat = make_hat()

    bumpers = make_bumpers()

    barriers = make_barriers()
     
    ShirtWalls = shirt_box()

    aL, aR = make_arms()

    #set starting values
    ball.vel = vector(0,0,0)
    RATE = 30
    dt = 1.0/RATE
    aR.vel = 0.0
    aR.time = 0
    aL.vel = 0.0
    aL.time = 0
    print aR.pos, aR.axis, aR.length
    print aL.pos, aL.axis, aL.length
    while True:
            rate(RATE)

            #physics!
            #ball movement
            ball.pos = ball.pos + ball.vel*dt
            #flippers
            aR.rotate(angle=aR.vel, axis=vector(0,1,0), origin=vector(39.5,2.5,58))
            aL.rotate(angle=aL.vel, axis=vector(0,1,0), origin=vector(-39.5,2.5,58))
            #this accounts for gravity
 #           ball.vel.z = ball.vel.z + .5*dt

            #end physics

            # collisions and timers
            t = time.time()
            #flipper collisions
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
            

            # left eye collisions
            if mag(ball.pos - bumpers[0].pos)< 10:
                diff = ball.pos - bumpers[0].pos
                dtan = rotate( diff, radians(90), vector(0,1,0) )
                # get the two velocities
                vi = ball.vel
                vj = (0,0,0)
                # undo the last time step
                ball.pos -= 2*(ball.vel*dt)
                # find the radial and tangent parts
                vi_rad = proj(vi, diff)
                vi_tan = proj(vi, dtan)
                vj_rad = proj(vj, -diff)
                vj_tan = proj(vj, dtan)
                # swap the radials and keep the tangents
                ball.vel =  1.5*(vj_rad + vi_tan)
                # turns on or off the eye
                if bumpers[0].material == materials.emissive:
                    bumpers[0].material = materials.plastic
                else:
                    bumpers[0].material = materials.emissive
          
            # right eye collisions
            if mag(ball.pos - bumpers[1].pos)< 10:
                diff = ball.pos - bumpers[1].pos
                dtan = rotate( diff, radians(90), vector(0,1,0) )
                # get the two velocities
                vi = ball.vel
                vj = (0,0,0)
                # undo the last time step
                ball.pos -= 2*(ball.vel*dt)
                # find the radial and tangent parts
                vi_rad = proj(vi, diff)
                vi_tan = proj(vi, dtan)
                vj_rad = proj(vj, -diff)
                vj_tan = proj(vj, dtan)
                # swap the radials and keep the tangents
                ball.vel = 1.5*(vj_rad + vi_tan)
                # turns on or off the eye
                #
                if bumpers[1].material == materials.emissive:
                    bumpers[1].material = materials.plastic
                else:
                    bumpers[1].material = materials.emissive
           
            # middle eye collisions
            if mag(ball.pos - bumpers[2].pos)< 10:
                diff = ball.pos - bumpers[2].pos
                dtan = rotate( diff, radians(90), vector(0,1,0) )
                # get the two velocities
                vi = ball.vel
                vj = (0,0,0)
                # undo the last time step
                ball.pos -= 2*(ball.vel*dt)
                # find the radial and tangent parts
                vi_rad = proj(vi, diff)
                vi_tan = proj(vi, dtan)
                vj_rad = proj(vj, -diff)
                vj_tan = proj(vj, dtan)
                # swap the radials and keep the tangents
                ball.vel =  1.5*(vj_rad + vi_tan)
                # lights up the eye if not lit, turns off if it is
                if bumpers[2].material == materials.emissive:
                    bumpers[2].material = materials.plastic
                else:
                    bumpers[2].material = materials.emissive

           # if bumpers[0].material == materials.emissive and \
#               bumpers[1].material == materials.emissive and \
#               bumpers[2].material == materials.emissive:
#                   text(text='You WIN!!!!!', align = 'center', depth = -.2,
#                        pos=(0,10,50), width=40, axis=(1,0,0), height=20, up=(0,0,-.5),
#                        color = color.yellow)
#                   break
          
            if mag(ball.pos) > 40:
                #print ball.vel
                # for the left side of the head collisions
                if ball.pos.x < 6 and ball.pos.z < 20 and ball.pos.z > -44:
                    ball.pos -= ball.vel*dt
                    ball.vel = -1*rotate(ball.vel, angle=pi/2, axis=(0,1,0))
                # for the right side of the head collisions

                elif ball.pos.x > 35 and ball.pos.z < 20 and ball.pos.z > -18.5:
                    ball.pos -= ball.vel*dt #keeps ball from getting stuck
                    ball.vel = -1*rotate(ball.vel, angle=pi/2, axis=(0,1,0))
                # for the shirt box collisions
                else:
                    #right side of box
                    if ball.pos.x > 40:
                        ball.pos.x = 39.5
                        ball.vel.x = -1*ball.vel.x
                    #left side of box
                    elif ball.pos.x < -40:
                        ball.pos.x = -39.5
                        ball.vel.x = -1*ball.vel.x
                    #bottom of box
                    elif ball.pos.z > 60:
                        # for with actual pinball
                        #
                        # print "Game Over!"
                        # break
                        #
                        ball.pos.z = 59.5
                        ball.vel.z = -1*ball.vel.z
                    else:
#                        for i in range(len(hat)):
                            d0=(ball.pos - hat[0].pos)
                            #print d.x, d.z
                            ax0 = hat[0].axis
 #                           rax = ax.rotate(angle=pi/2, axis=(0,1,0))
                            nax0 = norm(ax0)

                            d1=(ball.pos - hat[1].pos)
                            #print d.x, d.z
                            ax1 = hat[1].axis
                            nrax1 = ax1.rotate(angle=pi/2, axis=(0,1,0))
                            nax1 = norm(ax1)

                            d2=(ball.pos - hat[2].pos)
                            #print d.x, d.z
                            ax2 = hat[2].axis
                            rax2 = ax2.rotate(angle=pi/2, axis=(0,1,0))
                            nrax2 = norm(rax2)
                            
                            #print d.dot(nrax), d
                            if d0.dot(nax0) < .5 and d0.dot(nax0) > -.5 :
                               #print d.dot(nrax), 'hi'
                               ball.pos -= ball.vel*dt
                               ball.vel=-1*ball.vel
                              # print 'up'
                            elif ball.pos.z < -40 and d1.dot(nrax1) < 1 and\
                                 d1.dot(nrax1) > -1 :
                               ball.pos -= ball.vel*dt
                               #print d.dot(nrax), 'hi'
                               ball.vel=-1*ball.vel
                               print 'left'
                            elif ball.pos.z < -18 and \
                                 d2.dot(nrax2) < .25 and d2.dot(nrax2) > -.25 :
                               #print d.dot(nrax), 'hi'
                               ball.pos -= ball.vel*dt 
                               ball.vel=-1*ball.vel
                               #print'right', d2.dot(nax2)
                               
                      

                   

            #end coll


            if scene.kb.keys: #any keypress to be handled
                s = scene.kb.getkey()
                #left and right keys flap flippers!
 #               if aR.pos == vector(22,2.5,58):
#                    if s == "right":
#                       aR.vel = -.14
 #                       aR.time = time.time()
#                if aL.pos == vector(-22,2.5,58):
#                    if s == "left":
#                        aL.vel = .14
#                        aL.time = time.time()
                dx = 1; dz = 1   # easily-changeable values
                if s == 'left': ball.vel += vector(-dx,0,0)
                if s == 'right': ball.vel += vector(dx,0,0)
                if s == 'up': ball.vel += vector(0,0,-3*dz)
                if s == 'down': ball.vel += vector(0,0,dz)
                if s == 'r': ball.pos = vector(10,2.5,-10)


            
           # print ball.vel, ball.pos


        

        


# start things!
if __name__ == "__main__":
    main()
