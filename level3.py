import pygame, random, sys, time
from pygame.locals import *
import save

#used http://www.pygame.org/project-Plants+vs+Zombies-2632-.html
#as base

def play(user):
    #sets up pygame
    pygame.init()
    fpsClock = pygame.time.Clock()

    font = pygame.font.SysFont(None, 30)

    #saves progress
    save.save(user, '3')

    #sets up window
    WINDOWWIDTH = 1120
    WINDOWHEIGHT = 600
    window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Pants vs. Kosbie')

    #sets up images
    #used some graphics from the orginal game

    emptySeedImg = pygame.image.load('Graphics/empty_seed.png')
    background1 = pygame.image.load('Graphics/Frontyard.jpg')
    khakiImage = pygame.image.load('Graphics/pants.png')
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
    frozenkhakiImg = pygame.image.load('Graphics/frozen pants.png')
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
    pausedBgImg = pygame.image.load('Graphics/paused bg.png')
    pausedSignImg = pygame.image.load('Graphics/paused.png')
    quitSignImg = pygame.image.load('Graphics/quit.png')
    quitSignHoverImg = pygame.image.load('Graphics/quit hover.png')
    quitSignClickedImg = pygame.image.load('Graphics/quit clicked.png')
    pauseButtonImg = pygame.image.load('Graphics/pausebutton.png')
    pauseButtonClickedImg =pygame.image.load('Graphics/pausebutton clicked.png')
    cooldownImg = pygame.image.load('Graphics/cooldown.png')
    nextDayImg = pygame.image.load('Graphics/nextday.png')

    #sets up sounds
    #sounds from freesound.org
    #and the offical game

    hitSound = pygame.mixer.Sound('Sounds/splat.ogg')
    plantingSound = pygame.mixer.Sound('Sounds/planting.wav')
    sunSound = pygame.mixer.Sound('Sounds/sun.ogg')
    owSound = pygame.mixer.Sound('Sounds/ow.ogg')
    explosionSound = pygame.mixer.Sound('Sounds/explosion.ogg')
    smExplosionSound = pygame.mixer.Sound('Sounds/small explosion.ogg')

    #The next day transition

    while True:

        timer = 0
        nextdayX = 330
        nextdayY = 0
        endY = 200
        while True:
            window.fill((0,0,0))
            window.blit(nextDayImg, (nextdayX, nextdayY))

            if nextdayY == endY:
                #break out of the transition when nextdayY hits endY
                time.sleep(2)
                break

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            nextdayY += 10
            pygame.display.update()

        break

    #The beginning cutscene

    while True:
        pygame.mixer.music.load('Sounds/intmusic.ogg')
        curSpeech = 0
        pygame.mixer.music.play(-1, 0.0)
        while True:
            speech = 'Graphics/6speech' + str(curSpeech) + '.png'
            try:
                speechImg = pygame.image.load(speech)
            except:
                #when Kosbie runs out of things to say
                break
            window.blit(background1 ,(0,0))

            kosbieX = 200
            kosbieY = 22
            window.blit(kosbieCutsceneImg, (kosbieX, kosbieY))

            speechboxX = 450
            speechboxY = 115
            window.blit(speechBoxImg, (speechboxX, speechboxY))
            window.blit(speechImg, (speechboxX, speechboxY))

            if curSpeech == 2:
                imgX = 650
                imgY = 270
                window.blit(wallnutImg, (imgX,imgY))

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
            pygame.display.update()

        break

    def drawText(text, font, surface, x, y, color):
        #taken from http://www.pygame.org/project-Plants+vs+Zombies-2632-.html
        textobj = font.render(text, True, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def findRowCol(x, y):
        #returns the row and column based of the x and y of the mouse
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
        #checks if there is a baddie in the row of the plant
        for b in baddieList:
            if b.row == myRow:
                return True
        return False 

    def gameOver():
        #the cutscene if the user loses
        while True:
            curSpeech = 0
            while True:
                speech = 'Graphics/2speech' + str(curSpeech) + '.png'
                
                try:
                    speechImg = pygame.image.load(speech)
                except:
                    break

                window.blit(background1 ,(0,0))

                kosbieX = 200
                kosbieY = 22            
                window.blit(kosbieSadCutsceneImg, (kosbieX,kosbieY))

                speechboxX = 450
                speechboxY = 115
                window.blit(speechBoxImg, (speechboxX, speechboxY))
                window.blit(speechImg, (speechboxX, speechboxY))

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
                pygame.display.update()

            break

    def victory():
        # The cutscene if the user wins the level
        while True:
            curSpeech = 0
            while True:
                speech = 'Graphics/7speech' + str(curSpeech) + '.png'
                
                try:
                    speechImg = pygame.image.load(speech)
                except:
                    import level4
                    level4.play(user)

                window.blit(background1 ,(0,0))
                kosbieX = 200
                kosbieY = 22
                window.blit(kosbieCutsceneImg, (kosbieX, kosbieY))

                speechboxX = 450
                speechboxY = 115
                window.blit(speechBoxImg, (speechboxX, speechboxY))
                window.blit(speechImg, (speechboxX, speechboxY))

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
                pygame.display.update()

            break

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

        def move(self):
            #kosbie walking up and down
            if self.walkingDown:
                if self.y < self.patrolBot:
                    self.y += 1
                    self.rect = pygame.Rect(self.x,self.y,self.sizeX,self.sizeY)
                else:
                    self.walkingDown = False
            else:
                if self.y > self.patrolTop:
                    self.y -= 1
                    self.rect = pygame.Rect(self.x,self.y,self.sizeX,self.sizeY)
                else:
                    self.walkingDown = True

        def update(self, baddietype):
            #kosbie changing his model if a pant gets to him
            if baddietype == jeans:
                self.surface = kosbieJeansImg
            elif baddietype == khaki:
                self.surface = kosbieKhakisImg
            elif baddietype == shorts:
                self.surface = kosbieShortsImg

    class field(object):
        #sets up the game board
        def __init__(self):
            self.rows = 5
            self.cols = 9
            self.board = []
            for row in xrange(self.rows): self.board += [[None]*self.cols]

    class sun(object):
        def __init__(self, natural, x=None, y=None):
            if natural:
                #if generated from the sun
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
                size = 30
                self.rect = pygame.Rect(self.x, self.y, size, size)
                self.surface = pygame.transform.scale(sunImg, (size, size))
            else:
                #if generated from a sunflower
                xOffset = 14
                self.x = x + xOffset
                self.y = y
                self.endY = y + 42
                self.speed = 1
                self.life = 0
                self.lifeSpan = 200
                size = 30
                self.rect = pygame.Rect(self.x, self.y, size, size)
                self.surface = pygame.transform.scale(sunImg, (size, size))

    class peashooterPacket(object):
        #sets up the seed slot for the peashooter
        def __init__(self, slot):
            self.cost = 100
            self.slot = slot
            slotH = 57
            offset = 21
            y = slot * slotH + offset
            x = 20
            self.sizeX = 76
            self.sizeY = 47
            self.rect = pygame.Rect(x, y, self.sizeX, self.sizeY)
            self.surface = pygame.transform.scale(peashooterSeedImg, 
                                                  (self.sizeX,self.sizeY))
            self.cooldown = 90.0
            self.curCooldown = 0

        def makeNewPlant(self, row, col):
            return peashooter(row, col)

    class peashooterBullet(object):
        #sets up the bullets for the peashooter
        def __init__(self, x, y):
            self.speed = 15
            self.size = 24
            xOffset = 40
            self.x = x + xOffset
            self.y = y
            self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
            self.surface = pygame.transform.scale(peashooterBulletImg, 
                                                  (self.size,self.size))

    class peashooter(object):
        #sets up the peashooter plant
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
            self.surface = pygame.transform.scale(peashooterImg, 
                                                  (self.size, self.size))
            self.curBullet = None
            self.lastShot = time.time()

        def shoot(self, bulletList, baddieList):
            timeSinceLastShot = time.time() - self.lastShot 
            if not checkIfBaddieInRow(self.row, baddieList):
                #dont shoot if no baddies in the same row
                pass
            elif self.curBullet == None and timeSinceLastShot > 1:
                self.lastShot = time.time()
                bullet = peashooterBullet(self.x, self.y)
                bulletList.append(bullet)
                self.curBullet = bullet
            else:
                if self.curBullet not in bulletList:
                    self.curBullet = None

    class wallnutPacket(object):
        #sets up the seed slot for the wallnut
        def __init__(self, slot):
            self.cost = 50
            self.slot = slot
            slotH = 57
            offset = 21
            y = slot * slotH + offset
            x = 20
            self.sizeX = 76
            self.sizeY = 48
            self.rect = pygame.Rect(x, y, self.sizeX, self.sizeY)
            self.surface = pygame.transform.scale(wallnutSeedImg, 
                                                  (self.sizeX, self.sizeY))
            self.cooldown = 300.0
            self.curCooldown = 0

        def makeNewPlant(self, row, col):
            return wallnut(row, col)

    class wallnut(object):
        #sets up the wallnut plant
        def __init__(self, row, col):
            self.health = 300
            self.cost = 50
            self.row = row
            self.col = col
            self.fireRate = 1
            self.sizeX = 62
            self.sizeY = 71
            cellW = 82
            cellH = 98
            xOffset = 260
            yOffset = 84
            self.top = (col * cellW) + xOffset
            self.left= (row * cellH) + yOffset
            self.rect = pygame.Rect(self.top, self.left, self.sizeX, self.sizeY)
            self.surface = pygame.transform.scale(wallnutImg, 
                                                  (self.sizeX, self.sizeY))
            self.timeAlive = 0

        def update(self, zlist):
            #updates model when wallnut is damaged
            if self.health <= 100:
                self.surface = wallnutCracked2Img
            elif self.health > 100 and self.health <= 200:
                self.surface = wallnutCracked1Img

    class sunflowerPacket(object):
        #sets up the seed slot for the sunflower
        def __init__(self, slot):
            self.cost = 50
            self.slot = slot
            slotH = 57
            offset = 21
            y = slot * slotH + offset
            x = 20
            self.sizeX = 76
            self.sizeY = 48
            self.rect = pygame.Rect(x, y, self.sizeX, self.sizeY)
            self.surface = pygame.transform.scale(sunflowerSeedImg, 
                                                  (self.sizeX, self.sizeY))
            self.cooldown = 90.0
            self.curCooldown = 0

        def makeNewPlant(self, row, col):
            return sunflower(row, col)

    class sunflower(object):
        #sets up the sunflower plant
        def __init__(self, row, col):
            self.health = 75
            self.cost = 50
            self.row = row
            self.col = col
            self.fireRate = 180 #sun generating rate
            self.sizeX = 60
            self.sizeY = 63
            cellW = 79
            cellH = 98
            xOffset = 270
            yOffset = 88
            self.top = (col * cellW) + xOffset
            self.left= (row * cellH) + yOffset
            self.rect = pygame.Rect(self.top, self.left, self.sizeX, self.sizeY)
            self.surface = pygame.transform.scale(sunflowerImg, 
                                                  (self.sizeX,self.sizeY))
            self.timeAlive = 0

        def update(self, zlist):
            #generates sun
            self.timeAlive += 1
            if self.timeAlive == self.fireRate:
                self.timeAlive = 0
                newSun = sun(False, self.top, self.left)
                sunList.append(newSun)

    class repeater(object):
        #sets up the plant repeater, which is very similar to the peashooter
        def __init__(self, row, col):
            self.health = 75
            self.cost = 200
            self.row = row
            self.col = col
            self.sizeX = 63
            self.sizeY = 60
            cellW = 80
            cellH = 98
            xOffset = 260
            yOffset = 90
            self.x = (col * cellW) + xOffset
            self.y= (row* cellH) + yOffset
            self.rect = pygame.Rect(self.x, self.y, self.sizeX, self.sizeY)
            self.surface = pygame.transform.scale(repeaterImg, 
                                                  (self.sizeX,self.sizeY))
            self.curBullet = None
            self.lastShot = time.time()

        def shoot(self, bulletList, baddieList):
            #shoots two bullets instead of one
            timeSinceLastShot = time.time() - self.lastShot 
            if not checkIfBaddieInRow(self.row, baddieList):
                pass
            elif self.curBullet == None and timeSinceLastShot > 1:
                self.lastShot = time.time()
                gapInBetweenBullets = 21
                bullet1 = peashooterBullet(self.x + gapInBetweenBullets, self.y)
                bulletList.append(bullet1)
                bullet2 = peashooterBullet(self.x, self.y)
                bulletList.append(bullet2)
                self.curBullet = bullet2
            else:
                if self.curBullet not in bulletList:
                    self.curBullet = None

    class repeaterPacket(object):
        #sets up the seed slot for the repeater
        def __init__(self, slot):
            self.cost = 200
            self.slot = slot
            slotH = 57
            offset = 21
            y = slot * slotH + offset
            x = 20
            self.sizeX = 76
            self.sizeY = 46
            self.rect = pygame.Rect(x, y, self.sizeX, self.sizeY)
            self.surface = pygame.transform.scale(repeaterSeedImg, 
                                                  (self.sizeX,self.sizeY))
            self.cooldown = 105.0
            self.curCooldown = 0

        def makeNewPlant(self, row, col):
            return repeater(row, col)

    class snowpea(object):
        #sets up the plant snowpea
        def __init__(self, row, col):
            self.health = 75
            self.cost = 175
            self.row = row
            self.col = col
            self.sizeX = 57
            self.sizeY = 62
            cellW = 80
            cellH = 98
            xOffset = 260
            yOffset = 90
            self.x = (col * cellW) + xOffset
            self.y = (row* cellH) + yOffset
            self.rect = pygame.Rect(self.x, self.y, self.sizeX, self.sizeY)
            self.surface = pygame.transform.scale(snowpeaImg, 
                                                  (self.sizeX,self.sizeY))
            self.curBullet = None
            self.lastShot = time.time()

        def shoot(self, bulletList, baddieList):
            timeSinceLastShot = time.time() - self.lastShot 
            if not checkIfBaddieInRow(self.row, baddieList):
                pass
            elif self.curBullet == None and timeSinceLastShot > 1:
                self.lastShot = time.time()
                bullet = snowpeaBullet(self.x, self.y)
                bulletList.append(bullet)
                self.curBullet = bullet
            else:
                if self.curBullet not in bulletList:
                    self.curBullet = None

    class snowpeaPacket(object):
        #sets up the seed slot for the snowpea
        def __init__(self, slot):
            self.cost = 175
            self.slot = slot
            slotH = 57
            offset = 21
            y = slot * slotH + offset
            x = 20
            self.sizeX = 76
            self.sizeY = 46
            self.rect = pygame.Rect(x, y, self.sizeX, self.sizeY)
            self.surface = pygame.transform.scale(snowpeaSeedImg, 
                                                  (self.sizeX,self.sizeY))
            self.cooldown = 105.0
            self.curCooldown = 0

        def makeNewPlant(self, row, col):
            return snowpea(row, col)

    class snowpeaBullet(object):
        #sets up the bullet for the snowpea
        def __init__(self, x, y):
            self.speed = 15
            self.size = 26
            xOffset = 40
            self.x = x + xOffset
            self.y = y
            self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
            self.surface = pygame.transform.scale(snowpeaBulletImg, 
                                                  (self.size,self.size))

    class cherrybomb(object):
        #sets up the plant cherry bomb
        def __init__(self, row, col):
            self.health = 130
            self.cost = 150
            self.row = row
            self.col = col
            self.fireRate = 30
            self.warningTime = 15
            self.deathTime = 32

            self.sizeX = 102
            self.sizeY = 89

            self.cellW = 80
            self.cellH = 98
            xOffset = 244
            yOffset = 70
            self.x = (col * self.cellW) + xOffset
            self.y = (row* self.cellH) + yOffset

            self.rect = pygame.Rect(self.x, self.y, self.sizeX, self.sizeY)
            self.surface = pygame.transform.scale(cherryBombImg, 
                                                  (self.sizeX,self.sizeY))
            self.timeAlive = 0


        def update(self, zlist):
            #updates the model when the cherry bomb explodes
            self.timeAlive += 1
            if self.timeAlive > self.fireRate:
                xOffset = 250
                yOffset = 75
                self.x = (self.col - 1) * self.cellW + xOffset
                self.y = (self.row - 1) * self.cellH + yOffset
                sizeX = 238
                sizeY = 301
                self.rect = pygame.Rect(self.x, self.y, sizeX, sizeY)
                self.surface = pygame.transform.scale(cherryBombExpImg, 
                                                      (sizeX,sizeY))
                explosionSound.play()
                for z in zlist:
                    if z.rect.colliderect(self.rect):
                        zlist.remove(z)
            elif self.timeAlive == self.warningTime:
                self.surface = pygame.transform.scale(cherryBomb2Img, 
                                                      (self.sizeX, self.sizeY))

    class cherrybombPacket(object):
        #sets up the seed slot for the chery bomb
        def __init__(self, slot):
            self.cost = 150
            self.slot = slot
            slotH = 57
            offset = 21
            y = slot * slotH + offset
            x = 20
            self.sizeX = 76
            self.sizeY = 48
            self.rect = pygame.Rect(x, y, self.sizeX, self.sizeY)
            self.surface = pygame.transform.scale(cherryBombSeedImg, 
                                                  (self.sizeX,self.sizeY))
            self.cooldown = 450.0
            self.curCooldown = 0

        def makeNewPlant(self, row, col):
            return cherrybomb(row, col)

    class potatomine(object):
        #sets up the plant potato mine
        def __init__(self, row, col):
            self.health = 100
            self.cost = 25
            self.row = row
            self.col = col
            self.fireRate = 50
            self.sizeX = 73
            self.sizeY = 52

            cellW = 82
            cellH = 98
            xOffset = 252
            yOffset = 98
            self.x = (col * cellW) + xOffset
            self.y = (row * cellH) + yOffset

            self.rect = pygame.Rect(self.x, self.y, self.sizeX, self.sizeY)
            self.surface = pygame.transform.scale(pmineImg, 
                                                  (self.sizeX,self.sizeY))
            self.timeAlive = 0
            self.deathTime = None
            self.splattered = False

        def update(self, zlist):
            #updates the model for potato mine when it explodes
            self.timeAlive += 1
            if self.splattered:
                self.surface = pmineExpImg
                self.deathTime = 5
            elif self.timeAlive == self.fireRate:
                self.surface = pygame.transform.scale(pmine2Img, 
                                                      (self.sizeX,self.sizeY))
            elif self.timeAlive > self.fireRate:
                for z in zlist:
                    if z.rect.colliderect(self.rect):
                        smExplosionSound.play()
                        zlist.remove(z)
                        self.splattered = True
                        self.timeAlive = 0

    class potatominePacket(object):
        #sets up the seed slot for the potato mine
        def __init__(self, slot):
            self.cost = 25
            self.slot = slot
            slotH = 57
            offset = 21
            y = slot * slotH + offset
            x = 20
            self.sizeX = 76
            self.sizeY = 47
            self.rect = pygame.Rect(x, y, self.sizeX, self.sizeY)
            self.surface = pygame.transform.scale(pmineSeedImg, 
                                                  (self.sizeX,self.sizeY))
            self.cooldown = 300.0
            self.curCooldown = 0

        def makeNewPlant(self, row, col):
            return potatomine(row, col)

    class khaki(object):
        #sets up the baddie Khaki Pants
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
            self.surface = pygame.transform.scale(khakiImage, 
                                                  (self.sizeX,self.sizeY))
            self.eating = False
            self.frozen = False
            self.frozenSpeed = 1
            self.thawTimer = 0
            self.thawTime = 60

        def checkIfHit(self, bulletList):
            #checks if it is hit by a bullet
            for b in bulletList:
                if b.rect.colliderect(self.rect):
                    if type(b) == snowpeaBullet:
                        self.frozen = True
                        self.thawTimer = 0
                    hitSound.play()
                    bulletList.remove(b)
                    self.health -= 1

        def checkIfEat(self,plantsList, board):
            #checks if it should be eating a plant
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
            #updates the model if frozen
            if self.frozen:
                self.speed = self.frozenSpeed
                self.thawTimer += 1
                self.surface = pygame.transform.scale(frozenkhakiImg, 
                                                      (self.sizeX,self.sizeY))
                if self.thawTimer == self.thawTime:
                    self.thawTime = 0
                    self.frozen = False
                    self.speed = self.normalSpeed
                    self.surface = pygame.transform.scale(khakiImage, 
                                                        (self.sizeX,self.sizeY))

    class jeans(object):
        #sets up the baddie Jeans Pants
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
            self.surface = pygame.transform.scale(jeansImg, 
                                                  (self.sizeX,self.sizeY))
            self.eating = False
            self.frozen = False
            self.thawTimer = 0
            self.thawTime = 60

        def checkIfHit(self, bulletList):
            #checks if it is hit by a bullet
            for b in bulletList:
                if b.rect.colliderect(self.rect):
                    if type(b) == snowpeaBullet:
                        self.thawTimer = 0
                        self.frozen = True
                    hitSound.play()
                    bulletList.remove(b)
                    self.health -= 1

        def checkIfEat(self,plantsList, board):
            #checks if it should be eating a plant
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
            #updates the model if it is frozen
            if self.frozen:
                self.speed = self.frozenSpeed
                self.thawTimer += 1
                self.surface = pygame.transform.scale(frozenJeansImg, 
                                                      (self.sizeX,self.sizeY))
                if self.thawTimer == self.thawTime:
                    self.thawTimer = 0
                    self.frozen = False
                    self.speed = self.normalSpeed
                    self.surface = pygame.transform.scale(jeansImg, 
                                                        (self.sizeX,self.sizeY))

    class shorts(object):
        #sets up the baddie Short Pants
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
            self.surface = pygame.transform.scale(shortsImg, 
                                                  (self.sizeX,self.sizeY))
            self.eating = False
            self.frozen = False
            self.thawTimer = 0
            self.thawTime = 60

        def checkIfHit(self, bulletList):
            #checks if it is hit by a bullet
            for b in bulletList:
                if b.rect.colliderect(self.rect):
                    if type(b) == snowpeaBullet:
                        self.thawTimer = 0
                        self.frozen = True
                    hitSound.play()
                    bulletList.remove(b)
                    self.health -= 1

        def checkIfEat(self,plantsList, board):
            #checks if it should be eating a plant
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
            #updates the model if it is frozen
            if self.frozen:
                self.speed = self.frozenSpeed
                self.thawTimer += 1
                self.surface = pygame.transform.scale(frozenShortsImg, 
                                                      (self.sizeX,self.sizeY))
                if self.thawTimer == self.thawTime:
                    self.thawTimer = 0
                    self.frozen = False
                    self.speed = self.normalSpeed
                    self.surface = pygame.transform.scale(shortsImg, 
                                                        (self.sizeX,self.sizeY))

    class quitSign(object):
        def __init__(self):
            y = 264
            x = 414
            sizeX = 291
            sizeY = 54

            self.rect = pygame.Rect(x, y, sizeX, sizeY)
            self.surface = quitSignImg

        def hover(self):
            self.surface = quitSignHoverImg

        def clicked(self):
            self.surface = quitSignClickedImg

        def reset(self):
            self.surface = quitSignImg

    class pauseButton(object):
        def __init__(self):
            y = 20
            x = 1070
            sizeX = 30
            sizeY = 30

            self.rect = pygame.Rect(x, y, sizeX, sizeY)
            self.surface = pauseButtonImg

        def clicked(self):
            self.surface = pauseButtonClickedImg

        def reset(self):
            self.surface = pauseButtonImg

    spawnList = [
                 khaki(0, 400), 
                 khaki(1, 800), 
                 khaki(4, 1100), 
                 jeans(3, 1200),
                 khaki(2, 1350), 

                 jeans(2, 1400),
                 khaki(4, 1800),
                 khaki(1, 1950), 
                 jeans(0, 1980),
                 khaki(1, 2050),
                 khaki(4, 2130),
                 khaki(2, 2180), 
                 jeans(3, 2300), 

                 jeans(0, 2850), 
                 jeans(1, 2551), 
                 jeans(2, 2630),
                 jeans(3, 2550),
                 jeans(4, 2850), 

                 jeans(4, 2900),
                 jeans(2, 2932),
                 jeans(1, 2963),
                 jeans(0, 2940),
                 jeans(3, 2905),
                 jeans(0, 2970),
                 jeans(1, 2980),
                 jeans(2, 3010),
                 jeans(3, 3000),
                 jeans(4, 3010),
                 jeans(0, 3050),
                 jeans(1, 3030),
                 jeans(2, 3040),
                 jeans(3, 3020),
                 jeans(4, 3000),
                 ]


    while True:
        sunSpawnRate = 150
        baddieList = []
        plantsList = []
        bulletList = []
        sunList = []
        slotList = []
        slotList.append(sunflowerPacket(0))
        slotList.append(peashooterPacket(1))
        slotList.append(repeaterPacket(2))
        slotList.append(wallnutPacket(3))

        signsList = []
        signsList.append(quitSign())

        curSelectedSlot = None
        curSun = 50
        sunValue = 25
        khakiAddCounter = 0
        sunAddCounter = 0
        gameTime = 0
        lives = 2
        isGameOver = False
        gamePaused = False

        gField = field()    
        kosbieObj = kosbie()
        shovelObj = shovel()
        pauseObj = pauseButton()
        pygame.mixer.music.load('Sounds/grasswalk.ogg')
        pygame.mixer.music.play(-1, 0.0)

        while True:
            #main game loop

            if gamePaused:

                mouseX, mouseY = pygame.mouse.get_pos()

                #changes model of sign if hovered
                for s in signsList:
                    if s.rect.collidepoint(mouseX,mouseY):
                        s.hover()
                    else:
                        s.reset()

                #checks for user events
                for event in pygame.event.get():

                    #checks for exit
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYUP:
                        if event.key == K_ESCAPE:
                            pygame.quit()
                            sys.exit()

                    #checks for unpause
                    if event.type == KEYUP:
                        if event.key == K_p:
                            gamePaused = False

                    if event.type == MOUSEBUTTONUP:
                        #checks if Quit sign is clicked
                        for s in signsList:
                            if s.rect.collidepoint(mouseX,mouseY):
                                s.clicked()
                                import RunMe

                        #checks if pause button is clicked
                        if pauseObj.rect.collidepoint(mouseX, mouseY):
                                pauseObj.reset()
                                gamePaused = False

            if not gamePaused:

                gameTime += 1       #used for spawning

                kosbieObj.move()    #makes kosbie patrol

                #checks for user events
                for event in pygame.event.get():

                    #checks for exit
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYUP:
                        if event.key == K_ESCAPE:
                            pygame.quit()
                            sys.exit()

                        #checks for pause
                        if event.key == K_p:
                            gamePaused = True

                    if event.type == MOUSEBUTTONUP:
                        mouseX, mouseY = pygame.mouse.get_pos()
                        mRow, mCol = findRowCol(mouseX,mouseY)

                        # Shovel selected, remove a plant using the shovel
                        if shovelObj.selected:
                            if mRow != None and mCol != None:
                                if gField.board[mRow][mCol] == None:
                                    shovelObj.deselect()
                                else:
                                    plantsList.remove(gField.board[mRow][mCol])
                                    gField.board[mRow][mCol] = None
                                    shovelObj.deselect()

                            elif shovelObj.rect.collidepoint(mouseX, mouseY):
                                #can ignore this case. We deselect later to
                                #avoid conflictions between the two deselects.
                                pass

                            else:
                                shovelObj.deselect()

                        # We have a selected seed, plant it
                        elif curSelectedSlot != None:
                            if mRow != None and mCol != None:
                                #we clicked on the board
                                if gField.board[mRow][mCol] == None:
                                    #the current space is not occupied
                                        curP = slotList[curSelectedSlot]
                                        newPlant = curP.makeNewPlant(mRow, mCol)
                                        if curSun >= newPlant.cost:
                                            curP.curCooldown = curP.cooldown
                                            gField.board[mRow][mCol] = newPlant
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
                                if s.curCooldown == 0:
                                    curSelectedSlot = s.slot

                        #checks if shovel is selected
                        if shovelObj.rect.collidepoint(mouseX, mouseY):
                            if not shovelObj.selected:
                                shovelObj.select()
                            else:
                                shovelObj.deselect()

                        #checks if pause button is clicked
                        if pauseObj.rect.collidepoint(mouseX, mouseY):
                                pauseObj.clicked()
                                gamePaused = True

        ################################## Gameplay ############################
                
                # if the game is over, break out of everything
                if isGameOver:
                    break

                # if the player has defeated all the baddies, we win
                if spawnList == [] and baddieList == []:
                    victory()

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

                # Removes plants that are temporary(like cherry bombs)
                for p in plantsList:
                    try:
                        if p.deathTime != None:
                            if p.timeAlive > p.deathTime:
                                gField.board[p.row][p.col] = None
                                plantsList.remove(p)
                    except:
                        pass

                #spawns the pants
                for s in spawnList:
                    if s.spawnTime <= gameTime:
                        baddieList.append(s)
                        spawnList.remove(s)

                #spawns the sun currency
                sunAddCounter += 1
                if sunAddCounter == sunSpawnRate:
                    sunAddCounter = 0
                    newSun = sun(True)
                    sunList.append(newSun)

                #checks for dead pants and removes them
                for z in baddieList:
                    z.checkIfHit(bulletList)
                    if z.health <= 0:
                        baddieList.remove(z)

                #checks for expired sun and removes them
                for s in sunList:
                    if s.life == s.lifeSpan:
                        sunList.remove(s)
                    elif s.rect.top >= s.endY:
                        s.life += 1

                for s in slotList:
                    if s.curCooldown > 0:
                        s.curCooldown -= 1

        ################################### Movement ###########################

                # Move the pants forward
                for z in baddieList:
                    z.update()
                    z.checkIfEat(plantsList, gField.board)
                    if not z.eating: 
                        z.rect.move_ip(-1.0*z.speed, 0)

                # Delete pants that have reached the end.
                for z in baddieList:
                    if z.rect.left < 252:
                        kosbieObj.update(type(z))
                        baddieList.remove(z)
                        lives -= 1
                        if lives == 0:
                            isGameOver = True
                            gameOver()

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

    ################################### DRAWING ################################

            # Draw the game world on the window.
            window.blit(background1, (0, 0))

            # Draw the shovel
            window.blit(shovelObj.surface, shovelObj.rect)

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

                cdSizeY = int(round((s.curCooldown/s.cooldown) * s.sizeY))
                cooldownChangingImg = pygame.transform.scale(cooldownImg, 
                                                             (s.sizeX, cdSizeY))
                window.blit(cooldownChangingImg, s.rect)

            # Draw selected slot
            if curSelectedSlot != None:

                x = 20
                slotH = 57
                offset = 21
                y = (curSelectedSlot * slotH) + offset
                window.blit(selectedSlotImg, (x, y))

            if gamePaused:
                window.blit(pausedBgImg, (0,0))

                #draw the paused sign
                signX = 414
                signY = 200
                window.blit(pausedSignImg, (signX, signY))

                #draw the other  signs
                for s in signsList:
                    window.blit(s.surface, s.rect)

            # Draw the pause button
            window.blit(pauseObj.surface, pauseObj.rect)

            pygame.display.update()

        break

    import RunMe

def main():
  play('ken')

if __name__ == '__main__': main()