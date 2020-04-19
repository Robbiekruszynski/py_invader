import pygame
import random
import math

# from PIL import Image

# initalize pygame
pygame.init()

# screen creation
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("clouds.png")
# fire = pygame.imgae.load("fireball.png")

# Window title
pygame.display.set_caption('py Invaders')
icon = pygame.image.load('ship.png')
pygame.display.set_icon(icon)

# player and enemy start location
playerImg = pygame.image.load('percy.png')
playerX = 370
playerY = 480
playerX_change = 0


enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 8

for i in range (num_of_enemies):
    enemyImg.append(pygame.image.load('spaceShip.png'))
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(50, 100))
    enemyX_change.append(5.0)
    enemyY_change.append(10.0)

fireImg = pygame.image.load('pepe.png')
fireX = 0
fireY = 480
fireX_change = 0
fireY_change = 10
fire_state = "ready"

score = 0

# new values drawn on the screen
def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_ball(x, y):
    global fire_state
    fire_state = "fire"
    screen.blit(fireImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, fireX, fireY):
    distance = math.sqrt((math.pow(enemyX - fireX, 2)) + (math.pow(enemyY - fireY, 2)))
    if distance < 27:
        return True
    else:
        return False


# loop to keep the game running unless you click the close button => running == False
# GameLoop, in general...
running = True
while running:
    # consistant display runs in while loop
    screen.fill((242, 240, 238))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # keyboard movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -10.5

            if event.key == pygame.K_RIGHT:
                playerX_change = 10.5

            if event.key == pygame.K_SPACE:
                if fire_state is "ready":
                    fireX = playerX
                    fire_ball(fireX, fireY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # player movement
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 756:
        playerX = 756

    # enemy movement
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 5.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 756:
            enemyX_change[i] = -5.3
            enemyY[i] += enemyY_change[i]

        # collision
        collision = isCollision(enemyX[i], enemyY[i], fireX, fireY)
        if collision:
            fireY = 480
            fire_state = "ready"
            score += 1
            print(score)
            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # fireball movement
    if fireY <= 0:
        fireY = 480
        fire_state = "ready"


    if fire_state is "fire":
        fire_ball(fireX, fireY)
        fireY -= fireY_change

    player(playerX, playerY)

    pygame.display.update()
