# import the appropriate libraries
import pygame, sys
from pygame.locals import *

# initialize pygame
pygame.init()

# set the screen and the default color
screen = pygame.display.set_mode((640,400))
WHITE = (255,255,255)
screen.fill(WHITE)

# create a label
myfont = pygame.font.SysFont("monospace",35)
label = myfont.render("congratulations",1,(255,55,0))

# add the label to the screen
screen.blit(label,(100,100))

# update the display
pygame.display.update()

# run the game loop; check this as long as the program is running
while True:
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
