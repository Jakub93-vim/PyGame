import pygame

pygame.init()

win = pygame.display.set_mode((500,480))
pygame.display.set_caption("MyGame")
bg = pygame.image.load('bg.jpg')
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png')]
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png')]


class player(object):

    def __init__(self,x,y,width,height):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 3
        self.walkCount = 0
        self.jumpNum = 8
        self.isJump = False
        self.Left = False
        self.Right = False

    def draw(self, win):

        if jack.walkCount > 1:
            jack.walkCount = 0

        if jack.Left:
            win.blit(walkLeft[jack.walkCount],(jack.x, jack.y))
        else:
             win.blit(walkRight[jack.walkCount],(jack.x, jack.y))

class projectile (object):

    def __init__(self,x,y):

        self.x = x
        self.y = y
        self.radius = 5
        self.velocity = 3
        self.isShooting = False
        
    def draw(self,win):
        
        pygame.draw.circle(win, (255,0,0), (bullet.x+(jack.width/2),bullet.y + (jack.height/2)), self.radius)


jack = player(200,400,60,80)
run = True
bullet = projectile(jack.x,jack.y)

def drawOnScreen():

    win.blit(bg,(0,0))
    jack.draw(win)
    bullet.draw(win)
    pygame.display.update()

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.time.delay(100)
    keys = pygame.key.get_pressed()

    if not bullet.isShooting:
        if keys[pygame.K_SPACE]:
            bullet.isShooting = True

    else:
        if jack.Right:
            bullet.x += bullet.velocity
        if jack.Left:
            bullet.x -= bullet.velocity

    if keys[pygame.K_LEFT] and jack.x > jack.vel:
        jack.x -= jack.vel
        jack.walkCount += 1
        jack.Left = True
        jack.Right = False

    if keys[pygame.K_RIGHT] and jack.x < (450 - jack.vel):
        jack.x += jack.vel
        jack.walkCount += 1
        jack.Right = True
        jack.Left = False

    if not jack.isJump:
        if keys[pygame.K_UP]:
            jack.isJump = True
    else:
        jack.y -= jack.jumpNum * abs(jack.jumpNum) * 0.5
        jack.jumpNum -= 1
        if jack.jumpNum < -8:
            jack.isJump = False
            jack.jumpNum = 8


    drawOnScreen()

pygame.quit()