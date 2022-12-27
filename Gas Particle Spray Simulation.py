#--------INSTRUCTIONS--------#
#Press S to start/stop particle spray
#Press P to pause the simulation, and from there, C to continue or Q to quit
#Press ESC to quit and save image results
#Press Up Arrow to increase ejection velocity, Down Arrow to decrease ejection velocity
#Press O to take a screenshot

import pygame, pymunk, random, sys, math, itertools, sys, pyautogui, datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

#Basic Setup
caption = "Gas Particles Simulation"
FPS = 120
text_size = 15
walls_on = True

#Print Data
print_data_1 = False
print_data_2 = False
print_array = False

#Particle Setup
v_ox = 250
max_v_oy = 1
particle_velocity_additive_constant = 50
v_ox_changeable = True
max_v_oy_changeable = False
max_particles = 10000
particles_generated_per_frame = 1
particle_density = 1
particle_elasticity = 1
particle_size = 1
particle_mass = 0
particle_drag_multiplicative_constant = 0.99975
quit_at_frame = 1000
pipe_radius = 30
pipe_thickness = 1
pipe_end_factor = 3


#Array Setup
cols = 300
rows = 300
arr = [[0 for i in range(cols)] for j in range(rows)]
arr2 = [[0 for i in range(cols)] for j in range(rows)]

#Colors
particle_heat_coloration = True
particle_color = "Blue"
background_color = "Black"

#Color Configuration
background_color_pygame = pygame.Color(background_color)
particle_color_pygame = pygame.Color(particle_color)
text_color = (255-background_color_pygame.r, 255-background_color_pygame.g, 255-background_color_pygame.b)
pause_text_background = background_color_pygame

#Startup
sys.stdout = open("Gas Particle Data.txt", "w")
window_length = 1000
window_height = 1000
display = pygame.display.set_mode((window_length, window_height), pygame.RESIZABLE) 
clock = pygame.time.Clock()
space = pymunk.Space()
pygame.display.set_caption(caption)
pygame.init()
frame_passed = 0
dev_values = []
displacements = []
to_average = []
msd_values = []
particles_count = 0
startpos = 0

class Particle():
    def __init__(self, x, y):
        self.body = pymunk.Body()
        self.body.position = x, y
        self.body.velocity = [v_ox, random.uniform(-max_v_oy, max_v_oy)]
        self.shape = pymunk.Circle(self.body, particle_size)
        self.shape.mass = particle_mass
        self.shape.density = particle_density
        self.shape.elasticity = particle_elasticity
        space.add(self.body, self.shape)

    def render(self, display):
        x, y = self.body.position
        if (particle_heat_coloration): #Heat Coloration
            if (math.sqrt((self.body.velocity[0])**2 + (self.body.velocity[1])**2) > math.sqrt((math.sqrt((v_ox)**2+(max_v_oy)**2))**2+(max_v_oy)**2)):
                pygame.draw.circle(display, (255, 0, 0), (int(x), int(y)), particle_size)
            elif (math.sqrt((self.body.velocity[0])**2 + (self.body.velocity[1])**2) > math.sqrt((v_ox)**2+(max_v_oy)**2)-(math.sqrt((v_ox)**2+(max_v_oy)**2)/16)):
                pygame.draw.circle(display, (255, 19, 0), (int(x), int(y)), particle_size)
            elif (math.sqrt((self.body.velocity[0])**2 + (self.body.velocity[1])**2) > math.sqrt((v_ox)**2+(max_v_oy)**2)-(math.sqrt((v_ox)**2+(max_v_oy)**2)/16)*2):
                pygame.draw.circle(display, (255, 38, 0), (int(x), int(y)), particle_size)
            elif (math.sqrt((self.body.velocity[0])**2 + (self.body.velocity[1])**2) > math.sqrt((v_ox)**2+(max_v_oy)**2)-(math.sqrt((v_ox)**2+(max_v_oy)**2)/16)*3):
                pygame.draw.circle(display, (255, 57, 0), (int(x), int(y)), particle_size)
            elif (math.sqrt((self.body.velocity[0])**2 + (self.body.velocity[1])**2) > math.sqrt((v_ox)**2+(max_v_oy)**2)-(math.sqrt((v_ox)**2+(max_v_oy)**2)/16)*4):
                pygame.draw.circle(display, (255, 76, 0), (int(x), int(y)), particle_size)
            elif (math.sqrt((self.body.velocity[0])**2 + (self.body.velocity[1])**2) > math.sqrt((v_ox)**2+(max_v_oy)**2)-(math.sqrt((v_ox)**2+(max_v_oy)**2)/16)*5):
                pygame.draw.circle(display, (255, 95, 0), (int(x), int(y)), particle_size)
            elif (math.sqrt((self.body.velocity[0])**2 + (self.body.velocity[1])**2) > math.sqrt((v_ox)**2+(max_v_oy)**2)-(math.sqrt((v_ox)**2+(max_v_oy)**2)/16)*6):
                pygame.draw.circle(display, (255, 114, 0), (int(x), int(y)), particle_size)
            elif (math.sqrt((self.body.velocity[0])**2 + (self.body.velocity[1])**2) > math.sqrt((v_ox)**2+(max_v_oy)**2)-(math.sqrt((v_ox)**2+(max_v_oy)**2)/16)*7):
                pygame.draw.circle(display, (255, 133, 0), (int(x), int(y)), particle_size)
            elif (math.sqrt((self.body.velocity[0])**2 + (self.body.velocity[1])**2) > math.sqrt((v_ox)**2+(max_v_oy)**2)-(math.sqrt((v_ox)**2+(max_v_oy)**2)/16)*8):
                pygame.draw.circle(display, (255, 152, 0), (int(x), int(y)), particle_size)
            elif (math.sqrt((self.body.velocity[0])**2 + (self.body.velocity[1])**2) > math.sqrt((v_ox)**2+(max_v_oy)**2)-(math.sqrt((v_ox)**2+(max_v_oy)**2)/16)*9):
                pygame.draw.circle(display, (224, 133, 32), (int(x), int(y)), particle_size)
            elif (math.sqrt((self.body.velocity[0])**2 + (self.body.velocity[1])**2) > math.sqrt((v_ox)**2+(max_v_oy)**2)-(math.sqrt((v_ox)**2+(max_v_oy)**2)/16)*10):
                pygame.draw.circle(display, (192, 114, 64), (int(x), int(y)), particle_size)
            elif (math.sqrt((self.body.velocity[0])**2 + (self.body.velocity[1])**2) > math.sqrt((v_ox)**2+(max_v_oy)**2)-(math.sqrt((v_ox)**2+(max_v_oy)**2)/16)*11):
                pygame.draw.circle(display, (160, 95, 96), (int(x), int(y)), particle_size)
            elif (math.sqrt((self.body.velocity[0])**2 + (self.body.velocity[1])**2) > math.sqrt((v_ox)**2+(max_v_oy)**2)-(math.sqrt((v_ox)**2+(max_v_oy)**2)/16)*12):
                pygame.draw.circle(display, (128, 76, 128), (int(x), int(y)), particle_size)
            elif (math.sqrt((self.body.velocity[0])**2 + (self.body.velocity[1])**2) > math.sqrt((v_ox)**2+(max_v_oy)**2)-(math.sqrt((v_ox)**2+(max_v_oy)**2)/16)*13):
                pygame.draw.circle(display, (96, 57, 160), (int(x), int(y)), particle_size)
            elif (math.sqrt((self.body.velocity[0])**2 + (self.body.velocity[1])**2) > math.sqrt((v_ox)**2+(max_v_oy)**2)-(math.sqrt((v_ox)**2+(max_v_oy)**2)/16)*14):
                pygame.draw.circle(display, (64, 38, 192), (int(x), int(y)), particle_size)
            elif (math.sqrt((self.body.velocity[0])**2 + (self.body.velocity[1])**2) > 1):
                pygame.draw.circle(display, (32, 19, 224), (int(x), int(y)), particle_size)
            elif (math.sqrt((self.body.velocity[0])**2 + (self.body.velocity[1])**2) < 1):
                pygame.draw.circle(display, (0, 0, 255), (int(x), int(y)), particle_size)
        else:
            pygame.draw.circle(display, (particle_color_pygame.r, particle_color_pygame.g, particle_color_pygame.b), (int(x), int(y)), particle_size)

particles = []

class Wall():
    def __init__(self, p1, p2):
        self.body = pymunk.Body(body_type = pymunk.Body.STATIC)
        self.shape = pymunk.Segment(self.body, p1, p2, pipe_thickness)
        self.shape.elasticity = 1
        space.add(self.body)
        space.add(self.shape)
        pygame.draw.line(display, text_color, p1, p2, width=pipe_thickness)

def Draw_and_Track_Particles():
    global frame_passed
    time = 1
    particlenumber = 1
    for particle in particles:
        particle.render(display)

        #Deceleration
        if (particle.body.velocity[0] > 0): #stop at 0
            particle.body.velocity *= particle_drag_multiplicative_constant
        
        if (print_data_1):
            print(str(frame_passed) + ", " + str(particlenumber) + ", " + str(particle.body.position[0]) + ", " + str(particle.body.position[1]) + ", " + str(math.sqrt(particle.body.velocity[0]**2+particle.body.velocity[1]**2)) + ", " + str(particle.body.velocity[0]) + ", " + str(particle.body.velocity[1]))

        particlenumber += 1

        if particlenumber-1 == particles_generated_per_frame:
            frame_passed+=1

        if (quit_at_frame != 0):
            if (frame_passed-1 == quit_at_frame):
                quit_process()

#Pause Text
font = pygame.font.Font('freesansbold.ttf', text_size)
pause_text = font.render('Paused: C to continue or Q to quit', True, text_color, pause_text_background)
textRect = pause_text.get_rect()
textRect.center = (window_length/2, window_height/2)

def maketable():
    global frame_passed, arr, rows, cols
    arr = [[0 for i in range(cols)] for j in range(rows)]

    for particle in particles:    
        y = int(particle.body.position[0]/(100)*rows/10)
        x = int(particle.body.position[1]/(100)*rows/10)

        if (x > rows-1):
            x = rows-1
        if (y > rows-1):
            y = rows-1
        if (x < 0):
            x = 0
        if (y < 0):
            y = 0

        arr[x][y] += 1

def makefulltable():
    global frame_passed, arr2, rows, cols

    for particle in particles:    
        y = int(particle.body.position[0]/(100)*rows/10)
        x = int(particle.body.position[1]/(100)*rows/10)

        if (x > rows-1):
            x = rows-1
        if (y > rows-1):
            y = rows-1
        if (x < 0):
            x = 0
        if (y < 0):
            y = 0

        arr2[x][y] += 1

def matrixmap2():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(arr2, cmap='binary')
    plt.title("Gas Particle Concentration (Full)")
    fig.colorbar(cax)
    fig.savefig("Gas Particle Concentration (Full) Graph.png")
    plt.close()

def dev():
    maketable()
    dev = np.var(arr)*particles_count
    dev_values.append(dev)
    mean = np.mean(arr)

def printdata2():
    dev = np.var(arr)*particles_count
    mean = np.mean(arr)
    print(str(frame_passed) + ", " + str(dev) + ", " + str(mean))

def matrixmap():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(arr, cmap='jet')
    plt.title("Gas Particle Concentration (Quit)")
    fig.colorbar(cax)
    fig.savefig("Gas Particle Concentration (Quit) Graph.png")
    plt.close()

def makedisplacements():
    for particle in particles:    
        position = (particle.body.position)
        displacements.append(position)

def msd():
    global startpos, to_average

    for i in range(startpos, len(displacements)-particles_generated_per_frame):
        initial_pos = displacements[0]
        next_pos = displacements[i+particles_generated_per_frame]

        displacement = math.sqrt((initial_pos[0]-next_pos[0])**2+(initial_pos[1]-next_pos[1])**2)
        to_average.append(displacement)
        startpos+=1
    msd = np.average(to_average)
    msd_values.append(msd)

def msdgraphs():
    global msd_values
    
    num = len(msd_values)
    x = []

    for i in range (num):
        x.append(i)
        i+=1

    y = msd_values
    
    plt.rcParams.update({'font.size':7})
    plt.title("Gas Particle Mean Squared Dispersion")
    plt.xlabel('Frames') 
    plt.ylabel('Mean Squared Dispersion') 
    plt.plot(x, y, color = 'b')
    plt.savefig("Gas Particle Mean Squared Dispersion Graph.png")
    plt.close()

    y_p = np.diff(y) / np.diff(x) / 2
    x_p = (np.array(x)[:-1] + np.array(x)[1:]) / 2

    x_p = np.insert(x_p, 0, 0)
    y_p = np.insert(y_p, 0, 0)

    plt.rcParams.update({'font.size':7})
    plt.title("Gas Particle Mean Squared Dispersion Derivative / 2")
    plt.xlabel('Frames') 
    plt.ylabel('Mean Squared Dispersion Derivative / 2') 
    plt.plot(x_p, y_p, color = 'darkblue')
    plt.savefig("Gas Particle Mean Squared Dispersion Derivative Graph.png")
    plt.close()

def devgraph():
    global dev_values
    num = len(dev_values)
    x = []

    for i in range (num):
        x.append(i)
        i+=1

    y = dev_values
    
    plt.rcParams.update({'font.size':7})
    plt.title("Gas Particle Number Density Standard Deviation")
    plt.xlabel('Frames') 
    plt.ylabel('Standard Deviation') 
    plt.plot(x, y, color = 'r')
    plt.savefig("Gas Particle Number Density Standard Deviation Graph.png")
    plt.close()

def speed_distribution():
    speeds = []
    bins = []
    max_value = math.sqrt((math.sqrt((v_ox)**2+(max_v_oy)**2))**2+(max_v_oy)**2)

    i = 0
    while (i <= max_value+max_value*2):
        bins.append(i)
        i += max_value/10

    for particle in particles:
        speeds.append(math.sqrt(particle.body.velocity[0]**2+particle.body.velocity[1]**2))
    
    plt.hist(speeds, bins, facecolor='b', alpha=0.7)
    plt.xlabel("Speeds")
    plt.ylabel("Number of Particles")
    plt.title("Gas Particle Speed Distribution (Quit)")
    plt.savefig("Gas Particle Speed Distribution (Quit) Graph")
    plt.close()

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                if event.key == pygame.K_q:
                    quit_process()
        display.blit(pause_text, textRect)
        pygame.display.update()
        clock.tick(FPS)

def update_fps():
    fps = "FPS: " + str(int(clock.get_fps()))
    fps_text = font.render(fps, 1, text_color)
    return fps_text
'''
def lagrangian_velocity_autocorrelation(speeds, tau):
    lagrangian_velocity_autocorrelation = 0
    for i in range(len(speeds)):
        lagrangian_velocity_autocorrelation += speeds[i] * speeds[(i + tau) % len(velocities)]
    return lagrangian_velocity_autocorrelation / len(speeds)
'''

def update_time_left():
    fps = int(clock.get_fps())
    fps_left = quit_at_frame-frame_passed
    seconds_left = 0
    if (fps != 0):
        seconds_left = (fps_left/fps)

    if (seconds_left > 1):
        seconds_left = int(seconds_left)

    if (frame_passed == 0):
        seconds_left = 0

    minutes_and_seconds_left = str(datetime.timedelta(seconds=seconds_left))
    time_left_text = font.render("Time Left: " + str(minutes_and_seconds_left), 1, text_color)
    return time_left_text
    
if (print_data_1):
    print("Frame, Particle #, s_x, s_y, v, v_x, v_y")

if (print_data_2):
    print("Frame, Standard Deviation, Mean")

def quit_process():
    pyautogui.screenshot(region=(461,53, 990, 990)).save('Gas Particle Simulation (Quit).png')
    devgraph()
    maketable()
    if (print_array):
        print("\n")
        for row in arr:
          print (row)
        print("\n")
    msdgraphs()
    matrixmap()
    matrixmap2()
    speed_distribution()
    quit()

#Simulation
def simulation():
    global v_ox, max_v_oy, particle_size, particles_count
    particles_on, data_2_collection = False, False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_process()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause()
                if event.key == pygame.K_s:
                    particles_on = not particles_on
                    data_2_collection = True
                if event.key == pygame.K_ESCAPE:
                    quit_process()
                if event.key == pygame.K_o:
                    pyautogui.screenshot(region=(461,53, 990, 990)).save('Gas Particle Simulation (During).png')
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if (v_ox_changeable):
                v_ox+=particle_velocity_additive_constant
            if (max_v_oy_changeable):
                max_v_oy+=particle_velocity_additive_constant
        if keys[pygame.K_DOWN]:
            if (v_ox > 0):
                if (v_ox_changeable):
                    v_ox-=particle_velocity_additive_constant
            if (max_v_oy > 0):    
                if (max_v_oy_changeable):
                    max_v_oy-=particle_velocity_additive_constant

        if (particles_on):
            for x in range(particles_generated_per_frame):
                for i in range(pipe_radius*2-1):
                    particle = Particle(0, 500-pipe_radius+i+1) #location of particle generation
                    particles.append(particle)
                    particles_count += 1
                    
        if (data_2_collection):
            dev()
            
            makedisplacements()
            if(frame_passed != 0):
                msd()    

            if (print_data_2):
               printdata2()

        if (max_particles != 0):
            if (particles_count == max_particles):
                particles_on = False        

        if (max_particles != 0):
            if (frame_passed*particles_generated_per_frame == max_particles):
                pyautogui.screenshot(region=(461,53, 990, 990)).save('Gas Particle Simulation (Ejection End).png')

        display.fill((background_color_pygame))
        Draw_and_Track_Particles()
        makefulltable()
        particles_count_text = font.render(("Particles: " + str(particles_count)), 1, text_color)
        
        if (quit_at_frame != 0):
            frames_passed_text = font.render(("Frames Passed: " + str(frame_passed) + "/" + str(quit_at_frame)), 1, text_color)
        else:
            frames_passed_text = font.render(("Frames Passed: " + str(frame_passed)), 1, text_color)

        if (particles_on):
            ejection_text = font.render(("Ejection: On"), 1, pygame.Color("green"))
        if (not particles_on):
            ejection_text = font.render(("Ejection: Off"), 1, pygame.Color("red"))
        velocity_text = font.render(("Ejection Velocity: " + str(math.sqrt((v_ox)**2+(max_v_oy)**2))), 1, text_color)


        if (walls_on):
            walls = [Wall((0, 500-pipe_radius),(0, 500+pipe_radius)), Wall((0, 500-pipe_radius), (100, 500-pipe_radius)), Wall((100, 500-pipe_radius), (125, 500-pipe_radius/pipe_end_factor)), Wall((0, 500+pipe_radius), (100, 500+pipe_radius)), Wall((100, 500+pipe_radius), (125, 500+pipe_radius/pipe_end_factor))]

        display.blit(update_fps(), (0,3)) 
        display.blit(particles_count_text, (0,3+text_size))
        display.blit(ejection_text, (0,3+text_size*2))
        display.blit(velocity_text, (0,3+text_size*3))
        display.blit(frames_passed_text, (0,3+text_size*4))
        if (quit_at_frame != 0):
            display.blit(update_time_left(), (0,3+text_size*5)) 
        pygame.display.update()
        clock.tick(FPS)
        space.step(1/FPS)

simulation()
sys.stdout.close()
pygame.quit()

#--------NOTES--------#

#--------Max Particles--------#
#max_particles = 0 will eject particles indefinitely
#max_particles does not stop you from starting the spray again using S

#--------Frames--------#
#quit_at_frame = 0 will keep program running indefinitely

#--------Walls--------#
#window lengths/heights are original walls
#new walls are made when window is resized, but original walls are kept

#--------Coloration--------#
#particle_heat_coloration overrides particle_color_pygame
#heat coloration is relative to ejection velocity
#text color is automatically done, inverted from the background color selection
#all available particle colors: https://htmlcolorcodes.com/color-names/

#--------Values--------#
#particle_drag_multiplicative_constant = 1 --> no drag
#particle_elasticity = 1 --> perfect elastic collisions
#if launched too fast, particles may glitch out of wall
#values are printed for easy data input in spreadsheet program

#--------Array--------#
#if you unexpectedly see a high concentration of particles at a border, this is because many particles glitched out of the wall at those points

#--------Screenshot--------#
#Do not move simulation window for correct screenshot
