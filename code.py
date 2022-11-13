import random
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode([600, 600])

clock = pygame.time.Clock()
snake = [[120, 160], [120, 180], [120, 200]]
direction = [20, 0]
case_vide = [0, 0]
longueur = 3
score = 0
fruit = False  ## False = fruit non mangé
xf, yf = random.randint(0, 30) * 20, random.randint(0, 30) * 20


for i in range(30):
    for j in range(30):
        x = 20 * i
        y = 20 * j
        width = 20
        height = 20
        rect = [x, y, width, height]
        if (i + j) % 2 == 0:
            red = 255
            green = 255
            blue = 255
        elif (i + j) % 2 == 1:
            red = 0
            green = 0
            blue = 0
        color = [red, green, blue]
        pygame.draw.rect(screen, color, rect)


def fruiit(snake, xf, yf):
    if snake[0][0] == xf and snake[0][1] == yf:
        xf, yf = nouveau_fruit(snake)
        # score = score + 1
    width = 20
    height = 20
    red = 255
    green = 255
    blue = 0
    color = [red, green, blue]
    rect = [xf, yf, width, height]
    pygame.draw.rect(screen, color, rect)


def nouveau_fruit(snake):
    xf, yf = random.randint(0, 30) * 20, random.randint(0, 30) * 20
    if [xf, yf] in snake:
        xf, yf = nouveau_fruit(snake)
    return (xf, yf)


def deplacement(snake, direction):
    case_vide = snake[-1]
    snake.insert(0, [snake[0][0] + direction[0], snake[0][1] + direction[1]])
    snake.pop()
    print(snake)
    print(case_vide)
    print(direction)
    return snake


def case_v(case_vide):
    if ((case_vide[0] + case_vide[1]) / 20) % 2 == 0:
        print("ok")
        color1 = [200, 200, 200]
        rect1 = [case_vide[0], case_vide[1], 20, 20]
        pygame.draw.rect(screen, color1, rect1)
    else:
        pygame.draw.rect(screen, [0, 10, 100], [case_vide[1], case_vide[0], 20, 20])


while True:

    print("ok")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP and direction != [0, 20]:
                # print("↑")
                direction[1], direction[0] = -20, 0
            if event.key == pygame.K_DOWN and direction != [0, -20]:
                # print("↓")
                direction[1], direction[0] = 20, 0
            if event.key == pygame.K_LEFT and direction != [20, 0]:
                # print("←")
                direction[1], direction[0] = 0, -20
            if event.key == pygame.K_RIGHT and direction != [-20, 0]:
                # print("→")
                direction[1], direction[0] = 0, 20

    ## je fais bouger le serpent

    snake = deplacement(snake, direction)
    ## je dessine le serpent

    for i in range(longueur):
        x = snake[i][0]
        y = snake[i][1]
        width = 20
        height = 20
        red = 255
        green = 0
        blue = 0
        color = [red, green, blue]
        rect = [x, y, width, height]
        pygame.draw.rect(screen, color, rect)

    ## affichage case damier vide

    case_v(case_vide)

    fruiit(snake, xf, yf)  ## dessine le fruit, quelquesoit le cas d'avant

    # print(score)

    pygame.display.update()

    clock.tick(4)
