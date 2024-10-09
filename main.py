import pygame
import numpy as np


# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True

#Settings
l = 1000
color_DOTS = (255,0,0)
color_CIRCLE = (0,255,0)
NUM_OF_DOTS = 100000

#Coordinates of dots and drawing the dots in. 
coordinates = np.random.rand(NUM_OF_DOTS,2) * l
def draw_dots(coordinates):
        for coord in coordinates:
            pygame.draw.circle(screen,color_DOTS,coord,1)
            

#Calculating Pi
def calc_Pi(coordinates):
    count = 0 
    for coord in coordinates: 
        if ((l/2 - coord[0])**2 + (l/2 - coord[1])**2 )**0.5 <= l/2:
            count+=1

    pi= (4 * ( count / NUM_OF_DOTS))
    print(pi)
    
  
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("blue")

    
    # RENDER BOX, CIRCLE
    pygame.draw.circle(screen,color_CIRCLE,(l/2,l/2), l/2)
    
    # DRAW dots     
    draw_dots(coordinates)   
    
       
    calc_Pi(coordinates)
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(10)  # limits FPS to 60

pygame.quit()