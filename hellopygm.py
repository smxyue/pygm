import pygame
from pygame.locals import  *
from sys import exit

bak_img = 'univers.jpg'
cur_img = 'ship.jpg'

pygame.init()
screen = pygame.display.set_mode((700,525),0,32)
pygame.display.set_caption('hello pygame!')

bak = pygame.image.load(bak_img).convert()
cur = pygame.image.load(cur_img).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.blit(bak, (0, 0))
    x, y = pygame.mouse.get_pos();
    x -= cur.get_width()/2
    y -= cur.get_height() /2
    screen.blit(cur, (x, y))
    pygame.display.update()