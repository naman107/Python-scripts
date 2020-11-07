import pygame
import sys
import random
import math

# Initialize
pygame.init()

# Screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Screen caption, icon
pygame.display.set_caption('Blocks')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BACKGROUND_COLOR = (0, 0, 0)

# Rectangle Size
RECT_SIZE = 30

# Player co-ordinates
playerPOS = [WIDTH / 2, HEIGHT - RECT_SIZE]

# Enemy co-ordinates
enemyPOS = [random.randint(0, WIDTH - RECT_SIZE), 0]
enemy_list = [enemyPOS]

# Enemy fall
enemy_fall = 7

# Clock
clock = pygame.time.Clock()

# Frame
FPS = 30

# Score
score = 0


# Dropping Enemies
def enemy_attack(enemy_list, num_enemies):
    delay = random.random()
    if len(enemy_list) < num_enemies:
        new_enemyPOS = [random.randint(0, WIDTH - RECT_SIZE), 0]
        enemy_list.append(new_enemyPOS)


def draw_enemy(enemy_list):
    for enemyPOS in enemy_list:
        pygame.draw.rect(screen, BLUE, (enemyPOS[0], enemyPOS[1], RECT_SIZE, RECT_SIZE))


def enemy_movement(enemy_list, score):
    for index, enemyPOS in enumerate(enemy_list):  # enumerate return a tuple with index and value
        if enemyPOS[1] >= 0 and enemyPOS[1] < HEIGHT:
            enemyPOS[1] += enemy_fall
        else:
            score += 1
            enemy_list.pop(index)
    return score


# Set level
def level(score, enemy_fall):
    if score <= 20:
        enemy_fall = 5
    elif score > 20 and score <= 50:
        enemy_fall = 8
    elif score > 50 and score < 80:
        enemy_fall = 10
    else:
        enemy_fall = 15

    return enemy_fall


# Collision
def isCollision(playerPOS, enemy_list):
    for enemyPOS in enemy_list:
        distance = math.sqrt((enemyPOS[0] - playerPOS[0]) ** 2 + (enemyPOS[1] - playerPOS[1]) ** 2)
        collison_boundary = math.sqrt(2) * RECT_SIZE
        if distance <= collison_boundary:
            return True
        else:
            return False


# Game Loop
on = True
while on:
    screen.fill(BACKGROUND_COLOR)
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            x, y = playerPOS
            if event.key == pygame.K_LEFT:
                x -= RECT_SIZE
            elif event.key == pygame.K_RIGHT:
                x += RECT_SIZE
            playerPOS = [x, y]

    enemy_attack(enemy_list, 10)
    enemy_fall = level(score, enemy_fall)
    score = enemy_movement(enemy_list, score)

    if isCollision(playerPOS, enemy_list):
        print('You lost!')
        print('Score: ' + str(score))
        on = False
        break
    draw_enemy(enemy_list)
    pygame.draw.rect(screen, RED, (playerPOS[0], playerPOS[1], RECT_SIZE, RECT_SIZE))
    pygame.display.update()
