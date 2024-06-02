from src.settings import *
import pygame

class CooldownBar(pygame.sprite.Sprite):
    def __init__(self, button, level):
        super().__init__()
        self.level = level
        self.button = button
        self.height = 7 * CELL
        self.width = 0.5 * CELL
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill("green")
        self.rect = self.image.get_rect(bottomleft=(self.button.rect.left - 1 * CELL, self.button.rect.bottomleft[1]))
        self.last_update = 0
        self.level.all_sprites.add(self)

    def update(self, dt):
        if not self.button.active:
            self.height = 70 * ((self.button.now - self.button.lastupdate) / self.button.cooldown)
            if self.height <= 0:
                self.height = 0
        else:
            self.height = 7 * CELL

        self.image = game.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(bottomleft=(self.button.rect.left - 1 * CELL, self.button.rect.bottomleft[1]))
        self.image.fill((0, 255, 0))

