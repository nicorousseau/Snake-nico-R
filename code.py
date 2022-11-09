import random
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode([600, 600])
clock = pygame.time.Clock()
snake = [[120, 170], [120, 190], [120, 210]]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP:
                print("↑")
            if event.key == pygame.K_DOWN:
                print("↓")
            if event.key == pygame.K_LEFT:
                print("←")
            if event.key == pygame.K_RIGHT:
                print("→")
    # red = random.randint(0, 255)
    # green = random.randint(0, 255)
    # blue = random.randint(0, 255)
    # color = [red, green, blue]
    # screen.fill(color)
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
    snake = déplacement(snake, direction)
    for i in range(3):
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
    direction = [0, 1]
    pygame.display.update()
    clock.tick(1)


def déplacement(snake, direction):
    snake[0][0], snake[1][0], snake[2][0] = (
        snake[0][0] + direction[0],
        snake[1][0] + direction[0],
        snake[2][0] + direction[0],
    )
    snake[0][1], snake[1][1], snake[2][1] = (
        snake[0][1] + direction[0],
        snake[1][1] + direction[0],
        snake[2][1] + direction[0],
    )
    return snake
