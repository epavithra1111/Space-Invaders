import pygame
import math
import random

#intialise the pygame
pygame.init()

screen = pygame.display.set_mode((600, 500))   #createscreen

#title and icon
pygame.display.set_caption("pawo staa")
img = pygame.image.load('logo.png')
pygame.display.set_icon(img)

#player
playerimg = pygame.image.load('rifle.png')
playerX = 260
playerY = 350
playerX_change = 0

#enemy
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemy = 6

for i in range(number_of_enemy):
    enemyimg.append(pygame.image.load('alien.png'))
    enemyX.append(random.randint(0, 600))
    enemyY.append(random.randint(0, 150))
    enemyX_change.append(2)
    enemyY_change.append(20)

#background
background = pygame.image.load('bg.png')

#bullet
bulletimg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 350
bulletX_change = 0
bulletY_change = 5
bullet_state = 'ready'       #ready means u can't see the bullent on the screen


#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10
def show_score(x,y):
    score = font.render('score: '+ str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def player(x,y):
    screen.blit(playerimg, (x, y))

def enenmy(x,y, i):
    screen.blit(enemyimg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletimg, (x+15, y))


def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + math.pow(enemyY-bulletY, 2))
    if distance < 27:
        return True
    else:
        return False

#game loop
running = True
while running:
    #forscreencolors
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerX_change = -2
            if event.key == pygame.K_RIGHT:
                playerX_change = 2
            if event.key == pygame.K_SPACE:
                bulletX = playerX
                fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    if bulletY <= 0:
        bulletY = 350
        bullet_state = 'ready'


    #bullet state
    if bulletY <= 0:
        bulletY = 350
        bullet_state = 'ready'
    if bullet_state is 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change






    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 530:
        playerX = 530

    for i in range(number_of_enemy):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 530:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]

        collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 350
            bullet_state = "ready"
            score_value += 1
            #print(score_value)
            enemyX[i] = random.randint(0, 600)
            enemyY[i] = random.randint(0, 150)
        enenmy(enemyX[i], enemyY[i], i)

    player(playerX, playerY)
    show_score(textX,textY)
    pygame.display.update()







