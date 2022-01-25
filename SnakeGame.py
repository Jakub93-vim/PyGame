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
    def __init__(self,start, dirnx=1, dirny=0,color=(255,0,0)):

        self.color = color
        self.dirnx = 1
        self.dirny = 0
        self.pos = start

    def move(self, dirnx, dirny):
        dis = width/rows
        self.pos = (self.pos[0] + dirnx * dis, self.pos[1] + dirny * dis)

    def draw(self, surface):

        pygame.draw.rect(surface, self.color, ((self.pos[0],self.pos[1]),(24,24)))

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


        for body_position, body_part in enumerate(self.body)
            position = body_part.pos[:]
            if position in self.turns:
                turn = self.turns[body_position]
                body_part.move(turn[0],turn[1])
            else:
                print (self.body[0].pos[0])
                if self.body[0].pos[0] <= 1:
                    body_part.pos = (body_position[0] + 500,body_position[1])
                elif self.body[0].pos[0] >= 500:
                    body_part.pos = (body_position[0] - 500, body_position[1])
                elif self.body[0].pos[1] <= 1:
                    body_part.pos = (body_position[0],body_position[1] + 500)
                elif self.body[0].pos[1] >= 500:
                    body_part.pos = (body_position[0],body_position[1] - 500)
                self.body[0].move(self.dirnx, self.dirny )

    def draw(self, surface):

        self.body[0].draw(surface)
        self.body[1].draw(surface)


def redrawWindow(surface):

    win.fill((0, 0, 0))
    drawGrid(win)
    s.draw(win)
    pygame.display.update()

def drawGrid(surface):

    numLines = 20
    spaceBtwn = width/numLines
    for line in range(numLines):
        pygame.draw.line(surface, (255, 255, 255), (spaceBtwn * line, 0), (spaceBtwn * line, 500))
        pygame.draw.line(surface, (255, 255, 255), (0, spaceBtwn * line), (500, spaceBtwn * line))


s = snake((255,0,0), (51,126))

def main():

    flag = True


    while flag:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.time.delay(150)
        s.move()
        
        redrawWindow(win)

main()
