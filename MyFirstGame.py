import pygame

pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("First game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

class player(object):

    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.run = True

    def draw (self,win):

        if self.walkCount >= 9:
            self.walkCount = 0

        if self.left == True:
            win.blit(walkLeft[self.walkCount], (self.x, self.y))
            self.walkCount += 1

        elif self.right == True:
            win.blit(walkRight[self.walkCount], (self.x, self.y))
            self.walkCount += 1

        else:
            win.blit(char, (self.x, self.y))
            self.walkCount = 0

class projectile(object):

    def __init__(self, x, y, radius, color, facing):

        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):

        pygame.draw.circle(win, self.color, (self.x,self.y),  self.radius)





jack = player(300,410,64,64)

def redrawGameWindow():

    win.blit(bg, (0,0))
    jack.draw(win)
    pygame.display.update()

while jack.run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jack.run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and jack.x > jack.vel:
            jack.x -= jack.vel
            jack.left = True
            jack.right = False

    elif keys[pygame.K_RIGHT] and jack.x < 500 - jack.width - jack.vel :
            jack.x += jack.vel
            jack.right = True
            jack.left = False
    else:
        jack.left = False
        jack.right = False
        jack.walkCount = 0

    if not(jack.isJump):

        if keys[pygame.K_SPACE]:
            jack.isJump = True
            jack.right = False
            jack.left = False
            jack.walkCount = 0

    else:
        if jack.jumpCount >= -10:
            jack.y-= jack.jumpCount * abs(jack.jumpCount) * 0.5
            jack.jumpCount -= 1
        else:
            jack.jumpCount = 10
            jack.isJump = False

    redrawGameWindow()

pygame.quit()