import random
import math
import pygame
from PIL import Image
from pygame import mixer

# from PIL import Image

# initalize pygame
pygame.init()
cloock = pygame.time.Clock()

# screen creation
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("space.jpeg")

# music
mixer.music.load('game.aiff')
# -1 will play the music on a loop
mixer.music.play(-1)

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

for i in range(num_of_enemies):
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

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 24)

scoreX = 10
scoreY = 10

over = pygame.font.Font('freesansbold.ttf', 64)


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_ball(x, y):
    global fire_state
    fire_state = "fire"
    screen.blit(fireImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, fireX, fireY):
    distance = math.sqrt((math.pow(enemyX - fireX, 2)) +
                         (math.pow(enemyY - fireY, 2)))
    if distance < 27:
        return True
    else:
        return False


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over():
    over_text = over.render('GAME OVER', True, (255, 255, 255))
    screen.blit(over_text, (250, 250))


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
                    fire_Sound = mixer.Sound('lazer.ogg')
                    fire_Sound.play()
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

        # Game Over
        if enemyY[i] > 440:
            for k in range(num_of_enemies):
                # moves all enemies out of the screen
                enemyY[k] = 2000
                game_over()
                break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 10.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 756:
            enemyX_change[i] = -10.3
            enemyY[i] += enemyY_change[i]

        # collision
        collision = isCollision(enemyX[i], enemyY[i], fireX, fireY)
        if collision:
            kill_Sound = mixer.Sound('dead.wav')
            kill_Sound.play()
            fireY = 480
            fire_state = "ready"
            score_value += 1
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
    show_score(scoreX, scoreY)
    pygame.display.update()
