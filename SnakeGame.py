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

    def __init__(self, start, dirnx=1, dirny=0,color=(255,0,0)):
        self.start = start

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass

class snake(object):

    def __init__(self, color, pos):
        pass

    def move(self):
        pass

    def draw(self):
        pass


def redrawWindow(surface):
    surface.fill((0,0,0))
    drawGrid(surface)
    pygame.display.update()

def drawGrid(surface):

    numLines = 20
    spaceBtwn = width/numLines
    for line in range(numLines):
        pygame.draw.line(surface, (255, 255, 255), (spaceBtwn * line, 0), (spaceBtwn * line, 500))
        pygame.draw.line(surface, (255, 255, 255), (0, spaceBtwn * line), (500, spaceBtwn * line))


def main():

    flag = True

    #clock = pygame.time.Clock()

    while flag:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.time.delay(50)
        #clock.tick(10)
        
        redrawWindow(win)

main()
