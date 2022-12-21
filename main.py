# PROJET PYTHON MR ARTZ
# SASTRE Hugo, SCHELL Baptiste, SERRANO Jeremy, AYAD Nadjib
# Mini jeu en python
# Utilisation du frameworks Pygame
# Nom du jeu : PyShooter

#-------- IMPORT ---------#
import pygame
import math
from game import Game
from player import Player

# Initialisation du de pygame
pygame.init()

# Définition d'une clock qui permettra de gérer la frequence d'images par seconde
clock = pygame.time.Clock()
FPS = 120

# Génération de la fenetre du jeu
pygame.display.set_caption("PyShooter")
screen = pygame.display.set_mode((1080, 720))

# Importation et chargement de l'arriere plan du jeu
background = pygame.image.load('assets/bg.jpg')

# Importation et chargement de la banniére du jeu
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 3.5)

# Importation et chargement du bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.2)
play_button_rect.y = math.ceil(screen.get_height() / 2.8)

# Chargement du jeu
game = Game()

# Chargement du joueur
player = Player(game)

# Variable de maintien du jeu
running = True

# Boucle du jeu
while running:

    # Fixer le nombre de FPS sur la clock
    clock.tick(FPS)

    # Appliquer la fenetre du jeu a l'écran
    screen.blit(background, (0, -350))

    # Vérifier si notre partie a commencé ou non
    if game.is_playing:
        # Déclenchement des instructions de la partie
        game.update(screen)
    # Vérifier si notre partie n'a pas commencé
    else:
        # Ajout d'un écran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # Mise a jour de l'écran
    pygame.display.flip()

    for event in pygame.event.get():
        # Evenement de fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # Detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # Detetecter si la touche espace est enclenchée pour lancer un projectile
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                else:
                    # Mettre le jeu en mode lancer ( lancer la partie )
                    game.start()
                    # jouer le son de début de partie
                    game.sound_manager.play('musique')

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Vérification pour savoir si la souris est en collision avec le boutton 'Play'
            if play_button_rect.collidepoint(event.pos):
                # Mettre le jeu en mode lancer ( lancer la partie )
                game.start()
                # jouer le son de début de partie
                game.sound_manager.play('musique')


