import pygame
from settings import *
from sprites import *


class Player(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        self.image = PLAYER_CASTLE_IMAGE
        self.level = level
        self.xp = 9999
        self.money = 2000000000
        self.money_text = MoneyText(str(int(self.money)), self.level)
        self.xp_text = ExpText (str(int(self.xp)), self.level)
        self.rect = self.image.get_rect(midleft=(-8 * CELL, SCREEN_HEIGHT / 2))
        self.max_health = 5000
        self.health = 2000
        self.health_text = HealthText(str(int(self.health)), str(self.max_health), self.level, 2 * CELL, 58 * CELL)
        self.defense = 100
        self.last_money = 0

    def update(self, dt):
        now = game.time.get_ticks()
        if now - self.last_money > 6000:
            self.last_money = now
            self.money += 30
        self.xp_text.kill()
        self.xp_text = ExpText(str(int(self.xp)), self.level)
        self.money_text.kill()
        self.money_text = MoneyText(str(int(self.money)), self.level)
        self.health_text.kill()
        self.health_text = HealthText(str(int(self.health)), str(self.max_health), self.level, 2 * CELL, 58 * CELL)


