"""A class to represent a projectile fired from the Base in the Zombie Defense game."""

import pygame
import utils

class Projectile:
    """Class to represent a projectile fired from the Base."""

    def __init__(self, x, y, width=5, height=10, speed=7):
        """Initialize the Projectile with position, size, and speed."""
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

    def move(self):
        """Move the projectile upwards."""
        self.rect.y -= self.speed

    def draw(self, screen):
        """Draw the Projectile on the given screen."""
        pygame.draw.rect(screen, utils.PROJECTILE_COLOR, self.rect)

    def off_screen(self):
        """Check if the projectile is off the screen."""
        return self.rect.y < 0