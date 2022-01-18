import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

width = 500
height = 500
rows = 20

win = pygame.display.set_mode((width, height))

class cube(object):
    def __init__(self, dirnx=1, dirny=0,color=(255,0,0)):

        self.color = color
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = [20,20]

    def move(self, dirnx, dirny):

        self.pos[0] += dirnx
        self.pos[1] += dirny

    def draw(self, surface):


        pygame.draw.rect(surface, self.color, ((self.pos[0],self.pos[1]),(10,10)))

class snake(object):

    def __init__(self, color, pos):

        self.color = color
        self.pos = pos
        

    def move(self):

        keys = pygame.key.get_pressed()

        for key in keys:

            if keys[pygame.K_LEFT]:
                c.dirnx = -1
                c.dirny = 0
            if keys[pygame.K_UP]:
                c.dirnx = 0
                c.dirny = -1
            if keys[pygame.K_DOWN]:
                c.dirnx = 0
                c.dirny = 1
            if keys[pygame.K_RIGHT]:
                c.dirnx = 1
                c.dirny = 0
        c.move(c.dirnx,c.dirny)

    def draw(self, surface):

        pass


def redrawWindow(surface):

    drawGrid(win)
    c.draw(win)
    pygame.display.update()

def drawGrid(surface):

    numLines = 20
    spaceBtwn = width/numLines
    for line in range(numLines):
        pygame.draw.line(surface, (255, 255, 255), (spaceBtwn * line, 0), (spaceBtwn * line, 500))
        pygame.draw.line(surface, (255, 255, 255), (0, spaceBtwn * line), (500, spaceBtwn * line))


s = snake((255,0,0), (10,10))
c = cube()

def main():

    flag = True


    while flag:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.time.delay(150)
        s.move()
        
        redrawWindow(win)

main()
