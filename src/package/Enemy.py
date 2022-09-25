import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, scalex, scaley, x):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = 320
        self.hyena_sprites = [pygame.transform.scale(pygame.image.load(f"environment/enemy/enemy ({i}).png").convert_alpha(), (scalex, scaley)) for i in range(1, 7)]
        self.current_hyena_sprite = 0
        self.image = self.hyena_sprites[int(self.current_hyena_sprite)]
        self.mask = pygame.mask.from_surface(self.image)
        self.game_speed = 7
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self):
        self.rect.x -= self.game_speed
        self.mask = pygame.mask.from_surface(self.image)
        if self.rect.x < -50:
            self.kill()
        self.animate_hyena()
    
    def animate_hyena(self):
        self.current_hyena_sprite += 0.25
        if self.current_hyena_sprite >= len(self.hyena_sprites):
            self.current_hyena_sprite = 0
        self.image = self.hyena_sprites[int(self.current_hyena_sprite)]


class Vulture(pygame.sprite.Sprite):
    def __init__(self, width, scalex, scaley):
        pygame.sprite.Sprite.__init__(self)
        self.x = width+60
        self.y = random.randrange(301, 345)
        self.vulcture_sprites = [pygame.transform.scale(pygame.image.load(f"environment/vulture/vulture ({i}).png").convert_alpha(), (scalex, scaley)) for i in range(1, 5)]
        self.current_vulcture_sprite = 0
        self.game_speed = 8
        self.image = self.vulcture_sprites[(int(self.current_vulcture_sprite))]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        
    def update(self):
        self.rect.x -=  self.game_speed
        self.mask = pygame.mask.from_surface(self.image)
        if self.rect.x < -30:
            self.kill()
        # pygame.draw.rect(self.SCREEN, (0, 0, 0), self.rect, 2)
        self.animate_vulcture()

    def animate_vulcture(self):
        self.current_vulcture_sprite += 0.25
        if self.current_vulcture_sprite >= len(self.vulcture_sprites):
            self.current_vulcture_sprite = 0
        self.image = self.vulcture_sprites[int(self.current_vulcture_sprite)]
