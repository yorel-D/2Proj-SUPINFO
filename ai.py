import random
import pygame
from settings import *
from sprites import *


class AI(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        self.level = level
        self.mode = None
        self.image = ENEMY_CASTLE_IMAGE
        self.rect = self.image.get_rect(midright=(136 * CELL, SCREEN_HEIGHT / 2))
        self.enemy_sprites = pygame.sprite.Group()
        self.health = 5000
        self.max_health = 5000
        self.health_text = HealthText(str(int(self.health)), str(self.max_health), self.level, 120*CELL, 58 * CELL)
        self.defense = 100
        self.state = "pirates"
        self.start_time = game.time.get_ticks()
        self.last_update = 0
        self.easy_list = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3]
        self.normal_list = [1, 1, 1, 2, 2, 2, 3, 3, 3, random.randint(1, 4)]
        self.hard_list = [1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
        print(self.mode)

    def set_mode(self, mode):
        self.mode = mode

    def update(self, dt):
        self.health_text.kill()
        self.health_text = HealthText(str(int(self.health)), str(self.max_health), self.level, 95*CELL, 58 * CELL)
        now = pygame.time.get_ticks()
        if self.mode == "easy":
            if self.state == "pirates":
                if now - self.last_update > 6500 or self.last_update == 0:
                    print("easy spawn")
                    self.last_update = now
                    num = random.choice(self.easy_list)
                    if num == 1:
                        unit = EnemyLightPirate(self.level)
                    if num == 2:
                        unit = EnemyRangedPirate(self.level)
                    if num == 3:
                        unit = EnemyHeavyPirate(self.level)
            if self.state == "warriors":
                if now - self.last_update > 6500 or self.last_update == 0:
                    self.last_update = now
                    num = random.choice(self.easy_list)
                    if num == 1:
                        unit = EnemyLightWarrior(self.level)
                    if num == 2:
                        unit = EnemyRangedWarrior(self.level)
                    if num == 3:
                        unit = EnemyHeavyWarrior(self.level)

            if self.state == "elfs":
                if now - self.last_update > 6500 or self.last_update == 0:
                    self.last_update = now
                    num = random.choice(self.easy_list)
                    if num == 1:
                        unit = EnemyLightElf(self.level)
                    if num == 2:
                        unit = EnemyRangedElf(self.level)
                    if num == 3:
                        unit = EnemyHeavyElf(self.level)
            if 60 * 1000 * 8 < now - self.start_time < 60 * 1000 * 16:
                self.state = "warriors"
            elif now - self.start_time > 60 * 100 * 16:
                self.state = "elfs"
        if self.mode == "normal":
            if self.state == "pirates":
                if now - self.last_update > 5000 or self.last_update == 0:
                    print("normal spawn")
                    self.last_update = now
                    num = random.choice(self.normal_list)
                    if num == 1:
                        unit = EnemyLightPirate(self.level)
                    if num == 2:
                        unit = EnemyRangedPirate(self.level)
                    if num == 3:
                        unit = EnemyHeavyPirate(self.level)
            if self.state == "warriors":
                if now - self.last_update > 5000 or self.last_update == 0 :
                    self.last_update = now
                    num = random.choice(self.normal_list)
                    if num == 1:
                        unit = EnemyLightWarrior(self.level)
                    if num == 2:
                        unit = EnemyRangedWarrior(self.level)
                    if num == 3:
                        unit = EnemyHeavyWarrior(self.level)
            if self.state == "elfs":
                if now - self.last_update > 5000 or self.last_update == 0:
                    self.last_update = now
                    num = random.choice(self.normal_list)
                    if num == 1:
                        unit = EnemyLightElf(self.level)
                    if num == 2:
                        unit = EnemyRangedElf(self.level)
                    if num == 3:
                        unit = EnemyHeavyElf(self.level)
            if 60 * 1000 * 6 < now - self.start_time < 60 * 1000 * 12:
                self.state = "warriors"
            elif now - self.start_time > 60 * 100 * 12:
                self.state = "elfs"
        if self.mode == "hard":
            if self.state == "pirates":
                if now - self.last_update > 4000 or self.last_update == 0:
                    print("hard spawn")
                    self.last_update = now
                    num = random.choice(self.hard_list)
                    if num == 1:
                        unit = EnemyLightPirate(self.level)
                    if num == 2:
                        unit = EnemyRangedPirate(self.level)
                    if num == 3:
                        unit = EnemyHeavyPirate(self.level)
            if self.state == "warriors":
                if now - self.last_update > 4000 or self.last_update == 0:
                    self.last_update = now
                    num = random.choice(self.hard_list)
                    if num == 1:
                        unit = EnemyLightWarrior(self.level)
                    if num == 2:
                        unit = EnemyRangedWarrior(self.level)
                    if num == 3:
                        unit = EnemyHeavyWarrior(self.level)
            if self.state == "elfs":
                if now - self.last_update > 4000 or self.last_update == 0:
                    self.last_update = now
                    num = random.choice(self.hard_list)
                    if num == 1:
                        unit = EnemyLightElf(self.level)
                    if num == 2:
                        unit = EnemyRangedElf(self.level)
                    if num == 3:
                        unit = EnemyHeavyElf(self.level)
            if 60 * 1000 * 4 < now - self.start_time < 60 * 1000 * 8:
                self.state = "warriors"
            elif now - self.start_time > 60 * 100 * 8:
                self.state = "elfs"

