"""A class to represent a projectile fired from the Base in the Zombie Defense game."""

import pygame
import utils
from math import hypot

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, target_x, target_y, speed=500):
        super().__init__()
        dx = target_x - x
        dy = target_y - y
        length = hypot(dx, dy)
        if length == 0:
            length = 1
        self.vx = dx / length * speed
        self.vy = dy / length * speed
        self.x = x
        self.y = y
        self.radius = 4
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

        
        self.alive = True

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        # remove bullet if it goes off screen
        if not (0 <= self.x <= utils.SCREEN_WIDTH and 0 <= self.y <= utils.SCREEN_HEIGHT):
            self.alive = False

    def draw(self, surface):
        pygame.draw.circle(surface, utils.PROJECTILE_COLOR, (int(self.x), int(self.y)), self.radius)