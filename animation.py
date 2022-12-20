import pygame

# définir une classe qui va s'occuper des animations
class AnimationSprite(pygame.sprite.Sprite):

    # définir les choses à faire à la création de l'entité
    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)