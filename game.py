"""A game written in Python using Pygame. It is about a player base which has to defend itself from zombies."""

import pygame
import sys
import utils
from base import Base
from projectile import Projectile

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((utils.SCREEN_WITDH, utils.SCREEN_HEIGHT))
pygame.display.set_caption("Zombie Defense")
clock = pygame.time.Clock()
FPS = 60
dt = clock.tick(60) / 1000
font = pygame.font.SysFont(None, 36)

# Sounds
gunshot_sound = pygame.mixer.Sound("sfx/gunshot.mp3")
gunshot_sound.set_volume(0.2)


base = Base(utils.SCREEN_WITDH / 2 - 25, utils.SCREEN_HEIGHT / 2 - 25, 50, 50)  # Create a base instance

# Loop

running = True
projectiles = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # left click
            mx, my = pygame.mouse.get_pos()
            projectiles.append(Projectile(utils.SCREEN_WITDH / 2, utils.SCREEN_HEIGHT / 2, mx, my))
            gunshot_sound.play()
        

    # Game logic goes here
    for p in projectiles[:]:
        p.update(dt)
        if not p.alive:
            projectiles.remove(p)

    # Drawing code goes here
    screen.fill(utils.BACKGROUND_COLOR)  # Clear screen with black
    base.draw(screen)
    for b in projectiles:
        b.draw(screen)
    text_surface = font.render(f"Base Health: {base.get_health()}", True, (255, 255, 255), (10, 10, 20))
    screen.blit(text_surface, (10, 10))
    pygame.display.flip() # Update the display
    clock.tick(FPS)

sys.exit()
pygame.quit()