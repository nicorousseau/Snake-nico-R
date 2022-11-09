import random
import sys
import pygame


pygame.init()
screen = pygame.display.set_mode([300, 300])
x = 100
y = 100
width = 30
height = 30
rect = [x, y, width, height]
red = 255
green = 0
blue = 0
color = [red, green, blue]
pygame.draw.rect(screen, color, rect)