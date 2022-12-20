import pygame
import random
import animation
from monster import BallonZombie, GrosZombie


#créer une classe pour gérer les missiles
class Missile(animation.AnimationSprite):
    def __init__(self, missile_event):
        super().__init__("missile")
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 2)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.missile_event = missile_event

    def remove(self):
        self.missile_event.all_missiles.remove(self)
        # jouer le son
        self.missile_event.game.sound_manager.play('missile')
        #vérifier si le nombre de missile est de 0
        if len(self.missile_event.all_missiles)==0:
            # remettre barre à 0
            self.missile_event.reset_percent()
            # apparaitre les premiers monstres apres la chute des missiles
            self.missile_event.game.start()

    def fall(self):
        self.rect.y += self.velocity

        # ne tombe pas sur le sol
        if self.rect.y >= 500:
            self.remove()
        # si il n'y a plus de missile sur le jeu
        if len(self.missile_event.all_missiles)==0:
            # remettre la jauge au départ
            self.missile_event.reset_percent()
            self.missile_event.fall_mode = False

        # vérifier si missile touche le joueur
        if self.missile_event.game.check_collision(self, self.missile_event.game.all_players):
            print("Player touché !")
            # retirer le missile
            self.remove()
            # subir des dégats
            self.missile_event.game.player.damage(20)


