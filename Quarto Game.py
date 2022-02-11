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
    
    def middleToCorner(self, position):
        x = position[0] - self.size / 2
        y = position[1] - self.size / 2
        return int(x),int(y)
        
    def draw (self, surface):
        
        if self.shape == 'circle':
            pygame.draw.circle(surface, self.color, self.position, self.size)
            if self.inside_circle:
                pygame.draw.circle(surface, (0,0,0), self.position, 10)

        if self.shape == 'rect':
            x_moved = self.middleToCorner(self.position)[0]
            y_moved = self.middleToCorner(self.position)[1]
            pygame.draw.rect(surface, self.color, (x_moved,y_moved,self.size,self.size))
            if self.inside_circle:
                pygame.draw.circle(surface, (0,0,0), self.position, 10)

    def select(self):
        pass
    def move(self):
        self.position = (self.position[0] + 50, self.position[1])

tokens = []
red = (170,0,0)
blue = (0,40,160)

Red_1 = Token('circle', red , False, (320,585), 20)
Red_2 = Token('rect', red , False, (390,585), 40)
Red_3 = Token('rect', red , True, (460,585), 40)

Blue_1 = Token('circle', blue , False, (320,660), 20)
Blue_2 = Token('rect', blue , False, (390,660), 40)
Blue_3 = Token('rect', blue , True, (460,660), 40)

tokens.extend([Red_1, Red_2, Red_3, Blue_1, Blue_2, Blue_3])

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

        if event.type == pygame.MOUSEBUTTONUP:

            print ('mouse button')
            Red_1.move()

        print (pygame.mouse.get_pos())


        pygame.time.delay(150)

        redrawWindow()

mainLoop()


