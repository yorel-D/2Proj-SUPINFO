import pygame
from settings import *
from sprites import *
from player import Player
from ai import AI


class Level:
    def __init__(self):
        self.mode = None
        self.game = game
        self.display_surface = pygame.display.get_surface()
        self.background = BACKGROUND
        self.background_rect = self.background.get_rect()
        self.all_sprites = pygame.sprite.Group()
        self.player_sprites = pygame.sprite.Group()
        self.ai_sprites = pygame.sprite.Group()
        self.player = Player(self)
        self.player_sprites.add(self.player)
        self.ai = AI(self)
        self.ai_sprites.add(self.ai)
        self.all_sprites.add(self.player, self.ai)
        self.action_bar = ActionBar(self, "pirates")


    def run(self, dt, mode):
        self.mode = mode
        self.ai.set_mode(mode)
        m_pos = pygame.mouse.get_pos()
        self.display_surface.blit(self.background, self.background_rect)
        self.ai.update(dt)
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)
        if self.player.health <= 0:
            self.game.game_over = True
        if self.ai.health <= 0:
            self.game.game_won = True
