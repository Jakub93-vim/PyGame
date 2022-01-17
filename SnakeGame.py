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

        pass

    def move(self, dirnx, dirny):

        pass

    def draw(self, surface, eyes=False):

        pass

class snake(object):



    def move(self):

        keys = pygame.key.get_pressed()

        for key in keys:

            if keys[pygame.K_LEFT]:
                pass
        pass



    def draw(self, surface):

        pass


def redrawWindow(surface):

    pass

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
