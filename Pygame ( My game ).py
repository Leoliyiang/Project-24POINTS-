import pygame
from pygame.locals import *
display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('matchstick')
clock = pygame.time.Clock()

matchImg = pygame.image.load('matchstick.jpg')

def match_draw(x,y,count=5):
    for i in range(count):
        gameDisplay.blit(pygame.transform.scale(matchImg,(10,100)),(x+i*20,y))

def main(winstyle=0):
    pygame.init()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or \
                (event.type == KEYDOWN and event.key == K_ESCAPE):
                    return
        keystate = pygame.key.get_pressed()

        match_draw(display_width / 2 - 300, display_height / 2 - 300, 20)
        match_draw(display_width/2,display_height/2,20)
        match_draw(display_width / 2 + 200, display_height / 2 + 200, 20)
        pygame.display.update()





main()
pygame.quit()
quit()