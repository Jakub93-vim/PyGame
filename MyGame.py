import pygame

pygame.init()

win = pygame.display.set_mode((500,480))
pygame.display.set_caption("MyGame")
#background
bg = pygame.image.load('bg.jpg')
#pictures of the player
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png')]
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png')]
enemyLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png')]
enemyRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png')]


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
        self.hitbox = (self.x + 20, self.y + 7, 27, 52)
        self.rect = pygame.Rect(self.x + 20, self.y - 15, 27, 60)

    def draw(self, win):

        if jack.walkCount > 1:
            jack.walkCount = 0
        #draws player according to its orientation
        if jack.Left:
            win.blit(walkLeft[jack.walkCount],(jack.x, jack.y))
        else:
             win.blit(walkRight[jack.walkCount],(jack.x, jack.y))

        self.rect = pygame.Rect(self.x + 20, self.y + 7, 27, 60)
        self.hitbox = (self.x + 20, self.y + 7, 27, 52)
        pygame.draw.rect(win, (200, 50, 80), self.rect) # rectangle of the player

class projectile (object):

    def __init__(self,x,y):

        self.x = x
        self.y = y
        self.radius = 5
        self.velocity = 6
        self.isShooting = False
        self.facing = 1
        self.isHit = False
        
    def draw(self,win):
        #draws the bullet
        if not bullet.isHit:
            pygame.draw.circle(win, (255,0,0), (bullet.x+(jack.width/2),bullet.y + (jack.height/2)), self.radius)

class enemy(object):

    def __init__(self,x,y,width,height):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkDirection = -1
        self.vel = 5
        self.walkCount = 0
        self.hitbox = (self.x+20, self.y+7, 27, 52)
        self.Injury = 0
        self.rect = pygame.Rect(self.x + 20, self.y - 15, 40, 10)


    def draw(self,win):
        if hoblit.walkDirection == -1:
            win.blit(enemyLeft[hoblit.walkCount],(hoblit.x,hoblit.y))
        else:
            win.blit(enemyRight[hoblit.walkCount], (hoblit.x,hoblit.y))

        #updates coordinates in enemy's hitbox
        self.hitbox = (self.x+20, self.y+7, 27, 52)
        #pygame.draw.rect(win,(20,0,80), hoblit.hitbox) # rectangle of the enemy

        #remaining health of the enemy
        pygame.draw.rect(win, (180, 0, 0), (self.x + 20, self.y - 15, 40, 10), 3, 3)
        pygame.draw.rect(win, (180, 0, 0), (self.x + 20, self.y - 15, 40 + hoblit.Injury, 10), 0, 3)

    def hit(self):
        print('hit')
        hoblit.Injury -= 5

class obstacle(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.height, self.width)

    def draw(self,win):

        pygame.draw.rect(win,(0,0,0),self.rect,0,3)

#creates the objects of the game

hoblit = enemy(150,400,60,80)
jack = player(200,400,60,80)
level_1 = obstacle(250,385,20,80)
run = True
bullet = projectile(jack.x,jack.y)
myFont = pygame.font.SysFont('Comis Sans MS', 30)

def drawOnScreen():

    win.blit(bg,(0,0))
    jack.draw(win)
    #displays the bullet when K_SPACE is pressed
    if bullet.isShooting:
        bullet.draw(win)
    if hoblit.Injury > -40:
        hoblit.draw(win)
    Score = myFont.render('Your score is:' + str(abs(hoblit.Injury)), 1, (0,0,0) )
    win.blit(Score, (330,25))
    level_1.draw(win)

    pygame.display.update()

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.time.delay(100)
    keys = pygame.key.get_pressed()

    def enemyGetsShot(): # when enemy is hit, lowers its life and bullet disappears
        if bullet.x < hoblit.hitbox[0] and bullet.x > (hoblit.hitbox[0] - hoblit.hitbox[2]):
            bullet.isHit = True
            hoblit.hit()

    if not bullet.isShooting: #default value of isShooting is False
        if keys[pygame.K_SPACE]:
            if jack.Right: # setting the orientation of the bullet direction
                bullet.facing = 1
            else:
                bullet.facing = -1
            bullet.isShooting = True # goes to the else part in next while round
    else:
        enemyGetsShot()
        if bullet.facing == 1: #according to orientation sends a bullet
            bullet.x += bullet.velocity
        if bullet.facing == -1:
            bullet.x -= bullet.velocity
        if bullet.x < jack.vel or bullet.x > (460 - jack.vel): #when bullet of the screen, removes it
            bullet.isShooting = False
            bullet.isHit = False #when bullet of the screen, isHit is False
            bullet.x = jack.x
            bullet.y = jack.y

    #enemy animation
    if hoblit.walkCount < 1:
        hoblit.walkCount += 1

    else:
        hoblit.walkCount = 0

    #enemy walking
    if hoblit.walkDirection == -1:
        if hoblit.x > hoblit.vel:
            hoblit.x -= hoblit.vel
        else:
            hoblit.walkDirection = 1

    if hoblit.walkDirection == 1:
        if hoblit.x < 460 - hoblit.vel:
            hoblit.x += hoblit.vel
        else:
            hoblit.walkDirection = -1
    if not pygame.Rect.colliderect(level_1.rect, jack.rect):
        if keys[pygame.K_LEFT] and jack.x > jack.vel: # going left
            jack.x -= jack.vel
            jack.walkCount += 1
            jack.Left = True
            jack.Right = False

    if keys[pygame.K_RIGHT] and jack.x < (450 - jack.vel): # going right
        jack.x += jack.vel
        jack.walkCount += 1
        jack.Right = True
        jack.Left = False
        
    if keys[pygame.K_DOWN]:
        jack.rect2.move_ip(0,10)
        jack.y -= jack.vel

    #print ('jack horni a dolni rect', jack.rect[1],jack.rect[1]+jack.rect[3])
    #print ('obstacle horni a dolni rect', level_1.rect[1], level_1.rect[1]+level_1.rect[3])

    if not jack.isJump: # starts jump
        if keys[pygame.K_UP]:
            jack.isJump = True # switch to else part
    else:
        jack.y -= jack.jumpNum * abs(jack.jumpNum) * 0.5 # going up and down
        jackkoef = jack.jumpNum * abs(jack.jumpNum) * 0.5

        new_rect = pygame.Rect(jack.rect)
        jumpCoef = jack.jumpNum*abs(jack.jumpNum)*0.5
        new_rect.move_ip(0,-jumpCoef)
        jack.jumpNum -= 1
        print ('...........jack rect',jack.rect[1]+jack.rect[3],'new rect',new_rect[1]+jack.rect[3], '.....', jumpCoef, 'jack koef', jackkoef, '.....horni y obstacle',
               level_1.rect[1])
        if pygame.Rect.colliderect(level_1.rect, new_rect):
            print ('kolize rect, pozice jackrect:', jack.rect[1]+jack.rect[3])
            jack.isJump = False
        if jack.jumpNum < -8: # stops the jump
            jack.isJump = False
            jack.jumpNum = 8


    drawOnScreen()

pygame.quit()