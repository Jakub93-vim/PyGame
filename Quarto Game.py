import pygame, math

width = 800 # game window dimensions
height = 800

pygame.init()
win = pygame.display.set_mode((width, height))

run = True # game loop

class Token():

    def __init__(self, player, shape, color, inside_circle, position, size):
        self.player = player
        self.shape = shape
        self.color = color
        self.inside_circle = inside_circle # token with a circle inside
        self.position = position
        self.size = size
        self.selected = False

    
    def middleToCorner(self, position): # rectangle position correction, from edge to the middle
        x = position[0] - self.size / 2
        y = position[1] - self.size / 2
        return int(x),int(y)
        
    def draw (self, surface): # drawing tokens
        
        if self.shape == 'circle':
            pygame.draw.circle(surface, self.color, self.position, self.size/2)
            if self.inside_circle: # token with circle in the middle
                pygame.draw.circle(surface, (0,0,0), self.position, 10)

        if self.shape == 'rect':
            x_moved = self.middleToCorner(self.position)[0]
            y_moved = self.middleToCorner(self.position)[1]
            pygame.draw.rect(surface, self.color, (x_moved,y_moved,self.size,self.size))
            if self.inside_circle:
                pygame.draw.circle(surface, (0,0,0), self.position, 10)

def mouseAboveToken(token): # checks whether mouse is above token

    isAbove = False

    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]
    half_size = token.size/2


    if token.position[0]-half_size < mouse_x and token.position[0] + half_size > mouse_x: # x coordinates
        if token.position[1] - half_size < mouse_y and token.position[1] + half_size > mouse_y: # y coordinates
            isAbove = True
            #position info
            '''
            print ('x coor:',token.position[0],
                   'x mouse pos:', mouse_x,
                   'x + size:', token.position[0] + token.size,"\n",
                   'y coor:',token.position[1],
                   'y mouse pos:', mouse_y,
                   'y + size:', token.position[1] + token.size)
            '''

    return isAbove



tokens = []
red = (170,0,0)
blue = (0,40,160)

Red_1 = Token(1,'circle', red , False, (320,585), 40)
Red_2 = Token(1,'rect', red , False, (390,585), 40)
Red_3 = Token(1,'rect', red , True, (460,585), 40)

Blue_1 = Token(2,'circle', blue , False, (320,660), 40)
Blue_2 = Token(2,'rect', blue , False, (390,660), 40)
Blue_3 = Token(2,'rect', blue , True, (460,660), 40)

tokens.extend([Red_1, Red_2, Red_3, Blue_1, Blue_2, Blue_3])


listOfPosition = [] # positions of the game field circles
def drawGamefield(surface):

    numCircles = 3 # amount of circles in the field
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
            if ((circle_x_pos, circle_y_pos)) not in listOfPosition: #filling the list with the position
                listOfPosition.append((circle_x_pos, circle_y_pos))

    circPosDict(listOfPosition) # calls function with the list to make a dictionary and name the positions

positionDict = {}
def circPosDict(listOfPosition):
    letterPosition = ["A","B","C"] # defining the name position for the dict
    numberPosition = ["1","2","3"]

    listCount = 0
    for letter in letterPosition:
        for number in numberPosition:
            positionDict[letter + number] = listOfPosition[listCount] # making dict of positions {'A1': (246, 160), 'A2': (246, 306),.....}
            listCount += 1 # selecting the items from the listOfPositions

def mouseAboveCircle(): # checks if mouse is above the game field circle

    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]

    for circPosition in  listOfPosition:
        if math.sqrt ( (mouse_x - circPosition[0])**2 + (mouse_y - circPosition[1])**2) < 40: # with equation of circle checks mouse above game field circle
            return True


def select(token):
    token.color = (230,170,50)

def move(token):

    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]
    for circPosition in  listOfPosition: # takes all positions from the list
        if math.sqrt ( (mouse_x - circPosition[0])**2 + (mouse_y - circPosition[1])**2) < 40: #checks if there was a click in the circle
            token.position = [circPosition[0], circPosition[1]] # if there was a click moves the token to the position
            if token.player == 1:
                token.color = red
            if token.player == 2:
                token.color = blue

def redrawWindow(): # window update
    
    win.fill((0, 0, 0)) # fills with black color to remove old drawings
    drawGamefield(win) # draws gamefield
    for i in tokens: # draws all tokens
        i.draw(win)
    pygame.display.update()

def mainLoop ():

    numOfClicks = 0 # counts num of clicks from the user
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if pygame.mouse.get_pressed() == (1,0,0): # click

            print ('pozice mys', pygame.mouse.get_pos(), 'pozice token', Red_1.position)
            for x in tokens:
                if numOfClicks == 0: # first click selects the token
                    if mouseAboveToken(x): # checks if the click was above token
                        numOfClicks += 1
                        x.selected = True # marks selected token
                        select(x) # changes its color to selected

                if numOfClicks == 1 and x.selected == True and mouseAboveCircle(): # second click moves the token if mouse above circle and token selected
                    move(x)
                    print ('second click')
                    numOfClicks = 0
                    x.selected = False # deselection of the token




        pygame.time.delay(150)

        redrawWindow()


mainLoop()


