import pygame
import random
import time
from archer import Target

pygame.init()

pygame.display.set_caption("ARCHERY GAME!!! ")

WIDTH, HEIGHT = 800, 600

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

TARGET_LOC = 30
TARGET_EVENT = pygame.USEREVENT
TARGET_INCREMENT = 900

def draw(window, targets):
    window.fill('blue')

    for target in targets:
        target.draw(window)

    pygame.display.update()

def main():
    running = True

    targets = []
    pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            if event.type == TARGET_EVENT:
                x = random.randint(TARGET_LOC, WIDTH-TARGET_LOC)
                y = random.randint(TARGET_LOC, HEIGHT-TARGET_LOC)
                target = Target(x, y)
                targets.append(target)

        for target in targets:
            target.update()

        draw(WINDOW, targets)

        

main()
