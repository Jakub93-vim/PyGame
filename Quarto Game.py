import pygame

width = 800
height = 800

pygame.init()
win = pygame.display.set_mode((width, height))

run = True
selected = False

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
            pygame.draw.circle(surface, self.color, self.position, self.size/2)
            if self.inside_circle:
                pygame.draw.circle(surface, (0,0,0), self.position, 10)

        if self.shape == 'rect':
            x_moved = self.middleToCorner(self.position)[0]
            y_moved = self.middleToCorner(self.position)[1]
            pygame.draw.rect(surface, self.color, (x_moved,y_moved,self.size,self.size))
            if self.inside_circle:
                pygame.draw.circle(surface, (0,0,0), self.position, 10)

    def mouseAboveToken(self, token):

        self.isAbove = False

        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]
        half_size = token.size/2


        if token.position[0]-half_size < mouse_x and token.position[0] + half_size > mouse_x:
            if token.position[1] - half_size < mouse_y and token.position[1] + half_size > mouse_y:
                self.isAbove = True
                #position info
                '''
                print ('x souradnice:',token.position[0],
                       'x pozice mysi:', mouse_x,
                       'x + velikost:', token.position[0] + token.size,"\n",
                       'y souradnice:',token.position[1],
                       'y pozice mysi:', mouse_y,
                       'y + velikost:', token.position[1] + token.size)
                '''

        return self.isAbove


    def select(self):
        global selected

        if not selected:
            self.color = (230,170,50)
            selected = True

    def move(self):
        self.position = (self.position[0] + 50, self.position[1])

tokens = []
red = (170,0,0)
blue = (0,40,160)

Red_1 = Token('circle', red , False, (320,585), 40)
Red_2 = Token('rect', red , False, (390,585), 40)
Red_3 = Token('rect', red , True, (460,585), 40)

Blue_1 = Token('circle', blue , False, (320,660), 40)
Blue_2 = Token('rect', blue , False, (390,660), 40)
Blue_3 = Token('rect', blue , True, (460,660), 40)

tokens.extend([Red_1, Red_2, Red_3, Blue_1, Blue_2, Blue_3])

setOfPosition = set()
def drawGamefield(surface):

    numCircles = 3
    spaceBetween = width/numCircles - 120

    pygame.draw.circle(surface, (255,255,255), (width/2,height/2), 380, width = 5)
    pygame.draw.rect(surface, (255,255,255), (290,550,210,200), 2, border_radius=10)

    for x in range(numCircles):
        for y in range (numCircles):
            circle_x_pos = width/3 + spaceBetween*x -20
            circle_y_pos = height/5 + spaceBetween*y
            pygame.draw.circle(surface, (255,255,255), (circle_x_pos, circle_y_pos), 40, width = 2)

            circle_x_pos = int(circle_x_pos)
            circle_y_pos = int(circle_y_pos)
            setOfPosition.add((circle_x_pos,circle_y_pos))

    circPosDict(setOfPosition)


def circPosDict(setOfPosition):

    positionDict = {}
    letterPosition = ["A","B","C"]
    numberPosition = ["1","2","3"]

    for value in setOfPosition:
        for letter in letterPosition:
            for number in numberPosition:
                positionDict[letter + number] = value


    print(positionDict)

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

        if pygame.mouse.get_pressed() == (1,0,0):
            for x in tokens:
                if x.mouseAboveToken(x):
                    x.select()


        pygame.time.delay(150)

        redrawWindow()

mainLoop()


