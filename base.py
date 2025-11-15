"""A Class to represent the Player Base in the Zombie Defense game."""

import pygame
import utils
from projectile import Projectile

class Base:
    """Class to represent the Player Base."""

    def __init__(self, x, y, width, height, health=100, max_health=100, bullet_damage=10):
        """Initialize the Base with position and size."""
        self.rect = pygame.Rect(x, y, width, height)
        self.max_health = max_health
        self.bullet_damage = bullet_damage
        self._health = health


        # This is a Python Property
        # Its not pythonic to use getters and setters, fields are public
        # Turn them into properties as soon as you need logic (e. g. clamping)
        # This does not break dot notation (e. g. base.health = 100 still works)
    @property
    def health(self):
        return self._health
        
    @health.setter
    def health(self, value):
        self._health = max(0, min(self.max_health, value))

    def draw(self, screen):
        """Draw the Base on the given screen."""
        pygame.draw.rect(screen, utils.BASE_COLOR, self.rect)
