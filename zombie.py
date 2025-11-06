"""A class to represent the zombies"""

import pygame
import random
import utils

class Zombie:
    def __init__(self, speed, health):
        self.x, self.y = self.generate_random_spawn_position()
        self.speed = speed
        self.health = health

    def generate_random_spawn_position(self):
        """Generate spawn coordinates along the edges of the screen."""
        random_case = random.randint(1, 4)
        
        if random_case == 1:  # Spawn along the top edge
            x = random.uniform(0, utils.SCREEN_WITDH)
            y = -50
        elif random_case == 2:  # Spawn along the bottom edge
            x = random.uniform(0, utils.SCREEN_WITDH)
            y = utils.SCREEN_HEIGHT + 50
        elif random_case == 3:  # Spawn along the left edge
            x = -50
            y = random.uniform(0, utils.SCREEN_HEIGHT)
        else:  # Spawn along the right edge
            x = utils.SCREEN_WITDH + 50
            y = random.uniform(0, utils.SCREEN_HEIGHT)

        return x, y

    # CoPilot generated this code
    def move_towards_base(self, base_x, base_y, dt):
        """Move the zombie towards the base."""
        direction_x = base_x - self.x
        direction_y = base_y - self.y
        length = (direction_x ** 2 + direction_y ** 2) ** 0.5
        if length != 0:
            direction_x /= length
            direction_y /= length
        self.x += direction_x * self.speed * dt
        self.y += direction_y * self.speed * dt

    def draw(self, surface):
        """Draw the zombie on the given surface."""
        pygame.draw.circle(surface, utils.ZOMBIE_COLOR, (int(self.x), int(self.y)), 10)