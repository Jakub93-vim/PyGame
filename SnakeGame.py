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

    def move(self, dirnx, dirny):

        pass

    def draw(self, surface, eyes=False):

        pygame.draw.rect(surface, self.color, ((),()))

class snake(object):

    def __init__(self, color, pos):

        self.color = color
        self.pos = pos
        

    def move(self):

        keys = pygame.key.get_pressed()

        for key in keys:

            if keys[pygame.K_LEFT]:
                pass
        pass

    def draw(self, surface):

        pass


def redrawWindow(surface):

    drawGrid(win)
    pygame.display.update()

def drawGrid(surface):

    numLines = 20
    spaceBtwn = width/numLines
    for line in range(numLines):
        pygame.draw.line(surface, (255, 255, 255), (spaceBtwn * line, 0), (spaceBtwn * line, 500))
        pygame.draw.line(surface, (255, 255, 255), (0, spaceBtwn * line), (500, spaceBtwn * line))


s = snake((255,0,0), (10,10))

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
