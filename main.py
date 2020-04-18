import pygame

#initalize pygame
pygame.init()

#screen creation
screen = pygame.display.set_mode((800,600 ))

#loop to keep the game running unless you click the close button => running == False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False