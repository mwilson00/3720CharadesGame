#cpsc3720

import pygame, sys, random, time
from database.database import Database
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

X = 720
Y = 460
screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption('\ (•◡•) / CHARADES \ (•◡•) /')
pygame.display.flip()

screenW = screen.get_width()
screenH = screen.get_height()

clock = 60
font = pygame.font.SysFont('arial', 30)
bigfont = pygame.font.SysFont('arial', 40)
smallFont = pygame.font.SysFont('arial', 20)
medFont = pygame.font.SysFont('arial', 25)

orange = (245, 102,0)
blue = (0, 32, 91)
purple = (46,26,71)

db = Database()

class ToggleButton:
    def __init__(self, iName, xPos = 0, yPos = 0):
        self.toggle = False
        self.name = iName ; self.x = xPos; self.y = yPos
        text = font.render(self.name, True, orange)

        bt = text.get_rect()
        bt.midbottom = self.x + 50, self.y + 40
        pygame.draw.rect(screen, purple,[self.x - 25,self.y, 145,40])
        screen.blit(text, bt)

    def inBounds(self, mouse):
        if self.x - 25 <= mouse[0] <= self.x + 120 and self.y <= mouse[1] <= self.y + 40:
            self.toggle = not self.toggle
            self.color()
            
    def color(self):
        text = font.render(self.name, True, orange)
        bt = text.get_rect()
        bt.midbottom = self.x + 50, self.y + 40
        RectColor = blue if self.toggle == True else purple
        pygame.draw.rect(screen, RectColor,[self.x - 25,self.y, 145,40])
        screen.blit(text, bt)

class Button:
    def __init__(self, iName, xPos = 0, yPos = 0):
        self.name = iName ; self.x = xPos; self.y = yPos
        self.count = 0 
        text = font.render(self.name, True, orange)

        bt = text.get_rect()
        bt.midbottom = self.x + 50, self.y + 40
        pygame.draw.rect(screen, purple,[self.x - 25,self.y, 145,40])
        screen.blit(text, bt)

    def inBounds(self, mouse):
        if self.x - 25 <= mouse[0] <= self.x + 120 and self.y <= mouse[1] <= self.y + 40:
            return True 
        return False
            
    def color(self):
        text = font.render(self.name, True, orange)
        bt = text.get_rect()
        bt.midbottom = self.x + 50, self.y + 40
        pygame.draw.rect(screen, purple,[self.x - 25,self.y, 145,40])
        screen.blit(text, bt)

histButton = ToggleButton('History', 500, 200)
celebButton = ToggleButton('Celebrity', 300, 200)
movieButton = ToggleButton('Movies', 100, 200)
submitButton = Button('Submit', 300, 300)

def startScreen(event, mouse):
    menuTitle = bigfont.render('Charades!', True, purple)
    menuRect = menuTitle.get_rect()
    menuRect.midtop = (360, 10)
    screen.blit(menuTitle, menuRect)

    histButton.color()
    celebButton.color()
    movieButton.color()
    submitButton.color()

    breakLoop = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        histButton.inBounds(mouse)
        celebButton.inBounds(mouse)
        movieButton.inBounds(mouse)
        breakLoop = submitButton.inBounds(mouse)

    if breakLoop:
        return db.get_cards([i.name for i in [histButton, celebButton, movieButton] if i.toggle])
    
    return None

def activeRound():
    active = font.render('ACTIVE ROUND', True, purple) 
    activeRect = active.get_rect()
    activeRect.midtop = (360, 15)
    screen.blit(active, activeRect) 
    instructions = smallFont.render('Act out the word below', True, purple) 
    instructionsRect = instructions.get_rect()
    instructionsRect.midtop = (360, 50)
    screen.blit(instructions, instructionsRect) 

nextCardBT = Button('Next Card', screenW/2 - 45,screenH/2+85)

def nextCardButton():
    nextCardBT.color()

def currentCard(sg, ind):
    cardLabel = 'No More Cards!' if ind >= len(sg) else sg[ind]
    currCard = font.render( cardLabel, True, blue) 
    currCardRect = currCard.get_rect()
    currCardRect.midtop = (X/2, Y/2-40)
    screen.blit(currCard, currCardRect) 

#cocntroller
fpsController = pygame.time.Clock()

# sets timer to activate once per 1000 ms
pygame.time.set_timer(pygame.USEREVENT, 0)
inMain = True ; count = 0 
#game logic
while True:
    fpsController.tick(30)
    screen.fill((255,255,255))
    #the timer

    for event in pygame.event.get():
        #quitting
        if event.type == pygame.QUIT: 
            pygame.quit()

        # condition to catch timer activation
        elif event.type == pygame.USEREVENT:
            clock -= 1
            # condition to stop timer at 0
            if clock <= 0:
                clock = 0 ; pygame.time.set_timer(pygame.USEREVENT, 0)
        
        #get the pos of the mouse so we can know which button
        mouse = pygame.mouse.get_pos()

        if inMain:
            selectedGenres = startScreen(event, mouse)
            if selectedGenres is not None:
                inMain = False
            
        if not inMain:
            pygame.time.set_timer(pygame.USEREVENT, 1000)
            activeRound()
            timer = medFont.render('Time left: ' + str(clock), True, orange)
            screen.blit(timer, (290, 75))

            if event.type == pygame.MOUSEBUTTONDOWN and nextCardBT.inBounds(mouse):
                count += 1
            
            # restarts timer at 60 on key [r] pressed 
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                clock = 60 ; pygame.time.set_timer(pygame.USEREVENT, 1000)  

            nextCardButton()
            currentCard(selectedGenres, count)

        pygame.display.update()

#way selecting through the genres - buttons
#selecting genre -> timer 1min per player, 

