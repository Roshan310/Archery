import pygame
import random
import time
from archer import Target

pygame.init()

WIDTH, HEIGHT = 800, 600

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("ARCHERY GAME!!! ")

TARGET_LOC = 30
TARGET_EVENT = pygame.USEREVENT

# def draw(window, targets):
#     window.fill('blue')

#     for target in targets:
#         target.draw(window)

#     pygame.display.update()

def main():
    running = True

    targets = []

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        x = random.randint(TARGET_LOC, WIDTH-TARGET_LOC)
        y = random.randint(TARGET_LOC, HEIGHT-TARGET_LOC)
        target = Target(x, y)
        targets.append(target)

        for target in targets:
            target.update()
            target.draw(WINDOW)
    
        pygame.display.update()

        

main()
