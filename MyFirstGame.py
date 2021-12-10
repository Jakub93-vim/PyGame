import pygame

pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("First game")
score = 0

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
        self.standing = True
        self.hitbox = (self.x + 20, self.y + 20, 30 ,60)

    def draw (self,win):

        if self.walkCount >= 9:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walkCount], (self.x, self.y))
                self.walkCount += 1

            elif self.right:
                win.blit(walkRight[self.walkCount], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 30, 60)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

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

class enemy(object):

    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'),
                 pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'),
                 pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'),
                 pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'),
                pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'),
                pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'),
                pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 18, self.y + 1, 30, 60)

    def draw(self, win):
        self.move()
        if self.walkCount >= 11:
            self.walkCount = 0
        
        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount], (self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount], (self.x,self.y))
            self.walkCount += 1

        self.hitbox = (self.x + 18, self.y + 1, 30, 60)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1]:
                self.x += self.vel
            else:
                self.vel = -3

        if self.vel < 0:
            if 50 < self.x :
                self.x += self.vel
            else:
                self.vel = +3

    def hit(self):
        print ("hit")

jack = player(300,410,64,64)
bullets = []
goblin = enemy(60,410,64,64,200)


def redrawGameWindow():

    win.blit(bg, (0,0))
    jack.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    font = pygame.font.SysFont("comicsans", 30, True)
    text = font.render('Score: ' + str(score), 1, (0,0,0,))
    win.blit((text), (350,10))
    pygame.display.update()

while jack.run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jack.run = False

    for bullet in bullets:

        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if jack.left:

            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(projectile(jack.x+jack.width/2,jack.y+jack.height/2,6,(0,0,0),facing))

    if keys[pygame.K_LEFT] and jack.x > jack.vel:
        jack.x -= jack.vel
        jack.left = True
        jack.right = False
        jack.standing = False

    elif keys[pygame.K_RIGHT] and jack.x < 500 - jack.width - jack.vel :
        jack.x += jack.vel
        jack.right = True
        jack.left = False
        jack.standing = False
    else:
        jack.standing = True
        jack.walkCount = 0

    if not(jack.isJump):

        if keys[pygame.K_UP]:
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