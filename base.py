"""A Class to represent the Player Base in the Zombie Defense game."""

import pygame
import utils

class Base:
    """Class to represent the Player Base."""

    def __init__(self, x, y, width, height):
        """Initialize the Base with position and size."""
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        """Draw the Base on the given screen."""
        pygame.draw.rect(screen, utils.BASE_COLOR, self.rect)