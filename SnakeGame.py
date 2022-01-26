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

class cube(object):
    rows = 20
    def __init__(self,start, dirnx=1, dirny=0,color=(255,0,0)):

        self.color = color
        self.dirnx = 1
        self.dirny = 0
        self.pos = start

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + dirnx, self.pos[1] + dirny)

    def draw(self, surface):
        dis = width / rows
        pygame.draw.rect(surface, self.color, ((self.pos[0]*dis+1,self.pos[1]*dis+1),(24,24)))

class snake(object):
    body = []
    turns = {}
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
            print (body_part.pos[0])
            if position in self.turns:
                turn = self.turns[position]
                body_part.move(turn[0],turn[1])
            else:
                if body_part.pos[0] <= 1 and body_part.dirnx == -1:
                    body_part.pos = (body_part.rows,body_part.pos[1])
                elif body_part.pos[0] >= 20 and body_part.dirnx == 1:
                    body_part.pos = (0, body_part.pos[1])
                elif body_part.pos[1] <= 1 and body_part.dirny == -1:
                    body_part.pos = (body_part.pos[0],body_part.rows)
                elif body_part.pos[1] >= 20 and body_part.dirny == 1:
                    body_part.pos = (body_part.pos[0],0)
                body_part.move(self.dirnx, self.dirny )

    def draw(self, surface):

        self.body[0].draw(surface)

    def addCube (self):

        tail = self.body[-1]
        dx = tail.dirn


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

        pygame.time.delay(150)
        s.move()
        
        redrawWindow(win)

main()
