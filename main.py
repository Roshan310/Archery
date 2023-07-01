import pygame
import random
import time
from archer import Target

pygame.init()

pygame.display.set_caption("ARCHERY GAME!!! ")

WIDTH, HEIGHT = 800, 600

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
TOP_BAR_HEIGHT = 50
TARGET_LOC = 30
TARGET_EVENT = pygame.USEREVENT
TARGET_INCREMENT = 400

clock = pygame.time.Clock()

LABEL_FONT = pygame.font.SysFont('monospace', 20)

def draw(window, targets):
    window.fill('blue')

    for target in targets:
        target.draw(window)


def draw_top_bar(window, hits):
    pygame.draw.rect(window, 'grey', (0, 0, WIDTH, TOP_BAR_HEIGHT))
    hits = LABEL_FONT.render(f"Hits: {hits}", 1, "black")

    window.blit(hits, (10, 5))

def main():
    running = True

    click = False
    total_clicks = 0
    target_pressed = 0
    misses = 0


    targets = []
    pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)

    while running:

        mouse_position = pygame.mouse.get_pos()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            if event.type == TARGET_EVENT:
                x = random.randint(TARGET_LOC, WIDTH-TARGET_LOC)
                y = random.randint(TARGET_LOC + TOP_BAR_HEIGHT, HEIGHT-TARGET_LOC)
                target = Target(x, y)
                targets.append(target)

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                total_clicks += 1
        

        for target in targets:
            target.update()

            if target.size <= 0:
                targets.remove(target)
                misses += 1
            
            if click and target.collide(*mouse_position):
                targets.remove(target)
                collide_sound = pygame.mixer.Sound('ding.mp3')
                pygame.mixer.Sound.play(collide_sound)
                target_pressed += 1
                click = False

        draw(WINDOW, targets)
        draw_top_bar(WINDOW, target_pressed)
        pygame.display.update()

main()
