#cpsc3720

import pygame, sys, random, time,random
check_errors = pygame.init()

#make sure initializes correctly
if check_errors[1] > 0:
    print("(!) had {0} initializing errors, exiting....".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(!) PyGame Initialized Successfully")


def set_font(self):
     """Set the font and its properties."""
     self.font = pygame.font.Font(self.fontname, self.fontsize)
     self.font.set_bold(self.bold)
     self.font.set_italic(self.italic)
     self.font.set_underline(self.underline)


playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('!!! CHARADES !!!')
playSurface.fill((255,255,255))
pygame.display.flip()

#cocntroller
fpsController = pygame.time.Clock()

#game logic
while True:
    for event in pygame.event.get():
        #quitting
        if event.type == pygame.QUIT: 
            pygame.quit()
        #in the game logic

#way selecting through the genres - buttons
#selecting genre -> timer 1min per player, 

