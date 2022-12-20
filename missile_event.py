import pygame
from missile import Missile

# créer une classe pour gérer cet evenement

class MissileFallEvent:

    # lors du chargement -> créer un compteur

    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 5
        self.game = game
        self.fall_mode = False
        # définir un groupe de sprite pour stocker nos missiles
        self.all_missiles = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def missile_fall(self):
        # boucle pour les valeurs entre 1 et 10
        for i in range(1,10):
            # faire apparaitre les missiles
            self.all_missiles.add(Missile(self))
    def attempt_fall(self):
        # quand la jauge d'evenement est totalement chargé
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            self.missile_fall()
            self.fall_mode = True # activer l'evenement

    def update_bar(self, surface):

        # ajouter du pourcentage a la barre
        self.add_percent()

        # barre noir (en arriére plan )
        pygame.draw.rect(surface, (0, 0, 0), [
            0, # l'axe des X
            surface.get_height() - 20, # l'axe des Y
            surface.get_width(), # longeur de la fenetre
            10 # épaisseur de la barre
        ])

        # barre rouge (jauge d'event )
        pygame.draw.rect(surface, (187, 11, 11), [
            0, # l'axe des X
            surface.get_height() - 20, # l'axe des Y
            (surface.get_width() / 100) * self.percent, # longeur de la fenetre
            10 # épaisseur de la barre
        ])