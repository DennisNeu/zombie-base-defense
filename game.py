"""A game written in Python using Pygame. It is about a player base which has to defend itself from zombies."""

import pygame
import sys
import random
import utils
from base import Base
from projectile import Projectile
from sound_manager import SoundManager
from zombie import Zombie

def check_collisions():
    # AI cooked hard
    for z in zombies[:]:
        z.move_towards_base(utils.SCREEN_WITDH / 2, utils.SCREEN_HEIGHT / 2, dt)
        # Check collision with base
        base_rect = base.rect
        zombie_rect = pygame.Rect(z.x - z.radius, z.y - z.radius, z.radius * 2, z.radius * 2)
        if base_rect.colliderect(zombie_rect):
            base.take_damage(10)
            zombies.remove(z)
            sound_manager.play_sound("base_hit")
            continue
        # Check collision with projectiles
        for p in projectiles:
            projectile_rect = pygame.Rect(p.x - p.radius, p.y - p.radius, p.radius * 2, p.radius * 2)
            if zombie_rect.colliderect(projectile_rect):
                z.health -= 10
                p.alive = False
                sound_manager.play_sound("impact")
                if z.health <= 0:
                    zombies.remove(z)
                    utils.kill_count += 1
                break

def spawn_zombie():
    """Spawn a zombie with a random chance."""
    if random.randint(0,60) == 60:  # 2% chance to spawn a zombie each frame
        zombies.append(Zombie(speed=50, health=30))

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((utils.SCREEN_WITDH, utils.SCREEN_HEIGHT))
pygame.display.set_caption("Zombie Defense")
clock = pygame.time.Clock()
FPS = 60
dt = clock.tick(60) / 1000
font = pygame.font.SysFont(None, 36)
sound_manager = SoundManager()


base = Base(utils.SCREEN_WITDH / 2 - 25, utils.SCREEN_HEIGHT / 2 - 25, 50, 50)  # Create a base instance

# Loop
running = True
projectiles = []
zombies = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # left click
            mx, my = pygame.mouse.get_pos()
            projectiles.append(Projectile(utils.SCREEN_WITDH / 2, utils.SCREEN_HEIGHT / 2, mx, my))
            sound_manager.play_sound("gunshot")

    # Game logic goes here
    for p in projectiles[:]:
        p.update(dt)
        if not p.alive:
            projectiles.remove(p)
    
    spawn_zombie()
    
    check_collisions()

    # Drawing code goes here
    screen.fill(utils.BACKGROUND_COLOR)  # Clear screen with black
    base.draw(screen)
    for b in projectiles:
        b.draw(screen)
    for z in zombies:
        z.draw(screen)
    
    # TODO: Refactor text logic
    base_health_text = font.render(f"Base Health: {base.get_health()}", True, (255, 255, 255), (10, 10, 20))
    kill_count_text = font.render(f"Kill Count: {utils.kill_count}", True, (255, 255, 255), (10, 50, 20))
    screen.blit(kill_count_text, (10, 50))
    screen.blit(base_health_text, (10, 10))
    pygame.display.flip() # Update the display
    clock.tick(FPS)

sys.exit()
pygame.quit()