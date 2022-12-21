import pygame
from player import Player
from monster import Monster, BallonZombie, GrosZombie
from missile_event import MissileFallEvent
from sounds import SoundManager


# Class qui va représenter notre jeu
class Game:
    def __init__(self):
        # définir si notre jeu a commencé ou non
        self.is_playing = False
        # generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # générer l'evenement
        self.missile_event = MissileFallEvent(self)
        # groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        # mettre le score a 0
        self.font = pygame.font.Font('assets/my_custom_font.ttf', 25)
        self.score = 0
        # stockage historique des touches
        self.pressed = {}
        # gerer le son
        self.sound_manager = SoundManager()

    def start(self):
        self.is_playing = True
        self.spawn_monster(BallonZombie)
        self.spawn_monster(BallonZombie)
        self.spawn_monster(GrosZombie)

    def add_score(self, points=1):
        self.score += points
    def game_over(self):
        # remettre le jeu à neuf, retirer monstre, remettre joueur en vie, jeu en attente
        self.all_monsters = pygame.sprite.Group()
        self.missile_event.all_missiles = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.missile_event.reset_percent()
        self.is_playing = False
        self.score = 0
        # jouer le son de fin de partie
        self.sound_manager.play('game_over')
    def update(self, screen):

        # afficher le score sur l'écran
        score_text = self.font.render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))

        # appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # actualiser la barre d'événement du jeu
        self.missile_event.update_bar(screen)

        # recupérer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # récupérer les monstres de notre jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        #récupérer les missiles de notre jeu
        for missile in self.missile_event.all_missiles:
            missile.fall()

        # appliquer l'ensemble des images de mon groupe de projectiles
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des images de mon groupe de monstre
        self.all_monsters.draw(screen)

        # appliquer l'ensemble des images de mon groupe de missile
        self.missile_event.all_missiles.draw(screen)

        # verifier si le joueur souhaite aller à gauche ou à droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))

