"""A Class to represent the Player Base in the Zombie Defense game."""

import pygame
import utils
from projectile import Projectile

class Base:
    """Class to represent the Player Base."""

    def __init__(self, x, y, width, height):
        """Initialize the Base with position and size."""
        self.rect = pygame.Rect(x, y, width, height)
        self.health = utils.base_health

    def draw(self, screen):
        """Draw the Base on the given screen."""
        pygame.draw.rect(screen, utils.BASE_COLOR, self.rect)

    def take_damage(self, amount):
        """Reduce the Base's health by the given amount."""
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def get_health(self):
        """Return the current health of the Base."""
        return self.health