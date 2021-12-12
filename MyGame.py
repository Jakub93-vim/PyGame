import pygame

pygame.init()

win = pygame.display.set_mode((500,480))
pygame.display.set_caption("MyGame")
bg = pygame.image.load('bg.jpg')
turnLeft = [pygame.image.load('L1.png')]

class player(object):

    def __init__(self,x,y,width,height):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 3

    def draw(self, win):

        win.blit(turnLeft[0],(self.x, self.y))


jack = player(200,150,60,80)
run = True

def drawOnScreen():

    win.blit(bg,(0,0))
    jack.draw(win)
    pygame.display.update()
    

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.time.delay(100)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        jack.y -= jack.vel

    if keys[pygame.K_LEFT]:
        jack.x -= jack.vel

    if keys[pygame.K_RIGHT]:
        jack.x += jack.vel

    drawOnScreen()

pygame.quit()