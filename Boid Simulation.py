import pygame, pyautogui, math, datetime
from pygame.locals import *
from pygame.math import Vector2 as vector
import random
import matplotlib.pyplot as plt
import numpy as np
import sys

pygame.init()

#Setup
caption = "Boid Simulation"
clock = pygame.time.Clock()
background = pygame.Color("black")
foreground = pygame.Color("white")
window_length = 1000
window_height = 1000
display = pygame.display.set_mode((window_length, window_height), (pygame.RESIZABLE))
display_rect = display.get_rect()
text_color = pygame.Color("white")
text_size = 15
font = pygame.font.Font('freesansbold.ttf', text_size)
pause_text_background = pygame.Color("black")
pause_text = font.render('Paused: C to continue or Q to quit', True, text_color, pause_text_background)
textRect = pause_text.get_rect()
textRect.center = (window_length/2, window_height/2)
cols = 300
rows = 300
arr = [[0 for i in range(cols)] for j in range(rows)]
arr2 = [[0 for i in range(cols)] for j in range(rows)]
sys.stdout = open("Boid Data.txt", "w")
startpos = 0

#Entry
max_ejection_angle = 180
randompos = False
s_ox = 0
s_oy = 500
cohesion_constant = 0.001
alignment_constant = 0.05
separation_constant = 0.03
ideal_distance_from_other_boids = 5
max_turn = 4
sight_range = 30
max_speed = 5
boids_generated = 50 #if infinite, per frame
boid_size = 2
boid_angle = 60
max_boids = 50000
infinite_boid = True #makes boids generate per frame
quit_at_frame = 1000

#Print Data
print_data_1 = False #Frame, Boid #, s_x, s_y
print_data_2 = False #standard deviation, mean
print_array = False

#Startup
pygame.display.set_caption(caption)
update_rects = [[]]
fps = 120
frame_passed = 0
dev_values = []
current_boids = 0
to_average = []
msd_values = []
displacements = []

def intVector(v):
  return int(v.x), int(v.y)

class boid:
  size, degrees = boid_size, boid_angle
  limit = pygame.rect.Rect((0,0), display_rect.size-vector(-1, 1))
  limit.center = display_rect.center
  speed_lim, sightRange = max_speed, sight_range**2
  boids = []

  def __init__(self, pos=None, velocity=None):
    boidnum = 0
    if pos is None:
      if (randompos):
        pos = vector(random.random()*display_rect.w, random.random()*display_rect.h)
      else:
        pos = vector(s_ox, s_oy)

    self.pos = vector(pos)

    if velocity is None:
      self.velocity = vector(10, random.uniform(-1, 1))

    else:
      self.velocity = vector(velocity)
    self.prevPos, self.prevVelocity = vector(), vector()


  def __str__(self):
    return str(self.pos)+", "+str(self.velocity)
  
  @property
  def x(self):
    return self.pos.x
  
  @x.setter
  def x(self, value):
    self.pos.x = value
  
  @property
  def y(self):
    return self.pos.y
  
  @y.setter
  def y(self, value):
    self.pos.y = value
  
  def separation(self, others):
    others = [i for i in others if self.pos.distance_to(i.pos) < ideal_distance_from_other_boids]
    change = sum([self.pos - i.pos for i in others], vector())
    return change * separation_constant
  
  def alignment(self, others):
    change = sum([i.velocity for i in others], vector())/len(others) - self.velocity
    return change * alignment_constant
  
  def cohesion(self, others):
    change = sum([i.pos for i in others], vector())/len(others) - self.pos
    return change * cohesion_constant
  
  def edgePush(self):
    amount = max_turn
    if self.x < boid.limit.left:
      self.velocity.x += amount
    elif self.x > boid.limit.right:
      self.velocity.x -= amount
    if self.y < boid.limit.top:
      self.velocity.y += amount
    elif self.y > boid.limit.bottom:
      self.velocity.y -= amount

  def move(self):
    boidnum = 1
    self.prevPos, self.prevVelocity = vector(self.pos), vector(self.velocity)
    self.edgePush()
    others = [i for i in boid.boids if (i is not self and self.pos.distance_squared_to(i.pos)<boid.sightRange)]
    if others:
      self.velocity += sum(map(lambda x:getattr(self,x)(others), ["separation","alignment","cohesion"]), vector())
    if self.velocity.length_squared() > boid.speed_lim*boid.speed_lim:
      self.velocity.scale_to_length(boid.speed_lim)
    self.pos += self.velocity
  
  def draw(self, color=foreground):
    offset = self.velocity.normalize()*boid.size
    corner1 = offset.rotate(boid.degrees/2-180)+self.pos
    corner2 = offset.rotate(180-boid.degrees/2)+self.pos
    tip = 2*self.pos-corner1.lerp(corner2, 0.5)
    update_rects.append(pygame.draw.polygon(display, color, [*map(intVector, [tip, corner1, corner2])]))

  def trackframes():
    global frame_passed
    boidnum=1
    for boid1 in boid.boids:
      boidnum+=1
      if boidnum-1 == boids_generated:
        frame_passed+=1
        boidnum=1
        break

  def printdata1():
    global frame_passed, arr, rows, cols
    boidnum=1
    for boid1 in boid.boids:
      print(str(frame_passed) + ", " + str(boidnum) + ", " + str(boid1.pos[0]) + ", " + str(boid1.pos[1]))
      boidnum+=1

  def maketable():
    global frame_passed, arr, rows, cols    
    arr = [[0 for i in range(cols)] for j in range(rows)]

    for boid1 in boid.boids:
      y = int(boid1.pos[0]/(100)*rows/10)
      x = int(boid1.pos[1]/(100)*rows/10)

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

    for boid1 in boid.boids:    
      y = int(boid1.pos[0]/(100)*rows/10)
      x = int(boid1.pos[1]/(100)*rows/10)

      if (x > rows-1):
          x = rows-1
      if (y > rows-1):
          y = rows-1
      if (x < 0):
          x = 0
      if (y < 0):
          y = 0

      arr2[x][y] += 0.5

  def makedisplacements():
    for boid1 in boid.boids:    
        position = (boid1.pos)
        displacements.append(position)

  def msd():
    global startpos, to_average

    for i in range(startpos, len(displacements)-boids_generated):
        initial_pos = displacements[0]
        next_pos = displacements[i+boids_generated]
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
    plt.title("Boid Mean Squared Dispersion")
    plt.xlabel('Frames') 
    plt.ylabel('Mean Squared Dispersion') 
    plt.plot(x, y, color = 'b')
    plt.savefig("Boid Mean Squared Dispersion Graph.png")
    plt.close()

    y_p = np.diff(y) / np.diff(x)
    x_p = (np.array(x)[:-1] + np.array(x)[1:]) / 2

    x_p = np.insert(x_p, 0, 0)
    y_p = np.insert(y_p, 0, 0)

    plt.rcParams.update({'font.size':7})
    plt.title("Boid Mean Squared Dispersion Derivative / 2")
    plt.xlabel('Frames') 
    plt.ylabel('Mean Squared Dispersion Derivative / 2') 
    plt.plot(x_p, y_p, color = 'darkblue')
    plt.savefig("Boid Mean Squared Dispersion Derivative Graph.png")
    plt.close()


if (not infinite_boid):
  for i in range(boids_generated):
    boid.boids.append(boid())
    current_boids+=1

display.fill(background)
pygame.display.flip()
currentTime = pygame.time.get_ticks()

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
                  pygame.quit()
                  quit()
      display.blit(pause_text, textRect)
      pygame.display.update()
      clock.tick(fps)

if (print_data_1):
  print("Frame, Boid #, s_x, s_y")
if (print_data_2):
  print("Standard Deviation, Mean")

def dev():
    dev = np.var(arr)*current_boids
    dev_values.append(dev)
    mean = np.mean(arr)

def printdata2():
    dev = np.var(arr)*current_boids
    mean = np.mean(arr)
    print(str(dev) + ", " + str(mean))

def matrixmap():
  fig = plt.figure()
  ax = fig.add_subplot(111)
  cax = ax.matshow(arr, cmap='jet')
  fig.colorbar(cax)
  plt.title("Boid Concentration (Quit)")
  fig.savefig("Boid Concentration (Quit) Graph.png")
  plt.close()

def matrixmap2():
  fig = plt.figure()
  ax = fig.add_subplot(111)
  cax = ax.matshow(arr2, cmap='binary')
  plt.title("Boid Concentration (Full)")
  fig.colorbar(cax)
  fig.savefig("Boid Concentration (Full) Graph.png")
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
  plt.plot(x, y, color = 'r')
  plt.title("Boid Number Density Standard Deviation")
  plt.xlabel('Frames') 
  plt.ylabel('Standard Deviation') 
  plt.savefig("Boid Number Density Standard Deviation Graph.png")
  plt.close()

def update_fps():
    fps = "FPS: " + str(int(clock.get_fps()))
    fps_text = font.render(fps, 1, text_color)
    return fps_text

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

def quit_process():
  pyautogui.screenshot(region=(461,53, 990, 990)).save('Boid Simulation (Quit).png')
  devgraph()
  if (print_array):
    print("\n")
    for row in arr:
      print (row)
    print("\n")
  msdgraphs()
  matrixmap()
  matrixmap2()
  quit()

while True:
  clock.tick(-1)
  fps = clock.get_fps()
  
  if pygame.event.get(QUIT):
    quit_process()
    break
  for event in pygame.event.get():
    if event.type == KEYDOWN:
      if event.key == K_ESCAPE:
        quit_process()
      if event.key == pygame.K_p:
        pause()
      if event.key == pygame.K_o:
        pyautogui.screenshot(region=(461,53, 990, 990)).save('Boid Simulation (During).png')
  
  if (max_boids != 0):
    if (current_boids < max_boids):
      if (infinite_boid):
        for i in range(boids_generated):
          boid.boids.append(boid())
          current_boids+=1

  if (max_boids == 0):
    if (infinite_boid):
        for i in range(boids_generated):
          boid.boids.append(boid())
          current_boids+=1

  display.fill(background)
  boid.trackframes()

  prevTime, currentTime = currentTime, pygame.time.get_ticks()
  [*map(boid.move, boid.boids)]
  [*map(boid.draw, boid.boids)]

  dev()

  boid.maketable()
  boid.makedisplacements()
  boid.makefulltable()

  if(frame_passed >= 1):
    displacements.append([s_ox, s_oy])
    boid.msd() 

  if (print_data_1):
    boid.printdata1()

  if (print_data_2):
    printdata2()

  if (max_boids != 0):
      if (frame_passed*boids_generated == max_boids):
        pyautogui.screenshot(region=(461,53, 990, 990)).save('Boid Simulation (Ejection End).png')

  frames_passed_text = font.render(("Frames Passed: " + str(frame_passed) + "/" + str(quit_at_frame)), 1, text_color)
  current_boids_text = font.render(("Boids: " + str(current_boids)), 1, text_color)
  display.blit(update_fps(), (0,3))
  display.blit(current_boids_text, (0,3+text_size))
  display.blit(frames_passed_text, (0,3+text_size*2))
  if (quit_at_frame != 0):
    display.blit(update_time_left(), (0,3+text_size*3))

  if (quit_at_frame != 0):
    if (quit_at_frame == frame_passed-1):
      quit_process()

  pygame.display.update()

sys.stdout.close()
pygame.quit()

#Notes
#Do not move simulation window for correct screenshot; on Mac, minimize doc as much as possible
#The "standard deviation" formula for 