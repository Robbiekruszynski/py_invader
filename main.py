import pygame

#initalize pygame
pygame.init()

#screen creation
screen = pygame.display.set_mode((800,600 ))


#Window title
pygame.display.set_caption('py Invaders')
icon = pygame.image.load('ship.png')
pygame.display.set_icon(icon)

#player start location
playerImg = pygame.image.load('ship.png')
playerX = 370
playerY = 480
playerX_change = 0

#new values drawn on the screen
def player(x, y):
    screen.blit(playerImg, (x, y))


#loop to keep the game running unless you click the close button => running == False
#GameLoop, in general...
running = True
while running:
    # consistant display runs in while loop
    screen.fill((107, 97, 130))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #keyboard movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 1.8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    #player movement
    playerX += playerX_change
    player(playerX, playerY)
    pygame.display.update()
