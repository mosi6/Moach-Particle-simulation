from Particles import *
from ParticleFunctions import *
from animations import *

def movement(N, n, x_min = -20, x_max = 20, y_min = -20, y_max = 20, vx_max = 5, vy_max = 5): #master function for driving the simulation. N is the number of collision to simulate, n is the number of particles
    particles = Particle_Array(n, x_min,x_max, y_min, y_max, vx_max, vy_max) #create a particle array object containing all of the particles
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
            print('collision!')
            time = collision_disc[0]  # time until the nearest collision
            ttime += time  # add time to the total time
            particles.step(time)  # move particles to their position at the new time
            if particles.array[collision_disc[1][0]].x < particles.array[collision_disc[1][1]].x: #gives collision_disc the two particles in order - right one first (important for sin calculation in the function)
                change_velo_disc(particles.array[collision_disc[1][0]],particles.array[collision_disc[1][1]],particles)  # call function to change the velocities of the two discs that have just colided
            else:
                change_velo_disc(particles.array[collision_disc[1][1]], particles.array[collision_disc[1][0]],particles)
            prev_col = collision_disc[1]  # updates the collision that was just calculated to be the previus collision
    for d in range(N):
        animateit(particles.array,particles,d,25)
    min_len = []
    for z in particles.array:
        min_len.append(len(z.anim))
    print('missed frames:', max(min_len)-min(min_len))
    print(particles.array)
    fig = animation()
#    just_graph(particles.array)
    ani = animat.FuncAnimation(fig, animate, frames=min(min_len),interval=15, blit=True)
#    ani.save('mymovie4.mp4', fps=30)
    print("done!")


movement(500, 50)
plt.show()
