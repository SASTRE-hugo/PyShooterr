import pygame

class SoundManager:
    def __init__(self):
        self.sounds = {
            'musique': pygame.mixer.Sound("assets/sounds/batou_song.mp3"),
            'game_over': pygame.mixer.Sound("assets/sounds/clairon_mort.mp3"),
            'missile': pygame.mixer.Sound("assets/sounds/missile.mp3"),
            'grenade': pygame.mixer.Sound("assets/sounds/grenade.mp3"),
        }

    def play(self, name):
        self.sounds[name].play()
