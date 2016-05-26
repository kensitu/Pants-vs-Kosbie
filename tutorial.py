import pygame, random, sys, time
from pygame.locals import *

#used http://www.pygame.org/project-Plants+vs+Zombies-2632-.html
#as base

#sets up pygame
pygame.init()
fpsClock = pygame.time.Clock()

font = pygame.font.SysFont(None, 30)

#sets up window
WINDOWWIDTH = 1120
WINDOWHEIGHT = 600
window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Pants vs. Kosbie')

#sets up images
emptySeedImg = pygame.image.load('Graphics/empty_seed.png')
background1 = pygame.image.load('Graphics/Frontyard.jpg')
zombieImage = pygame.image.load('Graphics/pants.png')
peashooterImg = pygame.image.load('Graphics/Pea_Shooter copy.png')
peashooterSeedImg = pygame.image.load('Graphics/PeashooterSeed.png')
peashooterBulletImg = pygame.image.load('Graphics/Pea_Shooter_Bullet.png')
sunImg = pygame.image.load('Graphics/Sun.png')
selectedSlotImg = pygame.image.load('Graphics/selected.png')
sunCounterImg = pygame.image.load('Graphics/sun_counter.png')
wallnutImg = pygame.image.load('Graphics/wallnut.png')
wallnutCracked1Img = pygame.image.load('Graphics/Wallnut_cracked1.png')
wallnutCracked2Img = pygame.image.load('Graphics/Wallnut_cracked2.png')
wallnutSeedImg = pygame.image.load('Graphics/WallNutSeed.png')
sunflowerImg = pygame.image.load('Graphics/sunflower.png')
sunflowerSeedImg = pygame.image.load('Graphics/SunflowerSeed.png')
repeaterImg = pygame.image.load('Graphics/Repeater.png')
repeaterSeedImg = pygame.image.load('Graphics/RepeaterSeed.png')
snowpeaImg = pygame.image.load('Graphics/Snowpea.png')
snowpeaSeedImg = pygame.image.load('Graphics/SnowpeaSeed.png')
snowpeaBulletImg = pygame.image.load('Graphics/SnowpeaBullet.png')
frozenZombieImg = pygame.image.load('Graphics/frozen pants.png')
cherryBombImg = pygame.image.load('Graphics/Cherrybomb.png')
cherryBomb2Img = pygame.image.load('Graphics/Cherrybomb2.png')
cherryBombSeedImg = pygame.image.load('Graphics/CherrybombSeed.png')
cherryBombExpImg = pygame.image.load('Graphics/Cherryexplosion.png')
pmineImg = pygame.image.load('Graphics/pmine1.png')
pmine2Img = pygame.image.load('Graphics/pmine2.png')
pmineSeedImg = pygame.image.load('Graphics/pmine seed.png')
pmineExpImg = pygame.image.load('Graphics/PotatoMine_mashed.png')
jeansImg = pygame.image.load('Graphics/jeans.png')
frozenJeansImg = pygame.image.load('Graphics/jeans frozen.png')
kosbieNoPantsImg = pygame.image.load('Graphics/small kosbie.png')
kosbieKhakisImg = pygame.image.load('Graphics/small kosbie khakis.png')
kosbieJeansImg = pygame.image.load('Graphics/small kosbie jeans.png')
shortsImg = pygame.image.load('Graphics/shorts.png')
frozenShortsImg = pygame.image.load('Graphics/frozen shorts.png')
kosbieShortsImg = pygame.image.load('Graphics/small kosbie shorts.png')
shovelImg = pygame.image.load('Graphics/shovel.png')
shovelSelectedImg = pygame.image.load('Graphics/shovel selected.png')
kosbieCutsceneImg = pygame.image.load('Graphics/kosbie cutscene.png')
kosbieSadCutsceneImg = pygame.image.load('Graphics/kosbie cutscene sad.png')
speechBoxImg = pygame.image.load('Graphics/speechbox.png')

tutorialmap = pygame.image.load('Graphics/tutorialmap.jpg')
arrowLeftImg = pygame.image.load('Graphics/arrowleft.png')
arrowDownImg = pygame.image.load('Graphics/arrowdown.png')

#sets up sounds
#sounds from freesound.org

hitSound = pygame.mixer.Sound('Sounds/splat.ogg')
plantingSound = pygame.mixer.Sound('Sounds/planting.wav')
sunSound = pygame.mixer.Sound('Sounds/sun.ogg')
owSound = pygame.mixer.Sound('Sounds/ow.ogg')
explosionSound = pygame.mixer.Sound('Sounds/explosion.ogg')
smExplosionSound = pygame.mixer.Sound('Sounds/small explosion.ogg')


def drawText(text, font, surface, x, y, color):
    #taken from http://www.pygame.org/project-Plants+vs+Zombies-2632-.html
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def findRowCol(x, y):
    cellH = 98
    cellW = 82
    top = 84
    left = 252
    bottom = 574
    right = 995
    if x < left or y < top:
        return None, None
    elif x > right or y > bottom:
        return None, None
    else:
        return (y - top) / cellH, (x - left) / cellW

def checkIfBaddieInRow(myRow, baddieList):
    for b in baddieList:
        if b.row == myRow:
            return True
    return False 

class shovel(object):
    def __init__(self):
        slotH = 57
        offset = 21
        y = 25
        x = 230

        sizeX = 72
        sizeY = 47
        self.rect = pygame.Rect(x, y, sizeX, sizeY)
        self.surface = pygame.transform.scale(shovelImg, (sizeX,sizeY))
        self.selected = False

    def select(self):
        self.selected = True
        shovelObj.surface = shovelSelectedImg

    def deselect(self):
        self.selected = False
        shovelObj.surface = shovelImg

class kosbie(object):
    def __init__(self):
        self.x = 190
        self.y = 170
        self.sizeX = 55
        self.sizeY = 163
        self.rect = pygame.Rect(self.x,self.y,self.sizeX,self.sizeY)
        self.surface = kosbieNoPantsImg
        self.walkingDown = True
        self.patrolTop = 170
        self.patrolBot = 320

    def update(self, baddietype):
        if baddietype == jeans:
            self.surface = kosbieJeansImg
        elif baddietype == zombie:
            self.surface = kosbieKhakisImg
        elif baddietype == shorts:
            self.surface = kosbieShortsImg

class field(object):
    def __init__(self):
        self.rows = 5
        self.cols = 9
        self.board = []
        for row in xrange(self.rows): self.board += [[None]*self.cols]

class sun(object):
    def __init__(self, natural, x=None, y=None):
        if natural:
            left = 252
            right = 995
            self.x = random.randint(left, right)
            self.y = 0
            top = 126
            bottom = 560
            self.endY = random.randint(top, bottom)
            self.speed = random.randint(1,2)
            self.life = 0
            self.lifeSpan = 200
            size = 30 #######42
            self.rect = pygame.Rect(self.x, self.y, size, size)
            self.surface = pygame.transform.scale(sunImg, (size, size))
        else:
            xOffset = 14
            self.x = x + xOffset
            self.y = y
            self.endY = y + 42
            self.speed = 1
            self.life = 0
            self.lifeSpan = 200
            size = 30#####42
            self.rect = pygame.Rect(self.x, self.y, size, size)
            self.surface = pygame.transform.scale(sunImg, (size, size))

class peashooterPacket(object):
    def __init__(self, slot):
        self.cost = 100
        self.slot = slot
        slotH = 57
        offset = 21
        y = slot * slotH + offset
        x = 20
        sizeX = 76
        sizeY = 47
        self.rect = pygame.Rect(x, y, sizeX, sizeY)
        self.surface = pygame.transform.scale(peashooterSeedImg, (sizeX,sizeY))

    def makeNewPlant(self, row, col):
        return peashooter(row, col)

class peashooterBullet(object):
    def __init__(self, x, y):
        self.speed = 15
        self.size = 24
        xOffset = 40
        self.x = x + xOffset
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.surface = pygame.transform.scale(peashooterBulletImg, (self.size,self.size))

class peashooter(object):
    def __init__(self, row, col):
        self.health = 75
        self.cost = 100
        self.row = row
        self.col = col
        self.size = 56
        cellW = 80
        cellH = 98
        xOffset = 260
        yOffset = 90
        self.x = (col * cellW) + xOffset
        self.y= (row* cellH) + yOffset
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.surface = pygame.transform.scale(peashooterImg, (self.size, self.size))
        self.curBullet = None
        self.lastShot = time.time()

    def shoot(self, bulletList, baddieList):
        timeSinceLastShot = time.time() - self.lastShot 
        if not checkIfBaddieInRow(self.row, baddieList):
            pass
        elif self.curBullet == None and timeSinceLastShot > 1:
            self.lastShot = time.time()
            bullet = peashooterBullet(self.x, self.y)
            bulletList.append(bullet)
            self.curBullet = bullet
        else:
            if self.curBullet not in bulletList:
                self.curBullet = None

class sunflowerPacket(object):
    def __init__(self, slot):
        self.cost = 50
        self.slot = slot
        slotH = 57
        offset = 21
        y = slot * slotH + offset
        x = 20
        sizeX = 76
        sizeY = 48
        self.rect = pygame.Rect(x, y, sizeX, sizeY)
        self.surface = pygame.transform.scale(sunflowerSeedImg, (sizeX,sizeY))

    def makeNewPlant(self, row, col):
        return sunflower(row, col)

class sunflower(object):
    def __init__(self, row, col):
        self.health = 75
        self.cost = 50
        self.row = row
        self.col = col
        self.fireRate = 50
        self.sizeX = 60
        self.sizeY = 63
        cellW = 79
        cellH = 98
        xOffset = 270
        yOffset = 88
        self.top = (col * cellW) + xOffset
        self.left= (row * cellH) + yOffset
        self.rect = pygame.Rect(self.top, self.left, self.sizeX, self.sizeY)
        self.surface = pygame.transform.scale(sunflowerImg, (self.sizeX,self.sizeY))
        self.timeAlive = 0

    def update(self, zlist):
        self.timeAlive += 1
        if self.timeAlive == self.fireRate:
            self.timeAlive = 0
            newSun = sun(False, self.top, self.left)
            sunList.append(newSun)

class zombie(object):
    def __init__(self,row,spawnTime):
        self.health = 12
        self.normalSpeed = 1
        self.speed = self.normalSpeed
        self.sizeX = 56
        self.sizeY = 100
        self.row = row
        self.spawnTime = spawnTime

        cellH = 98
        yOffset = 56
        self.x = WINDOWWIDTH
        self.y = (self.row* cellH) + yOffset


        self.rect = pygame.Rect(self.x, self.y, self.sizeX, self.sizeY)
        self.surface = pygame.transform.scale(zombieImage, (self.sizeX,self.sizeY))
        self.eating = False
        self.frozen = False
        self.frozenSpeed = 1
        self.thawTimer = 0
        self.thawTime = 60

    def checkIfHit(self, bulletList):
        for b in bulletList:
            if b.rect.colliderect(self.rect):
                hitSound.play()
                bulletList.remove(b)
                self.health -= 1

    def checkIfEat(self,plantsList, board):
        collision = self.rect.collidelist(plantsList)
        if collision != -1:
            for p in plantsList:
                if p.rect.colliderect(self.rect):
                    if self.row == p.row:
                        self.eating = True
                        p.health -= 1
                        owSound.play()
                        if p.health <= 0:
                            board[p.row][p.col] = None
                            plantsList.remove(p)
                            self.eating = False
                    else: self.eating = False
        else: self.eating = False

    def update(self):
        if self.frozen:
            self.speed = self.frozenSpeed
            self.thawTimer += 1
            self.surface = pygame.transform.scale(frozenZombieImg, (self.sizeX,self.sizeY))
            if self.thawTimer == self.thawTime:
                self.thawTime = 0
                self.frozen = False
                self.speed = self.normalSpeed
                self.surface = pygame.transform.scale(zombieImage, (self.sizeX,self.sizeY))

class jeans(object):
    def __init__(self,row,spawnTime):
        self.health = 25
        self.normalSpeed = 1
        self.frozenSpeed = 1

        self.speed = self.normalSpeed
        self.sizeX = 56
        self.sizeY = 100
        self.row = row
        self.spawnTime = spawnTime


        cellH = 98
        yOffset = 56
        self.x = WINDOWWIDTH
        self.y = (self.row* cellH) + yOffset

        self.rect = pygame.Rect(self.x, self.y, self.sizeX, self.sizeY)
        self.surface = pygame.transform.scale(jeansImg, (self.sizeX,self.sizeY))
        self.eating = False
        self.frozen = False
        self.thawTimer = 0
        self.thawTime = 60

    def checkIfHit(self, bulletList):
        for b in bulletList:
            if b.rect.colliderect(self.rect):
                if type(b) == snowpeaBullet:
                    self.thawTimer = 0
                    self.frozen = True
                hitSound.play()
                bulletList.remove(b)
                self.health -= 1

    def checkIfEat(self,plantsList, board):
        collision = self.rect.collidelist(plantsList)
        if collision != -1:
            for p in plantsList:
                if p.rect.colliderect(self.rect):
                    if self.row == p.row:
                        self.eating = True
                        p.health -= 1
                        owSound.play()
                        if p.health <= 0:
                            board[p.row][p.col] = None
                            plantsList.remove(p)
                            self.eating = False
                    else: self.eating = False
        else: self.eating = False

    def update(self):
        if self.frozen:
            self.speed = self.frozenSpeed
            self.thawTimer += 1
            self.surface = pygame.transform.scale(frozenJeansImg, (self.sizeX,self.sizeY))
            if self.thawTimer == self.thawTime:
                self.thawTimer = 0
                self.frozen = False
                self.speed = self.normalSpeed
                self.surface = pygame.transform.scale(jeansImg, (self.sizeX,self.sizeY))

class shorts(object):
    def __init__(self,row,spawnTime):
        self.health = 5
        self.normalSpeed = 3
        self.frozenSpeed = 1

        self.speed = self.normalSpeed
        self.sizeX = 62
        self.sizeY = 75
        self.row = row
        self.spawnTime = spawnTime

        cellH = 98
        yOffset = 56

        self.x = WINDOWWIDTH
        self.y = (self.row* cellH) + yOffset

        self.rect = pygame.Rect(self.x, self.y, self.sizeX, self.sizeY)
        self.surface = pygame.transform.scale(shortsImg, (self.sizeX,self.sizeY))
        self.eating = False
        self.frozen = False
        self.thawTimer = 0
        self.thawTime = 60

    def checkIfHit(self, bulletList):
        for b in bulletList:
            if b.rect.colliderect(self.rect):
                if type(b) == snowpeaBullet:
                    self.thawTimer = 0
                    self.frozen = True
                hitSound.play()
                bulletList.remove(b)
                self.health -= 1

    def checkIfEat(self,plantsList, board):
        collision = self.rect.collidelist(plantsList)
        if collision != -1:
            for p in plantsList:
                if p.rect.colliderect(self.rect):
                    if self.row == p.row:
                        self.eating = True
                        p.health -= 1
                        owSound.play()
                        if p.health <= 0:
                            board[p.row][p.col] = None
                            plantsList.remove(p)
                            self.eating = False
                    else: self.eating = False
        else: self.eating = False

    def update(self):
        if self.frozen:
            self.speed = self.frozenSpeed
            self.thawTimer += 1
            self.surface = pygame.transform.scale(frozenShortsImg, (self.sizeX,self.sizeY))
            if self.thawTimer == self.thawTime:
                self.thawTimer = 0
                self.frozen = False
                self.speed = self.normalSpeed
                self.surface = pygame.transform.scale(shortsImg, (self.sizeX,self.sizeY))

# spawnList = [
#              zombie(3, 400), 
#              zombie(1, 800), 
#              zombie(2, 1100), 
#              zombie(3, 1200),
#              zombie(0, 1350), 
#              zombie(4, 1450), 
#              zombie(0, 1550), 
#              zombie(2, 1630),
#              zombie(0, 1650), 
#              zombie(4, 1700), 
#              zombie(4, 1750), 
#              zombie(3, 1800)]

spawnList = [zombie(2, 1), 
             shorts(2,10)]

pygame.mixer.music.load('Sounds/grasswalk.ogg')
pygame.mixer.music.play(-1, 0.0)

def round1():
    curSpeech = 0

    baddieList = []
    bulletList = []
    plantsList = []
    sunList = []

    slotList = []
    slotList.append(sunflowerPacket(0))

    curSelectedSlot = None
    curSun = 50
    kosbieObj = kosbie()

    while True:
        speech = 'Graphics/tspeech' + str(curSpeech) + '.png'
        
        if curSpeech < 2:
            speechImg = pygame.image.load(speech)
        else:
            break

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_SPACE:
                    curSpeech += 1

        # Draw the game world on the window.
        window.blit(tutorialmap, (0, 0))

        window.blit(speechImg, (270,10))

        # Draw the counter background for the sun
        counterBgX = 110
        counterBgY = 25
        window.blit(sunCounterImg, (counterBgX, counterBgY))

        # Draw the actual counter 
        white = (255, 255, 255)
        counterx = 144
        countery = 30
        drawText(str(curSun), font, window, counterx, countery, white)

        # Draw Kosbie
        window.blit(kosbieObj.surface, kosbieObj.rect)

        # Draw each baddie
        for z in baddieList:
            window.blit(z.surface, z.rect)

        # Draw each bullet
        for b in bulletList:
            window.blit(b.surface, b.rect)

        # Draw each plant
        for p in plantsList:
            window.blit(p.surface, p.rect)

        # Draw each sun
        for s in sunList:
            window.blit(s.surface, s.rect)

        # Draw each slot
        for s in slotList:
            window.blit(s.surface, s.rect)

        # Draw selected slot
        if curSelectedSlot != None:

            x = 20
            slotH = 57
            offset = 21
            y = (curSelectedSlot * slotH) + offset
            window.blit(selectedSlotImg, (x, y))

        pygame.display.update()

def round2():
    curSpeech = 2

    baddieList = []
    bulletList = []
    plantsList = []
    plantsList.append(sunflower(2,0))
    sunList = []

    slotList = []
    slotList.append(sunflowerPacket(0))

    curSelectedSlot = None
    curSun = 0
    kosbieObj = kosbie()

    while True:
        speech = 'Graphics/tspeech' + str(curSpeech) + '.png'
        
        if curSpeech < 4:
            speechImg = pygame.image.load(speech)
        else:
            break

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_SPACE:
                    curSpeech += 1

        # Draw the game world on the window.
        window.blit(tutorialmap, (0, 0))

        window.blit(speechImg, (270,10))

        # Draw the counter background for the sun
        counterBgX = 110
        counterBgY = 25
        window.blit(sunCounterImg, (counterBgX, counterBgY))

        # Draw the actual counter 
        white = (255, 255, 255)
        counterx = 144
        countery = 30
        drawText(str(curSun), font, window, counterx, countery, white)

        # Draw Kosbie
        window.blit(kosbieObj.surface, kosbieObj.rect)

        # Draw each baddie
        for z in baddieList:
            window.blit(z.surface, z.rect)

        # Draw each bullet
        for b in bulletList:
            window.blit(b.surface, b.rect)

        # Draw each plant
        for p in plantsList:
            window.blit(p.surface, p.rect)

        # Draw each sun
        for s in sunList:
            window.blit(s.surface, s.rect)

        # Draw each slot
        for s in slotList:
            window.blit(s.surface, s.rect)

        # Draw selected slot
        if curSelectedSlot != None:

            x = 20
            slotH = 57
            offset = 21
            y = (curSelectedSlot * slotH) + offset
            window.blit(selectedSlotImg, (x, y))

        pygame.display.update()

def round3():
    curSpeech = 4

    baddieList = []
    baddieList.append(sunflower(2,0))
    bulletList = []
    plantsList = []
    sunList = []

    slotList = []
    slotList.append(sunflowerPacket(0))

    curSelectedSlot = None
    curSun = 100
    kosbieObj = kosbie()

    while True:
        speech = 'Graphics/tspeech' + str(curSpeech) + '.png'
        
        if curSpeech < 5:
            speechImg = pygame.image.load(speech)
        else:
            break

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_SPACE:
                    curSpeech += 1

        # Draw the game world on the window.
        window.blit(tutorialmap, (0, 0))

        window.blit(speechImg, (270,10))

        # Draw the counter background for the sun
        counterBgX = 110
        counterBgY = 25
        window.blit(sunCounterImg, (counterBgX, counterBgY))

        # Draw the actual counter 
        white = (255, 255, 255)
        counterx = 144
        countery = 30
        drawText(str(curSun), font, window, counterx, countery, white)

        # Draw Kosbie
        window.blit(kosbieObj.surface, kosbieObj.rect)

        # Draw each baddie
        for z in baddieList:
            window.blit(z.surface, z.rect)

        # Draw each bullet
        for b in bulletList:
            window.blit(b.surface, b.rect)

        # Draw each plant
        for p in plantsList:
            window.blit(p.surface, p.rect)

        # Draw each sun
        for s in sunList:
            window.blit(s.surface, s.rect)

        # Draw each slot
        for s in slotList:
            window.blit(s.surface, s.rect)

        # Draw selected slot
        if curSelectedSlot != None:

            x = 20
            slotH = 57
            offset = 21
            y = (curSelectedSlot * slotH) + offset
            window.blit(selectedSlotImg, (x, y))

        pygame.display.update()

def round4(curSun, plantsList, slotList):
    curSpeech = 5

    baddieList = []
    baddieList.append(sunflower(2,0))
    bulletList = []
    sunList = []

    slotList.append(sunflowerPacket(0))

    curSelectedSlot = None
    kosbieObj = kosbie()

    while True:
        speech = 'Graphics/tspeech' + str(curSpeech) + '.png'
        
        if curSpeech < 8:
            speechImg = pygame.image.load(speech)
        else:
            break

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_SPACE:
                    curSpeech += 1

        # Draw the game world on the window.
        window.blit(tutorialmap, (0, 0))

        window.blit(speechImg, (270,10))

        # Draw the counter background for the sun
        counterBgX = 110
        counterBgY = 25
        window.blit(sunCounterImg, (counterBgX, counterBgY))

        # Draw the actual counter 
        white = (255, 255, 255)
        counterx = 144
        countery = 30
        drawText(str(curSun), font, window, counterx, countery, white)

        # Draw Kosbie
        window.blit(kosbieObj.surface, kosbieObj.rect)

        # Draw each baddie
        for z in baddieList:
            window.blit(z.surface, z.rect)

        # Draw each bullet
        for b in bulletList:
            window.blit(b.surface, b.rect)

        # Draw each plant
        for p in plantsList:
            window.blit(p.surface, p.rect)

        # Draw each sun
        for s in sunList:
            window.blit(s.surface, s.rect)

        # Draw each slot
        for s in slotList:
            window.blit(s.surface, s.rect)

        # Draw selected slot
        if curSelectedSlot != None:

            x = 20
            slotH = 57
            offset = 21
            y = (curSelectedSlot * slotH) + offset
            window.blit(selectedSlotImg, (x, y))

        pygame.display.update()

def round5(curSun, slotList):
    curSpeech = 8

    baddieList = []
    bulletList = []
    sunList = []
    plantsList = []

    slotList.append(sunflowerPacket(0))

    curSelectedSlot = None
    kosbieObj = kosbie()

    while True:
        speech = 'Graphics/tspeech' + str(curSpeech) + '.png'
        
        if curSpeech < 10:
            speechImg = pygame.image.load(speech)
        else:
            import RunMe

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_SPACE:
                    curSpeech += 1

        # Draw the game world on the window.
        window.blit(tutorialmap, (0, 0))

        window.blit(speechImg, (270,10))

        # Draw the counter background for the sun
        counterBgX = 110
        counterBgY = 25
        window.blit(sunCounterImg, (counterBgX, counterBgY))

        # Draw the actual counter 
        white = (255, 255, 255)
        counterx = 144
        countery = 30
        drawText(str(curSun), font, window, counterx, countery, white)

        # Draw Kosbie
        window.blit(kosbieObj.surface, kosbieObj.rect)

        # Draw each baddie
        for z in baddieList:
            window.blit(z.surface, z.rect)

        # Draw each bullet
        for b in bulletList:
            window.blit(b.surface, b.rect)

        # Draw each plant
        for p in plantsList:
            window.blit(p.surface, p.rect)

        # Draw each sun
        for s in sunList:
            window.blit(s.surface, s.rect)

        # Draw each slot
        for s in slotList:
            window.blit(s.surface, s.rect)

        # Draw selected slot
        if curSelectedSlot != None:

            x = 20
            slotH = 57
            offset = 21
            y = (curSelectedSlot * slotH) + offset
            window.blit(selectedSlotImg, (x, y))

        pygame.display.update()


while True:
    round1()
    curSpeech = 0
    sunSpawnRate = 150
    sunAddCounter = 0
    sunValue = 25

    baddieList = []
    bulletList = []
    plantsList = []
    sunList = []

    slotList = []
    slotList.append(sunflowerPacket(0))

    curSelectedSlot = None
    curSun = 50
    kosbieObj = kosbie()
    shovelObj = shovel()
    gameField = field()

    #tracks progress into the tutorial
    hasPlantedYet = False
    hasSpokenSunflowerYet = False
    hasReached100Yet = False
    hasKilledBaddieYet = False
    hasSpokenShovelYet = False
    hasUsedShovelYet = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONUP:
                mouseX, mouseY = pygame.mouse.get_pos()
                rowClicked, colClicked = findRowCol(mouseX,mouseY)

                if shovelObj.selected:
                    if rowClicked != None and colClicked != None:
                        if gameField.board[rowClicked][colClicked] == None:
                            shovelObj.deselect()
                        else:
                            plantsList.remove(gameField.board[rowClicked][colClicked])
                            gameField.board[rowClicked][colClicked] = None
                            shovelObj.deselect()

                    elif shovelObj.rect.collidepoint(mouseX, mouseY):
                        #can ignore this case. We deselect later to avoid
                        #conflictions between the two deselects.
                        pass

                    else:
                        shovelObj.deselect()

                elif curSelectedSlot != None:
                    if rowClicked != None and colClicked != None:
                        #we clicked on the board
                        if rowClicked == 2:
                            if gameField.board[rowClicked][colClicked] == None:
                                #the current space is not occupied
                                    currentPlantType = slotList[curSelectedSlot]
                                    newPlant = currentPlantType.makeNewPlant(rowClicked, colClicked)
                                    if curSun >= newPlant.cost:
                                        gameField.board[rowClicked][colClicked] = newPlant
                                        plantsList.append(newPlant)
                                        curSun -= newPlant.cost
                                        curSelectedSlot = None
                                        plantingSound.play()
                                    else: curSelectedSlot = None
                    else:
                        curSelectedSlot = None

                #checks if a slot is clicked
                for s in slotList:
                    if s.rect.collidepoint(mouseX, mouseY):
                        curSelectedSlot = s.slot

                #checks if shovel is selected
                if shovelObj.rect.collidepoint(mouseX, mouseY):
                    print "Asd"
                    if not shovelObj.selected:
                        shovelObj.select()
                    else:
                        shovelObj.deselect()

################################## GAMEPLAY ####################################
        if gameField.board[2][0] != None:
            hasPlantedYet = True

        if hasPlantedYet and not hasSpokenSunflowerYet:
            round2()
            hasSpokenSunflowerYet = True

        if not hasReached100Yet and curSun >= 100:
            round3()
            slotList.append(peashooterPacket(1))
            baddieList.append(zombie(2,1))
            hasReached100Yet = True

        if not hasKilledBaddieYet and hasReached100Yet:
            if baddieList == []:
                hasKilledBaddieYet = True

        if hasKilledBaddieYet and not hasSpokenShovelYet:
            round4(curSun, plantsList, slotList)
            hasSpokenShovelYet = True

        if hasSpokenShovelYet and not hasUsedShovelYet:
            empty = True
            for col in xrange(len(gameField.board[2])):
                if gameField.board[2][col] != None:
                    empty = False
            if empty:
                round5(curSun,slotList)
                break

        if hasPlantedYet:
        #starts the main gameplay

            #checks for expired sun and removes them
            for s in sunList:
                if s.life == s.lifeSpan:
                    sunList.remove(s)
                elif s.rect.top >= s.endY:
                    s.life += 1

            #spawns the sun currency
            sunAddCounter += 1
            if sunAddCounter == sunSpawnRate:
                sunAddCounter = 0
                newSun = sun(True)
                sunList.append(newSun)

            # Checks if mouse is on top of sun. Collects sun.
            for s in sunList:
                mouseX, mouseY = pygame.mouse.get_pos()
                if s.rect.collidepoint(mouseX,mouseY):
                    sunSound.play()
                    sunList.remove(s)
                    curSun += sunValue

            # Makes the plants shoot
            for p in plantsList:
                try:
                    p.shoot(bulletList, baddieList)
                except:
                    p.update(zlist=baddieList)

            #checks for dead zombies and removes them
            for z in baddieList:
                z.checkIfHit(bulletList)
                if z.health == 0:
                    baddieList.remove(z)



################################### Movement ####################################

            # Move the zombies forward
            for z in baddieList:
                z.update()
                z.checkIfEat(plantsList, gameField.board)
                if not z.eating: 
                    z.rect.move_ip(-1.0*z.speed, 0)

            # Delete zombies that have reached the end.
            for z in baddieList:
                if z.rect.left < 252:
                    kosbieObj.update(type(z))
                    baddieList.remove(z)

            # Move the sun down
            for s in sunList:
                if s.rect.top < s.endY:
                    s.rect.move_ip(0, 1*s.speed)

            # Propels the bullets
            for b in bulletList:
                b.rect.move_ip(b.speed, 0)

            #Removes the bullets that went off map
            for b in bulletList:
                if b.rect.left > WINDOWWIDTH:
                    bulletList.remove(b)

################################### DRAWING ####################################

        # Draw the game world on the window.
        window.blit(tutorialmap, (0, 0))

        # Draw the counter background for the sun
        counterBgX = 110
        counterBgY = 25
        window.blit(sunCounterImg, (counterBgX, counterBgY))

        # Draw the actual counter 
        white = (255, 255, 255)
        counterx = 144
        countery = 30
        drawText(str(curSun), font, window, counterx, countery, white)

        #draw the arrow
        if curSelectedSlot == None and not hasPlantedYet:
            window.blit(arrowLeftImg, (100,10))
        elif not hasPlantedYet:
            window.blit(arrowDownImg, (260,80))

        # Draw Kosbie
        window.blit(kosbieObj.surface, kosbieObj.rect)

        # Draw each baddie
        for z in baddieList:
            window.blit(z.surface, z.rect)

        # Draw each bullet
        for b in bulletList:
            window.blit(b.surface, b.rect)

        # Draw each plant
        for p in plantsList:
            window.blit(p.surface, p.rect)

        # Draw each sun
        for s in sunList:
            window.blit(s.surface, s.rect)

        # Draw each slot
        for s in slotList:
            window.blit(s.surface, s.rect)

        if hasKilledBaddieYet:
            # Draw the shovel
            window.blit(shovelObj.surface, shovelObj.rect)


        # Draw selected slot
        if curSelectedSlot != None:

            x = 20
            slotH = 57
            offset = 21
            y = (curSelectedSlot * slotH) + offset
            window.blit(selectedSlotImg, (x, y))

        pygame.display.update()


    break