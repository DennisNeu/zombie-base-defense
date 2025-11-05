"""A game written in Python using Pygame. It is about a player base which has to defend itself from zombies."""

import pygame
import sys
import utils
from base import Base

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((utils.SCREEN_WITDH, utils.SCREEN_HEIGHT))
pygame.display.set_caption("Zombie Defense")
clock = pygame.time.Clock()
FPS = 60

base = Base(utils.SCREEN_WITDH / 2 - 25, utils.SCREEN_HEIGHT / 2 - 25, 50, 50)  # Create a base instance

# Loop

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic goes here

    # Drawing code goes here
    screen.fill(utils.BACKGROUND_COLOR)  # Clear screen with black
    base.draw(screen)
    pygame.display.flip() # Update the display
    clock.tick(FPS)