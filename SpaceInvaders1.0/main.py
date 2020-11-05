import pygame
import random
import math
from pygame import mixer

# Initialize pygame
pygame.init()

# Game Screen
screen = pygame.display.set_mode((800, 600))

# Background Music
mixer.music.load('bg.mp3')
mixer.music.play(-1)

# Getting images
screen_icon = pygame.image.load('screen_icon.png')
spaceshipImg = pygame.image.load('spaceship.png')
bulletImg = pygame.image.load('bullet.png')
enemyImg = pygame.image.load('enemy.png')

# Set background icon
pygame.display.set_icon(screen_icon)

# Set window title
pygame.display.set_caption('Space Invaders')

# Default spaceship co-ordinates
spaceship_x = 400
spaceship_y = 520
spaceship_x_change = 0

# Default enemy co-ordinates
# enemy_x = random.randint(0, 560)
# enemy_y = random.randint(0, 120)
# enemy_x_change = 0.3
# enemy_y_change = 20

# For multiple enemies
enemyImg = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_enemies = 10

for i in range(num_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemy_x.append(random.randint(0, 560))
    enemy_y.append(random.randint(0, 120))
    enemy_x_change.append(0.3)
    enemy_y_change.append(40)

# Default bullet co-ordinates and state
bullet_x = 0
bullet_y = spaceship_y
bullet_y_change = 8
bullet_state = "ready"

# Score
score_value = 0

# Text on screen
score_text = pygame.font.Font('freesansbold.ttf', 32)
game_over_text = pygame.font.Font('freesansbold.ttf', 64)


# Paint screen functions
def spaceship(x, y):
    screen.blit(spaceshipImg, (x, y))


# For 1 enemy
# def enemy(x, y):
#     screen.blit(enemyImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x, y))


def show_score(x, y):
    score = score_text.render('Score: ' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over():
    text = game_over_text.render("GAME OVER!", True, (255, 255, 255))
    screen.blit(text, (200, 250))


# Collision function
def isCollision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow((enemy_x - bullet_x), 2) + math.pow((enemy_y - bullet_y), 2))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True

while running:
    # pygame.time.delay(1000)
    screen.fill((0, 0, 0))
    show_score(10, 10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                spaceship_x_change = -0.8
            if event.key == pygame.K_RIGHT:
                spaceship_x_change = 0.8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                spaceship_x_change = 0
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    mixer.Sound('shoot.wav').play()
                    bullet_x = spaceship_x + 16
                    fire_bullet(bullet_x, bullet_y)
    if bullet_state is "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    if bullet_y <= 0:
        bullet_y = spaceship_y
        bullet_state = "ready"

    spaceship_x += spaceship_x_change

    # Setting boundaries
    if spaceship_x <= 3:
        spaceship_x = 3
        spaceship_x_change = 0

    if spaceship_x > 730:
        spaceship_x = 730
        spaceship_x_change = 0

    # Enemy Movement and setting boundaries
    for i in range(num_enemies):
        if enemy_y[i] > 450:
            for j in range(num_enemies):
                enemy_y[j] = 2000
            game_over()
            break

        enemy_x[i] += enemy_x_change[i]

        if enemy_x[i] > 760:
            enemy_x_change[i] = -0.6
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] <= 0:
            enemy_x_change[i] = 0.6
            enemy_y[i] += enemy_y_change[i]

        # Collison
        collision = isCollision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)

        if collision:
            mixer.Sound('explosion.wav').play()
            score_value += 1
            bullet_y = spaceship_y
            bullet_state = "ready"
            enemy_x[i] = random.randint(0, 560)
            enemy_y[i] = random.randint(0, 120)

        enemy(enemy_x[i], enemy_y[i], i)

    spaceship(spaceship_x, spaceship_y)
    pygame.display.update()
