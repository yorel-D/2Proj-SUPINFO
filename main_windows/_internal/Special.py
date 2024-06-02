from src.settings import *
from random import randrange
import pygame
from random import randrange

class HealthSpecial(pygame.sprite.Sprite):
    def __init__(self, parent, bar_type, x, y):
        super().__init__()
        self.parent = parent
        self.bar_type = bar_type
        self.image = pygame.Surface((50, 10))
        self.rect = self.image.get_rect(topleft=(x, y))

class special(pygame.sprite.Sprite):
    def __init__(self, level, walking_frames, attacking_frames, damage, movementspeed):
        super().__init__()
        self.level = level
        self.walking_frames = walking_frames
        self.attacking_frames = attacking_frames
        self.idle_frames = walking_frames
        self.current_frames = walking_frames
        self.current = 0
        self.damage = damage
        self.image = self.walking_frames[self.current]
        self.rect = self.image.get_rect(midtop=(randrange(0, SCREEN_WIDTH - self.image.get_width()), randrange(-CELL * 30, CELL * 15)))
        self.starting_point = self.rect.centery
        self.walking = True
        self.attacking = False
        self.idle = False
        self.movement_speed = movementspeed
        self.orig_movement_speed = self.movement_speed
        self.lastupdate = 0
        self.health = 100
        self.back_health_bar = HealthSpecial(self, "back", self.rect.centerx, self.rect.top)
        self.front_health_bar = HealthSpecial(self, "front", self.rect.centerx, self.rect.top)
        self.level.all_sprites.add(self)
        self.level.player_sprites.add(self)

    def check_collision(self):
        self.enemy_collisions = pygame.sprite.spritecollide(self, self.level.ai_sprites, False)
        if self.enemy_collisions:
            for enemy in self.enemy_collisions:
                enemy.health -= self.damage
                self.kill()
                break

    def check_state(self):
        if self.walking:
            self.movement_speed = self.orig_movement_speed
            self.load_walk()

    def load_walk(self):
        now = pygame.time.get_ticks()
        if now - self.lastupdate > 70:
            self.lastupdate = now
            self.current_frames = self.walking_frames
            self.current = (self.current + 1) % len(self.current_frames)

    def move(self, dt):
        self.image = self.current_frames[self.current]
        self.rect.midtop = (self.rect.midtop[0], self.starting_point)
        self.starting_point += self.movement_speed * dt
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

    def update(self, dt):
        self.check_collision()
        self.check_state()
        self.move(dt)


class Special(special):
    def __init__(self, level):
        walking_frames = SPECIAL_SATYR
        attacking_frames = SPECIAL_SATYR
        super().__init__(level, walking_frames, attacking_frames, 100, 550)
        self.defense = 5


class Special1(special):
    def __init__(self, level):
        walking_frames = SPECIAL1
        attacking_frames = SPECIAL1
        super().__init__(level, walking_frames, attacking_frames, 100, 550)
        self.defense = 5


class Special2(special):
    def __init__(self, level):
        walking_frames = SPECIAL2
        attacking_frames = SPECIAL2
        super().__init__(level, walking_frames, attacking_frames, 100, 550)
        self.defense = 5


class Special3(special):
    def __init__(self, level):
        walking_frames = SPECIAL3
        attacking_frames = SPECIAL3
        super().__init__(level, walking_frames, attacking_frames, 100, 550)
        self.defense = 5


class Special4(special):
    def __init__(self, level):
        walking_frames = SPECIAL4
        attacking_frames = SPECIAL4
        super().__init__(level, walking_frames, attacking_frames, 400, 550)
        self.defense = 5


class Special5(special):
    def __init__(self, level):
        walking_frames = SPECIAL5
        attacking_frames = SPECIAL5
        super().__init__(level, walking_frames, attacking_frames, 500, 550)
        self.defense = 5
