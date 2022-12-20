import pygame
import random
import animation

# créer une classe qui va gérer la notion de monstre sur le jeu
class Monster(animation.AnimationSprite):
    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.offset = offset
        self.health = 50
        self.max_health = 50
        self.attack = 0.1
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 400 - offset
        self.loot_amount = 1

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, 2)

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def damage(self, amount):
        # Infliger les degats
        self.health -= amount

        # vérifier si son nouveau nombre de point de vue est inférieur ou égal à 0
        if self.health <= 0:
            # Reapparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, self.default_speed)
            self.health = self.max_health
            # ajouter le nombre de points
            self.game.add_score(self.loot_amount)

            # vérifier si la barre d'événement est chargé a son maximum
            if self.game.missile_event.is_full_loaded():
                # retirer du jeu
                self.game.all_monsters.remove(self)

                # appel de la méthode pour essayer de déclencher la pluie de missile
                self.game.missile_event.attempt_fall()

    def update_health_bar(self, surface):
        # dessiner notre barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + self.offset, self.rect.y - 30, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + self.offset, self.rect.y - 30, self.health, 5])

    def forward(self):
        # le déplacement ne ce fait que si il n'y a pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en colission avec le joueur
        else:
            # Infliger des dégats ( au joueur )
            self.game.player.damage(self.attack)

# définir une classe pour le ballon zombie
class BallonZombie(Monster):
    def __init__(self, game):
        super().__init__(game, "zombie_ballon", (150, 249))
        self.set_speed(3)
        self.set_loot_amount(1)

# définir une classe pour le gros zombie
class GrosZombie(Monster):
    def __init__(self, game):
        super().__init__(game, "zombie_gros", (400, 373), 70)
        self.health = 250
        self.max_health = 250
        self.attack = 0.8
        self.velocity = 0.02
        self.set_speed(1)
        self.set_loot_amount(5)




