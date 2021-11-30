#cpsc3720

import pygame, sys, random, time,random
check_errors = pygame.init()

#make sure initializes correctly
if check_errors[1] > 0:
    print("(!) had {0} initializing errors, exiting....".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(!) PyGame Initialized Successfully")

pygame.init()

#use this to know if start screen or not
activeRouund = False
#starts here -> once press start say round
currentScreen = 'Start'

screen = pygame.display.set_mode((720, 460))
clock = pygame.time.Clock()
timer = 60
pygame.display.set_caption('\ (•◡•) / CHARADES \ (•◡•) /')
screen.fill((255,255,255))
pygame.display.flip()

buttonColor = (100,100,100)
screenW = screen.get_width()
screenH = screen.get_height()

font = pygame.font.SysFont('arial', 40)

#text for the button
nextButton = font.render('Next Card', True, buttonColor, (30, 45))

#cocntroller
fpsController = pygame.time.Clock()

timer_text = font.render(str(round(timer, 1)), True, (240, 248, 255))
#convert to seconds
dt = clock.tick(60)/1000

def mousePressend(event):
    if(activeRouund == 'Round'):
        #if next key pressed -> add draw a new card

#game logic
while True:
    for event in pygame.event.get():
        #quitting
        if event.type == pygame.QUIT: 
            pygame.quit()
        #if event.type == pygame.USEREVENT:
            #if mouse clicked on button go to specific card deck and start game 
        #in the game logic

#get the pos of the mouse so we can know which button
mouse = pygame.mouse.get_pos()

#place text onto next button - may need to change location
screen.blit(nextButton, (screenW/2+50, screenH/2))
pygame.display.flip()
clock.tick(60)
#way selecting through the genres - buttons
#selecting genre -> timer 1min per player, 

