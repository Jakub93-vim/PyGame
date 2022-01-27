import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

width = 500
height = 500
rows = 20

pygame.init()
win = pygame.display.set_mode((width, height))

class cube(object): # cube class that makes the part of the snake and food
    rows = 20
    w = 500

    def __init__(self,start, dirnx=1, dirny=0,color=(255,0,0)):

        self.color = color
        self.dirnx = 1 # direction of moving the cube
        self.dirny = 0 # direction of moving the cube
        self.pos = start # start position, input value when object is created

    def move(self, dirnx, dirny): # moving single cube
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny) # changing the position

    def draw(self, surface, eyes = False):
        dis = self.w / self.rows
        i = self.pos[0]
        j = self.pos[1]
        pygame.draw.rect(surface, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2)) # drawing one cube

        if eyes: # draws eyes in the first cube
            centre = dis // 2
            radius = 3
            circleMiddle = (i * dis + centre - radius, j * dis + 8)
            circleMiddle2 = (i * dis + dis - radius * 2, j * dis + 8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)

class snake(object):
    body = [] # list of cube objects
    turns = {} # dictionary of turns that user makes
    def __init__(self, color, pos):

        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1
        

    def move(self):

        keys = pygame.key.get_pressed()

        for key in keys:

            if keys[pygame.K_LEFT]:
                self.dirnx = -1
                self.dirny = 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            if keys[pygame.K_UP]:
                self.dirnx = 0
                self.dirny = -1
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            if keys[pygame.K_DOWN]:
                self.dirnx = 0
                self.dirny = 1
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            if keys[pygame.K_RIGHT]:
                self.dirnx = 1
                self.dirny = 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]


        for body_position, body_part in enumerate(self.body):
            position = body_part.pos[:]
            if position in self.turns:
                turn = self.turns[position]
                body_part.move(turn[0],turn[1])
                if body_position == len(self.body)-1:
                    self.turns.pop(position)
            else:
                if body_part.pos[0] <= 1 and body_part.dirnx == -1:
                    body_part.pos = (body_part.rows,body_part.pos[1])
                elif body_part.pos[0] >= 20 and body_part.dirnx == 1:
                    body_part.pos = (0, body_part.pos[1])
                elif body_part.pos[1] <= 1 and body_part.dirny == -1:
                    body_part.pos = (body_part.pos[0],body_part.rows)
                elif body_part.pos[1] >= 20 and body_part.dirny == 1:
                    body_part.pos = (body_part.pos[0],0)
                body_part.move(body_part.dirnx, body_part.dirny )

    def draw(self, surface):

        for body_position, body_part in enumerate(self.body):

            if body_position ==0:
                body_part.draw(surface,True)
            else:
                body_part.draw(surface)

    def addCube (self):

        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
        elif dx == -1 and dy ==0:
            self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0],tail.pos[1]+1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1


def redrawWindow(surface):
    global rows, snack
    win.fill((0, 0, 0))
    drawGrid(win)
    s.draw(win)
    snack.draw(surface)
    pygame.display.update()

def drawGrid(surface):

    numLines = 20
    spaceBtwn = width/numLines
    for line in range(numLines):
        pygame.draw.line(surface, (255, 255, 255), (spaceBtwn * line, 0), (spaceBtwn * line, 500))
        pygame.draw.line(surface, (255, 255, 255), (0, spaceBtwn * line), (500, spaceBtwn * line))

def randomSnack(rows, snake):

    positions = snake.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            continue
        else:
            break

    return (x,y)

def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


s = snake((255,0,0), (10,10))
snack = cube(randomSnack(rows, s), color=(0, 255, 0))

def main():
    global rows, s, snack
    flag = True
    snack = cube(randomSnack(rows, s), color=(0, 255, 0))

    while flag:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows,s),color=(0,255,0))

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x + 1:])):
                print('Score: ', len(s.body))
                message_box('You Lost!', 'Play again...')
                s.reset((10, 10))
                break

        pygame.time.delay(150)
        s.move()
        
        redrawWindow(win)

main()
