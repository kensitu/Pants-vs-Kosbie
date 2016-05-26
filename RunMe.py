import pygame, random, sys, time
from pygame.locals import *
import inputbox
import save
import level1, level2, level3, level4, level5, level6

pygame.init()
fpsClock = pygame.time.Clock()

#sets up window
WINDOWWIDTH = 1100
WINDOWHEIGHT = 600
window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Pants vs. Kosbie')

bgImg = pygame.image.load( 'Graphics/bg.png')
pantsImg = pygame.image.load('Graphics/hd pants copy.png')
storySignImg = pygame.image.load('Graphics/storymode sign.png')
storySignHoverImg = pygame.image.load('Graphics/storymode sign hover.png')
storySignClickedImg = pygame.image.load('Graphics/storymode sign clicked.png')
tutSignImg = pygame.image.load('Graphics/tutorialsign.png')
tutSignHoverImg = pygame.image.load('Graphics/tutorialsign hover.png')
tutSignClickedImg = pygame.image.load('Graphics/tutorialsign clicked.png')
freeSignImg = pygame.image.load('Graphics/freeplay sign.png')
freeSignHoverImg = pygame.image.load('Graphics/freeplay sign hover.png')
freeSignClickedImg = pygame.image.load('Graphics/freeplay sign clicked.png')
kosbieImg = pygame.image.load('Graphics/kosbie body.png')
kosbie2Img = pygame.image.load('Graphics/kosbie body 2.png')
speechImg = pygame.image.load('Graphics/hatepantsspeech.png')

font = pygame.font.SysFont(None, 30)

def drawText(text, font, surface, x, y, color):
    #func taken from http://www.pygame.org/project-Plants+vs+Zombies-2632-.html
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

#runs the level based off the input given
def level(progress, user):
    if progress == '1':
        level1.play(user)
    elif progress == '2':
        level2.play(user)
    elif progress == '3':
        level3.play(user)
    elif progress == '4':
        level4.play(user)
    elif progress == '5':
        level5.play(user)
    elif progress == '6':
        level6.play(user)

class storySign(object):
    def __init__(self):
        y = 410
        x = 420
        sizeX = 291
        sizeY = 54

        self.rect = pygame.Rect(x, y, sizeX, sizeY)
        self.surface = storySignImg

    def hover(self):
        self.surface = storySignHoverImg

    def clicked(self):
        self.surface = storySignClickedImg

    def reset(self):
        self.surface = storySignImg

class tutSign(object):
    def __init__(self):
        y = 460
        x = 420
        sizeX = 291
        sizeY = 54

        self.rect = pygame.Rect(x, y, sizeX, sizeY)
        self.surface = tutSignImg

    def hover(self):
        self.surface = tutSignHoverImg

    def clicked(self):
        self.surface = tutSignClickedImg

    def reset(self):
        self.surface = tutSignImg

class freeSign(object):
    def __init__(self):
        y = 510
        x = 420
        sizeX = 291
        sizeY = 54

        self.rect = pygame.Rect(x, y, sizeX, sizeY)
        self.surface = freeSignImg

    def hover(self):
        self.surface = freeSignHoverImg

    def clicked(self):
        self.surface = freeSignClickedImg

    def reset(self):
        self.surface = freeSignImg

class kosbie(object):
    def __init__(self):
        x = 900
        y = 44
        sizeX = 172
        sizeY = 511
        self.rect = pygame.Rect(x,y,sizeX,sizeY)
        self.surface = kosbieImg

    def update(self):
        self.surface = kosbie2Img
        window.blit(speechImg, (720,105))



class pants(object):
    def __init__(self):
        self.x = -105
        self.y = 220
        self.sizeX = 210/2
        self.sizeY = 378/2
        self.rect = pygame.Rect(self.x,self.y,self.sizeX,self.sizeY)
        self.surface = pantsImg

    def update(self):
        self.x += 6
        self.y += 4
        self.rect = pygame.Rect(self.x,self.y,self.sizeX,self.sizeY)
        if self.y > WINDOWHEIGHT:
            self.x = -165
            self.y = 260

#took inputbox from online
answer = inputbox.ask(window, "Who are you?")

# Tracks progress depending on the player
try:
    progress = save.read(answer)
except:
    progress = '1'

pant = pants()
kosbieObj = kosbie()
pygame.mixer.music.load('Sounds/music.ogg')
pygame.mixer.music.play(-1, 0.0)


while True:
    window.blit(bgImg ,(0,0))
    signs = []

    sign1 = storySign()
    signs.append(sign1)

    sign2 = tutSign()
    signs.append(sign2)

    sign3 = freeSign()
    signs.append(sign3)

    pant.update()

    x,y = pygame.mouse.get_pos()
    for s in signs:
        if s.rect.collidepoint(x,y):
            s.hover()
            kosbieObj.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            for s in signs:
                if s.rect.collidepoint(x,y):
                    s.clicked()
                    if type(s) == storySign:
                        level(progress, answer)
                    elif type(s) == tutSign:
                        import tutorial
                    else:
                        import freeplay

    offset = len(answer) * 3 #offsets the center for long names
    drawText(answer, font, window, WINDOWWIDTH/2 - offset, 368, (255,255,255))
    for s in signs:
        window.blit(s.surface, s.rect)
    window.blit(pant.surface, pant.rect)
    window.blit(kosbieObj.surface, kosbieObj.rect)
    pygame.display.update()

