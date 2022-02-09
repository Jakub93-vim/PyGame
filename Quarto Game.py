import pygame

width = 800
height = 800

pygame.init()
win = pygame.display.set_mode((width, height))

run = True

class Token(object):

    def __init__(self, shape, color, inside_circle, position, size):
        self.shape = shape
        self.color = color
        self.inside_circle = inside_circle
        self.position = position
        self.size = size
        
    def returnMiddle(self,position):
        x = position[0] + self.size/2
        y = position[1] + self.size/2
        return x,y
        
    def draw (self, surface):
        
        if self.shape == 'circle':
            pygame.draw.circle(surface, self.color, self.position, self.size)
            if self.inside_circle:
                pygame.draw.circle(surface, (0,0,0), self.position, 10)

        if self.shape == 'rect':
            pygame.draw.rect(surface, self.color, (self.position[0],self.position[1],self.size,self.size))
            if self.inside_circle:
                pygame.draw.circle(surface, (0,0,0), self.returnMiddle(self.position), 10)
    def select(self):
        pass
    def move(self):
        pass

tokens = []

Black_1 = Token('circle', (255,255,255), False, (550,420), 20)
Black_2 = Token('rect', (255,255,255), False, (500,420), 40)
Black_3 = Token('rect', (255,255,255), True, (450,420), 40)

tokens.append(Black_1)
tokens.append(Black_2)
tokens.append(Black_3)

def drawGamefield(surface):

    numCircles = 3
    spaceBetween = width/numCircles - 120

    pygame.draw.circle(surface, (255,255,255), (width/2,height/2), 380, width = 5)
    pygame.draw.rect(surface, (255,255,255), (290,550,210,200), 2, border_radius=10)

    for circle_x in range(numCircles):
        for circle_y in range (numCircles):
            pygame.draw.circle(surface, (255,255,255), (width/3 + spaceBetween*circle_x -20,
                                                        height/5 + spaceBetween*circle_y), 40, width = 2)


def redrawWindow():

    drawGamefield(win)
    for i in tokens:
        i.draw(win)
    pygame.display.update()

def mainLoop ():

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.time.delay(150)

        redrawWindow()

mainLoop()


