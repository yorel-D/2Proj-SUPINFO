import random
import pygame
from src.settings import *
from src.sprites import *


class AI(pygame.sprite.Sprite):
    def __init__(self, level, state):
        super().__init__()
        self.level = level
        self.state = state
        self.mode = None
        self.start_time = pygame.time.get_ticks()
        self.last_update = 0
        self.health = 5000
        self.max_health = 5000
        self.defense = 100

        self.easy_list = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3]
        self.normal_list = [1, 1, 1, 2, 2, 2, 3, 3, 3, random.randint(1, 4)]
        self.hard_list = [1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
        self.impossible_list = [1, 2, 2, 2, 2, 3, 3, 3, 3, 3]

        self.update_image()
        self.rect = self.image.get_rect(midright=(136 * CELL, SCREEN_HEIGHT / 2))
        self.health_text = HealthText(str(int(self.health)), str(self.max_health), self.level, 120 * CELL, 58 * CELL)
        self.enemy_sprites = pygame.sprite.Group()

    def set_mode(self, mode):
        self.mode = mode

    def update_image(self):
        state_image_map = {
            "satyrs": PLAYER_CASTLE_IMAGE,
            "golems": PLAYER_CASTLE_IMAGE1,
            "elfs": PLAYER_CASTLE_IMAGE2,
            "angel": PLAYER_CASTLE_IMAGE3,
            "wraith": PLAYER_CASTLE_IMAGE4,
            "villager": PLAYER_CASTLE_IMAGE5,
        }
        self.image = state_image_map.get(self.state, PLAYER_CASTLE_IMAGE)
        self.image = pygame.transform.flip(self.image, True, False)

    def spawn_enemy(self, num):
        state_enemy_map = {
            "satyrs": (EnemyLightPirate, EnemyRangedPirate, EnemyHeavyPirate, EnemyHeroPirate),
            "golems": (EnemyLightWarrior, EnemyRangedWarrior, EnemyHeavyWarrior, EnemyHeroWarrior),
            "elfs": (EnemyLightFairy, EnemyRangedFairy, EnemyHeavyFairy, EnemyHeroFairy),
            "angel": (EnemyLightAngel, EnemyRangedAngel, EnemyHeavyAngel, EnemyHeroAngel),
            "wraith": (EnemyLightWraith, EnemyRangedWraith, EnemyHeavyWraith, EnemyHeroWraith),
            "villager": (EnemyLightVillager, EnemyRangedVillager, EnemyHeavyVillager, EnemyHeroVillager),
        }
        enemy_classes = state_enemy_map.get(self.state, state_enemy_map["satyrs"])
        return enemy_classes[num - 1](self.level)

    def update(self, dt):
        self.update_image()
        self.health_text.kill()
        self.health_text = HealthText(str(int(self.health)), str(self.max_health), self.level, 95 * CELL, 58 * CELL)
        now = pygame.time.get_ticks()

        mode_spawn_delay_map = {
            "easy": 6500,
            "normal": 5000,
            "hard": 4000,
            "impossible": 3000,
        }
        delay = mode_spawn_delay_map.get(self.mode, 6500)

        mode_list_map = {
            "easy": self.easy_list,
            "normal": self.normal_list,
            "hard": self.hard_list,
            "impossible": self.impossible_list,
        }
        spawn_list = mode_list_map.get(self.mode, self.easy_list)

        if now - self.last_update > delay or self.last_update == 0:
            self.last_update = now
            num = random.choice(spawn_list)
            unit = self.spawn_enemy(num)

        state_timing = [
            (60 * 1000 * 2, "golems"),
            (60 * 1000 * 4, "elfs"),
            (60 * 1000 * 6, "angel"),
            (60 * 1000 * 8, "wraith"),
            (60 * 1000 * 10, "villager"),
        ]
        elapsed_time = now - self.start_time
        for time, new_state in state_timing:
            if elapsed_time >= time:
                self.state = new_state
