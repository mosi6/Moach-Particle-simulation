import matplotlib.pyplot as plt
import matplotlib.animation as animat
import math
from ParticleFunctions import *


def animateit(p_array, i, fps): #function that creates list of locations with a fixed gap between them for a given collision
    for p in p_array: #for every particle in the simulation
        dis = distance(p.locations[i+1][0], p.locations[i+1][1], p.locations[i][0], p.locations[i][0]) #the distance between this collision and the next one
        va = math.sqrt((p.velocities[i][0]) ** 2 + (p.velocities[i][1]) ** 2) #the velocity in the same axis as the distance
        if va == 0 or dis == 0: #if either of them is zero the function will error out; in that case f will be 1 and dx would be the entire space between the collision
            time = 0.2
        else:
            time = abs(dis / va) #time is distance divided by velocity
        f = fps * time #the number of frames to animate
        dx = (p.locations[i+1][0] - p.locations[i][0]) / f #the change in the x axis
        dy = (p.locations[i+1][1] - p.locations[i][1]) / f #the change in the y axis
        kx = p.locations[i][0] #the starting location x
        ky = p.locations[i][1] #the strating location y
        for _ in range(int(f)): #for each frame we add the dx and dy to the animation list of the current particle
            p.anim.append((kx,ky))
            kx += dx
            ky += dy






# rect is the box edge
# rect = plt.Rectangle(box.bounds[::2],
#                     box.bounds[1] - box.bounds[0],
#                     box.bounds[3] - box.bounds[2],
#                     ec='none', lw=2, fc='none')
# ax.add_patch(rect)

def init(pi_array):
    """initialize animation"""
    global p_array
    p_array = pi_array
    # particles holds the locations of the particles
    # particles, = ax.plot([], [], 'bo', ms=6)



def animate(i):
    """perform animation step"""
    xdata = []
    ydata = []
    lnr, = plt.plot([], [], 'ro')
    for p in p_array:
        xdata.append(p.anim[i][0])
        ydata.append(p.anim[i][1])
    lnr.set_data(xdata, ydata)
    return lnr,





def animation():
    fig = plt.figure()
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                         xlim=(-50, 50), ylim=(-50, 50))
    return fig

