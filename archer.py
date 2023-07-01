import pygame
import math

class Target:
    GROWTH_RATE = 0.8
    MAX_SIZE = 50
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
  

    def collide(self, x, y):
        distance = math.sqrt((self.x_coord-x)**2 + (self.y_coord-y)**2)
        # print(f'Distace: {distance}, Size: {self.size}')
        return distance <= self.size