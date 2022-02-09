import pygame

width = 800
height = 800

pygame.init()
win = pygame.display.set_mode((width, height))

run = True

class Token(object):

    def __init__(self, shape, color, inside_circle, position):
        self.shape = shape
        self.color = color
        self.inside_circle = inside_circle
        self.position = position
        
    def draw (self, surface):
        
        if self.shape == 'circle':
            pygame.draw.circle(surface, self.color, self.position, 20)
        
    def select(self):
        pass
    def move(self):
        pass

Black_1 = Token('circle', (255,255,255), False, (550,420))


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
    Black_1.draw(win)
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


