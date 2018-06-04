import pygame
from pygame.locals import *



matchImg = pygame.image.load('matchstick.jpg')
state = "player1"
active_row = None
game_over = True

class Button:

    x = 0
    y = 0
    image=0
    text = ""
    def __int__(self):
        pass
        #self.img= pygame.draw.rect(DISPLAY, blue, (200, 150, 100, 50))

    def draw(self,x,y,text,gameDisplay):
        self.x=x
        self.y=y
        self.text = text

        self.img = pygame.draw.rect(gameDisplay, (0,0,200), (self.x, self.y, 200, 50))
        a_sys_font = pygame.font.SysFont("Arial", 40)

        # AA, no transparancy, bold
        a_sys_font.set_bold(1)

        ren = a_sys_font.render(text, 1, (255,255,255))
        gameDisplay.blit(ren, (x+3 , y+3))
        a_sys_font.set_bold(0)
       # gameDisplay.blit(pygame.transform.scale(self.img, (10, 100)), (self.x, self.y))

    def check_mouse(self,pos,click):
        mx=pos[0]
        my=pos[1]

        if self.x < mx and self.x+200 > mx and self.y < my and self.y + 50 > my and click:
            print("click")
            global state
            global active_row
            if state == "player1":
                state = "player2"
                active_row = None
            elif state == "player2" or game_over==True:
                state = "player1"
                active_row = None


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

    def check_mouse(self,pos,click,row):
        mx=pos[0]
        my=pos[1]
        #print(pos)
        global active_row
        if self.x < mx and self.x+10 > mx and self.y < my and self.y + 100 > my and click:
            print("click")
            if active_row == None:
                self.alive = False
                active_row = row
            elif active_row == row:
                self.alive = False






# def match_draw(x,y,count=5):
#     for i in range(count):
#         gameDisplay.blit(pygame.transform.scale(matchImg,(10,100)),(x+i*20,y))

def main(winstyle=0):
    pygame.init()
    display_width = 800
    display_height = 600
    game_over = False
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)

    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('matchstick')
    clock = pygame.time.Clock()
    matches1 = [Match() for i in range(6)]
    matches2 = [Match() for i in range(6)]
    matches3 = [Match() for i in range(6)]
    button= Button()


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
        if state == "player1":
            button.draw(400,200, "Player1", gameDisplay)
        elif state == "player2":
            button.draw(400, 200, "Player2", gameDisplay)

        button.check_mouse(pos,click)

        for (i,v) in enumerate(matches1):
            if active_row == None or active_row == "row1":
                v.check_mouse(pos,click, "row1")
            v.draw(i*15,10, gameDisplay)
            if v.alive is True:
                game_over = False


        for (i,v) in enumerate(matches2):
            if active_row == None or active_row == "row2":
                v.check_mouse(pos,click,"row2")
            v.draw(i * 15, 120,gameDisplay)
            if v.alive is True:
                game_over = False


        for (i,v) in enumerate(matches3):
            if active_row == None or active_row == "row3":
                v.check_mouse(pos,click,"row3")
            v.draw(i * 15, 240,gameDisplay)
            if v.alive is True:
                game_over = False

        if game_over == True:
            button.draw(400, 200, "Play Again", gameDisplay)

        pygame.display.update()


main()
pygame.quit()
quit()