import random
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode([600, 600])

clock = pygame.time.Clock()
snake = [[120, 160], [120, 180], [120, 200]]
direction = [20, 0]
case_vide = snake[-1]
score = 0
xf, yf = random.randint(0, 29) * 20, random.randint(0, 29) * 20


for i in range(30):
    for j in range(30):
        x = 20 * i
        y = 20 * j
        width = 20
        height = 20
        rect = [x, y, width, height]
        if (i + j) % 2 == 0:
            red = 0
            green = 0
            blue = 0
        elif (i + j) % 2 == 1:
            red = 20
            green = 20
            blue = 20
        color = [red, green, blue]
        pygame.draw.rect(screen, color, rect)


def fruit(snake, xf, yf, score):
    if snake[0][0] == xf and snake[0][1] == yf:
        while [xf, yf] in snake:
            xf, yf = random.randint(0, 29) * 20, random.randint(0, 29) * 20
        print(xf, yf)
        score += 1
        print(score)
        snake.append(snake[-1])
        # score = score + 1
    width = 20
    height = 20
    red = 255
    green = 0
    blue = 0
    color = [red, green, blue]
    rect = [xf, yf, width, height]
    pygame.draw.rect(screen, color, rect)
    return (xf, yf, score)


def deplacement(snake, direction, case_vide):
    case_vide = snake[-1]
    snake.insert(0, [snake[0][0] + direction[0], snake[0][1] + direction[1]])
    snake.pop()

    return snake, case_vide


def case_v(case_vide):

    if (((case_vide[0] + case_vide[1]) / 20) % 2) == 0:

        color1 = [0, 0, 0]
        rect1 = [case_vide[0], case_vide[1], 20, 20]
        pygame.draw.rect(screen, color1, rect1)

    else:
        pygame.draw.rect(screen, [20, 20, 20], [case_vide[0], case_vide[1], 20, 20])

def mort(snake):
    if snake[0] in snake[1:]:
        pygame.quit()
        sys.exit()
    if (snake[0][0]/20)>29 or (snake[0][0]/20)<0 or (snake[0][1]/20)>29 or (snake[0][1]/20)<0 :
        pygame.quit()
        sys.exit()




while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP and direction != [0, 20]:
                # print("???")
                direction[1], direction[0] = -20, 0
            if event.key == pygame.K_DOWN and direction != [0, -20]:
                # print("???")
                direction[1], direction[0] = 20, 0
            if event.key == pygame.K_LEFT and direction != [20, 0]:
                # print("???")
                direction[1], direction[0] = 0, -20
            if event.key == pygame.K_RIGHT and direction != [-20, 0]:
                # print("???")
                direction[1], direction[0] = 0, 20

    ## je fais bouger le serpent

    snake, case_vide = deplacement(snake, direction, case_vide)
    ## je dessine le serpent

    for i in range(len(snake)):
        x = snake[i][0]
        y = snake[i][1]
        width = 20
        height = 20
        red = 0
        green = 230
        blue = 0
        color = [red, green, blue]
        rect = [x, y, width, height]
        pygame.draw.rect(screen, color, rect)

    ## affichage case damier vide

    case_v(case_vide)

    xf, yf, score = fruit(
        snake, xf, yf, score
    ) 

    mort(snake)
        
    pygame.display.update()

    clock.tick(score+8)
