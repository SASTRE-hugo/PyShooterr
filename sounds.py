import pygame

class SoundManager:
    def __init__(self):
        self.sounds = {
            'musique': pygame.mixer.Sound("assets/sounds/clairon.mp3"),
            'game_over': pygame.mixer.Sound("assets/sounds/ROI.mp3"),
            'missile': pygame.mixer.Sound("assets/sounds/missile.mp3"),
            'grenade': pygame.mixer.Sound("assets/sounds/grenade.mp3"),
        }

    def play(self, name):
        self.sounds[name].play()
