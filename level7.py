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
    save.save(user, '1')

    #sets up window
    WINDOWWIDTH = 1120
    WINDOWHEIGHT = 600
    window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Pants vs. Kosbie')

    #sets up images
    #used some graphics from the orginal game

    background1 = pygame.image.load('Graphics/Frontyard.jpg')
    kosbieCutsceneImg = pygame.image.load('Graphics/kosbie cutscene.png')
    speechBoxImg = pygame.image.load('Graphics/speechbox.png')
    cooldownImg = pygame.image.load('Graphics/cooldown.png')
    nextDayImg = pygame.image.load('Graphics/nextday.png')
    endtxtImg = pygame.image.load('Graphics/endtext.png')

    #sets up sounds
    #sound from freesound.org
    victorySound = pygame.mixer.Sound('Sounds/victory.ogg')

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
        pygame.mixer.music.load('Sounds/victory.ogg')
        curSpeech = 0
        pygame.mixer.music.play(-1, 0.0)
        while True:
            speech = 'Graphics/14speech' + str(curSpeech) + '.png'
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

    while True:

        timer = 0
        nextdayX = 330
        nextdayY = 200

        while True:
            window.fill((0,0,0))
            window.blit(endtxtImg, (nextdayX, nextdayY))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONUP:
                    import RunMe

            pygame.display.update()

        break

def main():
  play('ken')

if __name__ == '__main__': main()