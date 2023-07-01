import pygame

# pygame.init()

# WIDTH, HEIGHT = 800, 600

# WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# pygame.display.set_caption("ARCHERY GAME!!! ")

class Target:
    GROWTH_RATE = 0.8
    MAX_SIZE = 30
    COLOR = 'red'
    SECONDARY_COLOR = 'white'

    def __init__(self, x_coord, y_coord) -> None:
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.grow = True
        self.size = 0

    def update(self):
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False
        
        if self.grow:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE
        
    def draw(self, window):
        pygame.draw.circle(window, self.COLOR, (self.x_coord, self.y_coord), self.size)
        pygame.draw.circle(window, self.SECONDARY_COLOR, (self.x_coord, self.y_coord), self.size*0.8)
        pygame.draw.circle(window, self.COLOR, (self.x_coord, self.y_coord), self.size*0.6)
        pygame.draw.circle(window, self.SECONDARY_COLOR, (self.x_coord, self.y_coord), self.size*0.4)
  
