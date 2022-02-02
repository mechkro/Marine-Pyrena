#GlowScript 3.1 VPython

import vpython
#from vpython import *
#from visual import *
#import random
#import collections as clc
#from tkinter import messagebox
scene = vpython.canvas()
scene.resizable = True
scene.title = 'Marine Arena'
#scene.fullscreen = True
#--------------------------------------------
def display_point(evt):
    """ 
    
    """
    loc = evt.pos
    return
    #T = text(canvas = scene, text=f'{loc}', align='center', color=color.green)
    #messagebox.showinfo("User has clicked!", vpython.vector(loc))
    
 
def move_player(evt):
    """ 
    If you want all of the spheres to go into the xy plane, perpendicular to the z axis, change the latter part of the program like this:
    loc = evt.project(normal=vector(0,0,1))
    # loc is None if no intersection with plane
    if loc:
        sphere(pos=loc,radius=0.2,color=color.cyan)
    """
    loc = evt.project(normal=vpython.vector(0,0,1))


#from vpython import *
#from visual import *
#import random
#import collections as clc
#from tkinter import messagebox

scene = vpython.canvas()
scene.resizable = True
scene.title = 'Marine Arena'
#scene.fullscreen = True

#--------------------------------------------
def display_point(evt):
    """ 
    
    """
    loc = evt.pos
    return
    #T = text(canvas = scene, text=f'{loc}', align='center', color=color.green)
    #messagebox.showinfo("User has clicked!", vpython.vector(loc))
    
 
def move_player(evt):
    """ 
    If you want all of the spheres to go into the xy plane, perpendicular to the z axis, change the latter part of the program like this:
    loc = evt.project(normal=vector(0,0,1))
    # loc is None if no intersection with plane
    if loc:
        sphere(pos=loc,radius=0.2,color=color.cyan)
    """
    loc = evt.project(normal=vpython.vector(0,0,1))
    if loc:
        sphere(canvas = scene2, pos = loc, radius = 4, color = vpython.color.yellow)    
    


#---------------------------------------------
scene2 = vpython.canvas(title='Marine Arena', x=0, y=0, width=1200, height=600,
     center=vpython.vector(5,0,0), background=vpython.vector(1,1,1))

scene2.bind('click', display_point)

   
#T1_init.velocity = vpython.vector(loc)       
#If you want all of the spheres to go into the xy plane, perpendicular to the z axis, change the latter part of the program like this:

# loc = evt.project(normal=vector(0,0,1))
# # loc is None if no intersection with plane
# if loc:
#     sphere(pos=loc,radius=0.2,color=color.cyan)
"""
txt = vpython.text(pos = vpython.vector(0,.25,0),                                  
           axis = vpython.vector(0,0,0),
           text = 'MA',
           width = 50,
           height = 50,
           color = vpython.color.black)
"""


#def box_maker(p,l,w,h,o):
#    vpython.box(canvas=scene2,pos=p,length=l,width=w,height=h,opacity=0)



#Define the arena grid in which the 4 base spawns will be located at edge corners

arena = vpython.box(pos = vpython.vector(0,-2,0),
            length = 500,
            width = 500,
            height = 3,
            opacity = 0.5)  


#arena = box_maker(vpython.vector(0,-2,0),500,500,3,0.5)

# Middle battleground
Ring = vpython.ring(pos = vpython.vector(0,35,0),
            axis = vpython.vector(0,1,0),
            radius = 100,
            thickness = 8,
            opacity = 0.6)


# Start of arena wall creations
wallyellow_1 = vpython.box(pos = vpython.vector(-210,.25+10,-150),
                   length = 75,
                   width = 3,
                   height = 20,
                   color = vpython.color.yellow,
                   opacity = 0.6)

wallyellow_2 = vpython.box(pos = vpython.vector(-150,.25+10,-210),
                   length = 3,
                   width = 75,
                   height = 20,
                   color = vpython.color.yellow,
                   opacity = 0.6)

wallblue_1 = vpython.box(pos = vpython.vector(210,.25+10,-150),
                   length = 75,
                   width = 3,
                   height = 20,
                   color = vpython.color.blue,
                   opacity = 0.6)

wallblue_2 = vpython.box(pos = vpython.vector(150,.25+10,-210),
                   length = 3,
                   width = 75,
                   height = 20,
                   color = vpython.color.blue,
                   opacity = 0.6)

wallgreen_1 = vpython.box(pos = vpython.vector(-210,.25+10,150),
                   length = 75,
                   width = 3,
                   height = 20,
                   color = vpython.color.green,
                   opacity = 0.6)

wallgreen_2 = vpython.box(pos = vpython.vector(-150,.25+10,210),
                   length = 3,
                   width = 75,
                   height = 20,
                   color = vpython.color.green,
                   opacity = 0.6)                   

wallmagenta_1 = vpython.box(pos = vpython.vector(210,.25+10,150),
                   length = 75,
                   width = 3,
                   height = 20,
                   color = vpython.color.magenta,
                   opacity = 0.6)

wallmagenta_2 = vpython.box(pos = vpython.vector(150,.25+10,210),
                   length = 3,
                   width = 75,
                   height = 20,
                   color = vpython.color.magenta,
                   opacity = 0.6)


mid_wall_yellow = vpython.box(pos = vpython.vector(-25,.25+10,-125),
                   length = 75,
                   width = 3,
                   height = 20,
                   color = vpython.color.yellow,
                   opacity = 0.6)
                   
mid_wall_blue = vpython.box(pos = vpython.vector(25,.25+10,125),
                   length = 75,
                   width = 3,
                   height = 20,
                   color = vpython.color.blue,
                   opacity = 0.6)

mid_wall_green = vpython.box(pos = vpython.vector(-25,.25+10,-125),
                   length = 75,
                   width = 3,
                   height = 20,
                   color = vpython.color.green,
                   opacity = 0.6)

mid_wall_magenta = vpython.box(pos = vpython.vector(25,.25+10,125),
                   length = 75,
                   width = 3,
                   height = 20,
                   color = vpython.color.magenta,
                   opacity = 0.6)


# These are spawn locations (homebase) for each team
Team_1_spawn = vpython.box(pos = vpython.vector(-225,.25,-225),
                   length = 50,
                   width = 50,
                   height = 1,
                   color = vpython.color.yellow,
                   opacity = 0.8)            
Team_2_spawn = vpython.box(pos = vpython.vector(225,.25,-225),
                   length = 50,
                   width = 50,
                   height = 1,
                   color = vpython.color.blue,
                   opacity = 0.8)                   
Team_3_spawn = vpython.box(pos = vpython.vector(-225,.25,225),
                   length = 50,
                   width = 50,
                   height = 1,
                   color = vpython.color.green,
                   opacity = 0.8) 
Team_4_spawn = vpython.box(pos = vpython.vector(225,.25,225),
                   length = 50, 
                   width = 50,
                   height = 1,
                   color = vpython.color.magenta,
                   opacity = 0.8)   


ll_1 = vpython.local_light(pos = vpython.vector(-225,.25,-225),
                   color = vpython.color.yellow)
ll_2 = vpython.local_light(pos = vpython.vector(225,.25,-225),
                   color = vpython.color.blue)
ll_3 = vpython.local_light(pos = vpython.vector(-225,.25,225),
                   color = vpython.color.green)
ll_4 = vpython.local_light(pos = vpython.vector(225,.25,225),
                   color = vpython.color.magenta)


#t1s = rr.randrange(0,10)
t2s_1 = range(-225,-200,5)
t2s_2 = range(200,225,5)
t3s_1 = range(200,225,5)
t3s_2 = range(-225,-200,5)
t4s = range(200,225,5)



T1_init = vpython.sphere(canvas = scene2, pos = vpython.vector(-220,4.25,-220), radius = 4, color = vpython.color.yellow)
T1_init.velocity = vpython.vector(0,0,0)

T2 = vpython.pyramid(canvas = scene2, pos=vpython.vector(200,4.25,200), size=vpython.vector(10,16,10), axis = vpython.vector(0,1,0), color = vpython.color.magenta)
T2.velocity = vpython.vector(-25,0,-25)

cnt = 0
Bullethold = []

dt = .01
delt = 0


#----------------------------------
def yellow_soldiers():
    """ """
    yellowhold.append(vpython.sphere(pos = vpython.vector(-220,2,-220),
            axis = vpython.vector(0,1,0),
            radius = 4,color = vpython.color.yellow, shininess = 1))
    yellowhold[-1].velocity = vpython.vector(0,0,1)
    return

#----------------------------------
def blue_soldiers():
    """ """
    bluehold.append(vpython.sphere(pos = vpython.vector(225,2,-225),
            axis = vpython.vector(0,1,0),
            radius = 4,color = vpython.color.blue, shininess = 1))
    bluehold[-1].velocity = vpython.vector(1,0,0)
    return 

#----------------------------------
def green_soldiers():
    """ """
    greenhold.append(vpython.sphere(pos = vpython.vector(-225,2,225),
            axis = vpython.vector(0,1,0),
            radius = 4,color = vpython.color.green, shininess = 1))
    greenhold[-1].velocity = vpython.vector(1,0,1)
    return

#----------------------------------
def magenta_soldiers():
    """ """
    magentahold.append(vpython.sphere(pos = vpython.vector(225,2,225),
            axis = vpython.vector(0,1,0),
            radius = 4,color = vpython.color.magenta, shininess = 1))
    magentahold[-1].velocity = vpython.vector(1,0,1)
    return


yellowhold = []
bluehold = []
greenhold = []
magentahold = []

#----------------------------------
while True:
    
    vpython.rate(100)
    delt = delt + dt
    #print(delt)
    T1_init.pos = vpython.vector(T1_init.pos + T1_init.velocity*dt)
    T2.pos = vpython.vector(T2.pos + T2.velocity*dt)
    
    #----------------------------------
    def firebullet(evt):
        """
        vnorm = norm(loc)
        
        #if int(Bullets) <= 5:
        Bullethold.append(vpython.sphere(pos = T1_init.pos,
                axis = vnorm, radius = 15,color = vpython.color.yellow, shininess = 1))
        Bullethold[-1].velocity = vnorm*(10)
        Bullethold.append(vpython.sphere(pos = vpython.vector(T1_init.pos.x,15,T1_init.pos.z),
                axis = vpython.vector(T1_init.pos - loc),
                radius = 15,color = vpython.color.yellow, shininess = 1))
        Bullethold[-1].velocity = vpython.vector(T1_init.pos - loc)*(-9)
        """
        loc = vpython.vector(evt.pos)
        Bullethold.append(vpython.sphere(pos = vpython.vector(T1_init.pos.x,15,T1_init.pos.z),
                axis = vpython.vector(T1_init.pos - loc),
                radius = 15,color = vpython.color.yellow, shininess = 1))
        Bullethold[-1].velocity = vpython.vector(T1_init.pos - loc)*(-9)
        return
    
    scene2.bind('click', firebullet)
    
    for i in Bullethold:
        try:
            i.pos = vpython.vector(i.pos + i.velocity*dt)
        except AttributeError:
            pass
        if vpython.mag(i.pos) >= 300:
            i.visible = False
            del i
        else:
            pass
        
    if delt >= 1:
        yellow_soldiers()
        blue_soldiers()
        green_soldiers()
        magenta_soldiers()        
        delt = 0
    else:
        pass
    
    for i in yellowhold:
        i.pos = vpython.vector(i.pos + i.velocity*dt)
    for i in bluehold:
        i.pos = vpython.vector(i.pos + i.velocity*dt)
    for i in greenhold:
        i.pos = vpython.vector(i.pos + i.velocity*dt)
    for i in magentahold:
        i.pos = vpython.vector(i.pos + i.velocity*dt)
        

#    for i in [yellowhold[:],bluehold[:],greenhold[:],magentahold[:]]:
#        for j in i:
#            j.pos = vpython.vector(j.pos + j.velocity*dt)
            
        
            
    