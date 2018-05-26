import pygame
from pygame.locals import *



matchImg = pygame.image.load('matchstick.jpg')

class Match:
    x = 0
    y = 0
    alive = True
    img = pygame.image.load('matchstick.jpg')
    def __int__(self):
        self.img = pygame.image.load('matchstick.jpg')
        self.alive = True

    def draw(self,x,y,gameDisplay):
        self.x=x
        self.y=y

        if self.alive:
            gameDisplay.blit(pygame.transform.scale(self.img, (10, 100)), (self.x, self.y))

    def check_mouse(self,pos,click):
        mx=pos[0]
        my=pos[1]
        print(pos)
        if self.x < mx and self.x+10 > mx and self.y < my and self.y + 100 > my and click:
            print("click")
            self.alive = False



# def match_draw(x,y,count=5):
#     for i in range(count):
#         gameDisplay.blit(pygame.transform.scale(matchImg,(10,100)),(x+i*20,y))

def main(winstyle=0):
    pygame.init()
    display_width = 800
    display_height = 600

    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('matchstick')
    clock = pygame.time.Clock()
    matches1 = [Match() for i in range(10)]
    matches2 = [Match() for i in range(10)]
    matches3 = [Match() for i in range(10)]


    while True:
        click = False
        pos = (0, 0)
        for event in pygame.event.get():
            if event.type == QUIT or \
                (event.type == KEYDOWN and event.key == K_ESCAPE):
                    return
            if event.type == pygame.MOUSEBUTTONUP:
                #pos = pygame.mouse.get_pos()
                click = True

        pos = pygame.mouse.get_pos()
        keystate = pygame.key.get_pressed()

        # match_draw(display_width / 2 - 200, display_height / 2 - 200, 20)
        # match_draw(display_width/2 -200 ,display_height/2,20)
        # match_draw(display_width / 2 - 200, display_height / 2 + 150, 20)
        #match1.draw(10,10)
        gameDisplay.fill((0,0,0))

        for (i,v) in enumerate(matches1):
            v.check_mouse(pos,click)
            v.draw(i*15,10, gameDisplay)


        for (i,v) in enumerate(matches2):
            v.check_mouse(pos,click)
            v.draw(i * 15, 120,gameDisplay)

        for (i,v) in enumerate(matches3):
            v.check_mouse(pos,click)
            v.draw(i * 15, 240,gameDisplay)

        pygame.display.update()


main()
pygame.quit()
quit()