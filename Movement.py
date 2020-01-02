from Particles import *
from ParticleFunctions import *
from animations import *

def movement(N, n, x_min, x_max, y_min, y_max, vmax): #master function for driving the simulation. N is the number of collision to simulate, n is the number of particles
    particles = Particle_Array(n, x_min,x_max, y_min, y_max,vmax) #create a particle array object containing all of the particles
    init(particles.array)
    prev_col = (9999999999, 999999999)#keeping the previous collision so that we won't calculate it again
    #hit = 0 |number of hits, relavent when N is not in the functionn
    ttime = 0 #total time
    #keepitup = True| relavent only when N is not in the function
    #while keepitup:| relavent only when N is not in the function
    for _ in range(N):
        collision_disc = find_collision_disc(particles.array,prev_col)
        collision_wall = find_collision_wall(particles.array) #optional room size
        if collision_wall[0] < collision_disc[0]: #checks if the nearest collision is with a wall
            time = collision_wall[0] #time until the nearest collision
            ttime += time #add time to the total time
            particles.step(time) #move particles to their position at the new time
            change_velo_wall(particles.array[collision_wall[1]]) #call function to change the velocity of the disc that had just colided
            prev_col = (9999999999, 999999999)
        else:
            time = collision_disc[0]  # time until the nearest collision
            ttime += time  # add time to the total time
            particles.step(time)  # move particles to their position at the new time
            change_velo_disc(particles.array[collision_disc[1][0]],particles.array[collision_disc[1][1]],particles)  # call function to change the velocities of the two discs that have just colided
            prev_col = collision_disc[1]  # updates the collision that was just calculated to be the previus collision
            # hit += 1 | #see "hit" comment above(line 11) ¯\_(ツ)_/¯
            # print('collision')
        # print('position:', posi_x, posi_y, '\n velocity:', velo_x, velo_y) | was used to check for errors
        # keepitup = std(velo_x,velo_y,expected_value,ttime)
        # print('progress:' + str(h+1) + '/' + str(N))
    # print("there are {} frames to animate...".format(hit)) | not relavent because hit doesn't exist
    for d in range(N):
        animateit(particles.array,d,5)
    min_len = []
    for z in particles.array:
        min_len.append(len(z.anim))
    print('missed frames:', max(min_len)-min(min_len))
    fig = animation()
    ani = animat.FuncAnimation(fig, animate, frames=min(min_len),
                               interval=10, blit=True)
    #ani.save('mymovie4.mp4', fps=30)
    print("done!")

movement(100,10,-20,20,-20,20,5)
plt.show()
