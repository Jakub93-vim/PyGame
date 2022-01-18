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
    def __init__(self,start, dirnx=1, dirny=0,color=(255,0,0)):

        self.color = color
        self.dirnx = 1
        self.dirny = 0
        self.pos = start

    def move(self, dirnx, dirny):
        dis = width/rows
        self.pos[0] += dirnx * dis
        self.pos[1] += dirny * dis

    def draw(self, surface):

        pygame.draw.rect(surface, self.color, ((self.pos[0],self.pos[1]),(24,24)))

class snake(object):
    body = []
    def __init__(self, color, pos):

        self.color = color
        self.body.append(cube(pos))
        self.dirnx = 0
        self.dirny = 1
        

    def move(self):

        keys = pygame.key.get_pressed()

        for key in keys:

            if keys[pygame.K_LEFT]:
                self.dirnx = -1
                self.dirny = 0
            if keys[pygame.K_UP]:
                self.dirnx = 0
                self.dirny = -1
            if keys[pygame.K_DOWN]:
                self.dirnx = 0
                self.dirny = 1
            if keys[pygame.K_RIGHT]:
                self.dirnx = 1
                self.dirny = 0

    def draw(self, surface):

        self.body[0].draw(surface)


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

        pygame.time.delay(150)
        s.move()
        
        redrawWindow(win)

main()
