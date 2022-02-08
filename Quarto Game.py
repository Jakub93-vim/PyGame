import pygame

width = 500
height = 500

pygame.init()
win = pygame.display.set_mode((width, height))

run = True

def mainLoop ():

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.time.delay(150)

mainLoop()


