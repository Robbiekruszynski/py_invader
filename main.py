import pygame

#initalize pygame
pygame.init()

#screen creation
screen = pygame.display.set_mode((800,600 ))


#Window title
pygame.display.set_caption('py Invaders')
icon = pygame.image.load('ship.png')
pygame.display.set_icon(icon)

#loop to keep the game running unless you click the close button => running == False
#GameLoop, in general...
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#consistant display runs in while loop
    screen.fill((107,97,130))
    pygame.display.update()
