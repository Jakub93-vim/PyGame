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


def main():

