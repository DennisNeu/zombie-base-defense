"""A class to handle the sound effects in the game."""

import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {
            "gunshot": pygame.mixer.Sound("sfx/gunshot.mp3"),
            "impact": pygame.mixer.Sound("sfx/impact.mp3"),
            # Add sound for base hit
        }
        self.sounds["gunshot"].set_volume(0.2)

    def play_sound(self, sound_name):
        if sound_name in self.sounds:
            self.sounds[sound_name].play()