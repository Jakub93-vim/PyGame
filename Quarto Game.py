import pygame, math

width = 800 # game window dimensions
height = 800

pygame.init()
myfont = pygame.font.SysFont("monospace", 25,True) # initialize font
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
            if self.selected == True:
                self.color = (230,170,50)
            pygame.draw.circle(surface, self.color, self.position, self.size/2)
            if self.inside_circle: # token with circle in the middle
                pygame.draw.circle(surface, (80, 80, 80), self.position, 10)

        if self.shape == 'rect':
            x_moved = self.middleToCorner(self.position)[0]
            y_moved = self.middleToCorner(self.position)[1]
            if self.selected == True:
                self.color = (230,170,50)
            pygame.draw.rect(surface, self.color, (x_moved,y_moved,self.size,self.size))
            if self.inside_circle:
                pygame.draw.circle(surface, (80, 80, 80), self.position, 10)

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
Red_4 = Token(1,'rect', red , True, (460,710), 40)
Red_5 = Token(1,'circle', red , True, (390,710), 40)

Blue_1 = Token(2,'circle', blue , False, (320,650), 40)
Blue_2 = Token(2,'rect', blue , False, (390,650), 40)
Blue_3 = Token(2,'rect', blue , True, (460,650), 40)
Blue_4 = Token(2,'circle', blue , True, (320,710), 40)

tokens.extend([Red_1, Red_2, Red_3, Red_4, Red_5, Blue_1, Blue_2, Blue_3, Blue_4])


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
    
    win.fill((80, 80, 80)) # fills with black color to remove old drawings
    drawGamefield(win) # draws gamefield
    for i in tokens: # draws all tokens
        i.draw(win)
    if PlayerRed:

        label = myfont.render("Player Red wins!", 1, (0, 0, 0))
        win.blit(label, (20, 20))
    if PlayerBlue:

        label = myfont.render("Player Blue wins!", 1, (0, 0, 0))
        win.blit(label, (20, 20))
    pygame.display.update()

    if BlueTurn:

        label = myfont.render("Blue turn!", 1, (blue))
        win.blit(label, (580, 520))
    pygame.display.update()

    if RedTurn:

        label = myfont.render("Red turn!", 1, (red))
        win.blit(label, (120, 520))
    pygame.display.update()


def mainLoop ():

    numOfClicks = 0 # counts num of clicks from the user

    global PlayerRed, PlayerBlue, BlueTurn, RedTurn
    PlayerRed = False
    PlayerBlue = False
    BlueTurn = True
    RedTurn = False
    gameEvalCircHoriz = [[0,0,0],[0,0,0],[0,0,0]]
    gameEvalCircVerti = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    gameEvalRectHoriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    gameEvalRectVerti = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if pygame.mouse.get_pressed() == (1,0,0): # click

            for x in tokens:
                if numOfClicks == 0: # first click selects the token
                    if mouseAboveToken(x): # checks if the click was above token
                        numOfClicks += 1
                        x.selected = True # marks selected token
                        #select(x) # changes its color to selected


                if numOfClicks == 1 and x.selected == True and mouseAboveCircle(): # second click moves the token if mouse above circle and token selected
                    move(x)
                    numOfClicks = 0
                    x.selected = False # deselection of the token

                    if BlueTurn == False:
                        BlueTurn = True
                    else:
                        BlueTurn = False

                    if RedTurn == False:
                        RedTurn = True
                    else:
                        RedTurn = False


                    print (x.position, positionDict.get('B2'))


        posNamesHoriz = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
        posNamesVerti = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']

        for token in tokens:
            name = 0
            if token.shape == 'circle':
                for i in range (3):
                    for j in range (3):
                        if tuple (token.position) == positionDict.get(posNamesHoriz[name]):
                            gameEvalCircHoriz[i][j] = 1
                        if name <8:
                            name += 1

            name = 0
            if token.shape == 'circle':
                for i in range(3):
                    for j in range(3):
                        if tuple(token.position) == positionDict.get(posNamesVerti[name]):
                            gameEvalCircVerti[i][j] = 1
                        if name < 8:
                            name += 1

            name = 0
            if token.shape == 'rect':
                for i in range(3):
                    for j in range(3):
                        if tuple(token.position) == positionDict.get(posNamesHoriz[name]):
                            gameEvalRectHoriz[i][j] = 1
                        if name < 8:
                            name += 1

            name = 0
            if token.shape == 'rect':
                for i in range(3):
                    for j in range(3):
                        if tuple(token.position) == positionDict.get(posNamesVerti[name]):
                            gameEvalRectVerti[i][j] = 1
                        if name < 8:
                            name += 1


        if gameEvalCircHoriz[0][0] == 1 and gameEvalCircHoriz[0][1]==1 and gameEvalCircHoriz[0][2]==1:
            PlayerRed = True
        elif gameEvalCircHoriz[1][0] == 1 and gameEvalCircHoriz[1][1]==1 and gameEvalCircHoriz[1][2]==1:
            PlayerRed = True
        elif gameEvalCircHoriz[2][0] == 1 and gameEvalCircHoriz[2][1]==1 and gameEvalCircHoriz[2][2]==1:
            PlayerRed = True

        if gameEvalCircVerti[0][0] == 1 and gameEvalCircVerti[0][1]==1 and gameEvalCircVerti[0][2]==1:
            PlayerRed = True
        elif gameEvalCircVerti[1][0] == 1 and gameEvalCircVerti[1][1]==1 and gameEvalCircVerti[1][2]==1:
            PlayerRed = True
        elif gameEvalCircVerti[2][0] == 1 and gameEvalCircVerti[2][1]==1 and gameEvalCircVerti[2][2]==1:
            PlayerRed = True

        if gameEvalRectHoriz[0][0] == 1 and gameEvalRectHoriz[0][1]==1 and gameEvalRectHoriz[0][2]==1:
            PlayerRed = True
        elif gameEvalRectHoriz[1][0] == 1 and gameEvalRectHoriz[1][1]==1 and gameEvalRectHoriz[1][2]==1:
            PlayerRed = True
        elif gameEvalRectHoriz[2][0] == 1 and gameEvalRectHoriz[2][1]==1 and gameEvalRectHoriz[2][2]==1:
            PlayerRed = True

        if gameEvalRectVerti[0][0] == 1 and gameEvalRectVerti[0][1]==1 and gameEvalRectVerti[0][2]==1:
            PlayerRed = True
        elif gameEvalRectVerti[1][0] == 1 and gameEvalRectVerti[1][1]==1 and gameEvalRectVerti[1][2]==1:
            PlayerRed = True
        elif gameEvalRectVerti[2][0] == 1 and gameEvalRectVerti[2][1]==1 and gameEvalRectVerti[2][2]==1:
            PlayerRed = True


        pygame.time.delay(150)
        redrawWindow()


mainLoop()


