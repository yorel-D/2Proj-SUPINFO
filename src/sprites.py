from src.settings import *
from random import randrange
import pygame
from random import randrange
from src.Turret.CannonBall import *


class HealthText(pygame.sprite.Sprite):
    def __init__(self, current, max, level, x, y):
        super().__init__()
        font = pygame.font.SysFont(None, 50)
        self.image = font.render(f"Health: {current} / {max} ", True, "white")
        self.rect = self.image.get_rect(topleft=(x, y))
        level.all_sprites.add(self)


class ExpText(pygame.sprite.Sprite):
    def __init__(self, text, level):
        super().__init__()
        font = pygame.font.SysFont(None, 50)
        self.image = font.render("EXP: " + text, True, "white")
        self.rect = self.image.get_rect(topleft=(5 * CELL, 3 * CELL))
        level.all_sprites.add(self)


class HealthBar(pygame.sprite.Sprite):
    def __init__(self, unit, position, x, y):
        super().__init__()
        self.unit = unit
        self.position = position
        self.image = pygame.Surface((80, 3))
        self.topleft = self.unit.rect.topleft
        self.rect = self.image.get_rect(topleft=self.topleft)
        self.max = self.unit.health
        self.width = 80
        if self.position == "back":
            self.image.fill((255, 0, 0))
        if self.position == "front":
            self.image.fill((0, 255, 0))

        self.unit.level.all_sprites.add(self)

    def update(self, dt):
        if self.position == "front":
            self.width = 80 * (self.unit.health / self.max)
            if self.width <= 0:
                self.width = 0
            self.image = game.transform.scale(self.image, (self.width, 3))
        self.topleft = self.unit.rect.topleft
        self.rect = self.image.get_rect(topleft=self.topleft)
        

class MoneyText(pygame.sprite.Sprite):
    def __init__(self, text, level):
        super().__init__()
        font = pygame.font.SysFont(None, 50)
        self.image = font.render("Money: " + text, True, "white")
        self.rect = self.image.get_rect(topleft=(5 * CELL, 10 * CELL))
        level.all_sprites.add(self)


class EnemyRangedCombatUnit(pygame.sprite.Sprite):
    def __init__(self, level, walking_frames, attacking_frames, idle_frames, health, damage, defense, movementspeed,
                 range):
        super().__init__()
        self.level = level
        self.walking_frames = walking_frames
        self.attacking_frames = attacking_frames
        self.idle_frames = idle_frames
        self.current_frames = []
        self.current = 0
        self.health = health
        self.damage = damage
        self.defense = defense
        self.image = self.walking_frames[self.current]
        self.rect = self.image.get_rect(midleft=(106 * CELL, 39 * CELL))
        self.starting_point = self.rect.centerx
        self.walking = True
        self.attacking = False
        self.idle = False
        self.walking_attacking = False
        self.idle_attacking = False
        self.movement_speed = movementspeed
        self.orig_movement_speed = self.movement_speed
        self.range_box = RangeBox(self, range, "enemy")
        self.lastupdate = 0
        self.back_health_bar = HealthBar(self, "back", self.rect.centerx, self.rect.top)
        self.front_health_bar = HealthBar(self, "front", self.rect.centerx, self.rect.top)
        self.level.all_sprites.add(self)
        self.level.ai_sprites.add(self)

    def check_collision(self):

        self.enemy_collisions = game.sprite.spritecollide(self, self.level.player_sprites, False)

        if self.enemy_collisions:

            self.idle = False
            self.attacking = True
            self.walking = False
            if self.current == 6:
                closest_enemy = self.enemy_collisions[0]
                closest_enemy.health -= self.damage
                self.current = 0
        else:
            self.idle = False
            self.walking = True
            self.attacking = False

        ai_sprites_list = [sprite for sprite in self.level.ai_sprites if
                           sprite is not self.level.ai]

        if len(ai_sprites_list) > 1:
            for i in range(1, len(ai_sprites_list)):
                if ai_sprites_list[i].rect.left - ai_sprites_list[i - 1].rect.right <= -10:
                    ai_sprites_list[i].idle = True
                    ai_sprites_list[i].walking = False
                    ai_sprites_list[i].attacking = False
                else:
                    ai_sprites_list[i].idle = False
                    ai_sprites_list[i].walking = True
                    ai_sprites_list[i].attacking = False

        if self.range_box.is_in_range() and self.idle:
            self.idle_attacking = True
            self.walking_attacking = False
            self.attacking = False
            self.walking = False
            self.idle = False
            if self.current == 6:
                enemy = [enemy for enemy in list(self.level.player_sprites) if not enemy == self.level.player]
                enemy.append(self.level.player)
                if enemy:
                    enemy[0].health -= self.damage
                    self.current = 0

        if self.range_box.is_in_range() and self.walking:
            self.walking_attacking = True
            self.idle_attacking = False
            self.attacking = False
            self.walking = False
            self.idle = False
            if self.current == 6:
                enemy = [enemy for enemy in list(self.level.player_sprites) if not enemy == self.level.player]
                enemy.append(self.level.player)
                if enemy:
                    enemy[0].health -= self.damage
                    self.current = 0

    def check_state(self):
        if self.walking:
            self.movement_speed = self.orig_movement_speed
            self.load_walk()
        elif self.attacking:
            self.movement_speed = 0
            self.load_attack()
        elif self.idle:
            self.movement_speed = 0
            self.load_idle()
        elif self.walking_attacking:
            self.movement_speed = self.orig_movement_speed
            self.load_attack()
        elif self.idle_attacking:
            self.movement_speed = 0
            self.load_attack()

    def check_health(self):
        if self.health <= 0:
            self.health = 0
            self.front_health_bar.kill()
            self.back_health_bar.kill()
            self.range_box.kill()
            self.level.player.money += 80
            self.level.player.xp += 70
            self.kill()

    def load_idle(self):
        now = game.time.get_ticks()
        if now - self.lastupdate > 70:
            self.lastupdate = now
            self.current_frames = self.idle_frames
            self.current = (self.current + 1) % (len(self.current_frames))

    def load_walk(self):
        now = game.time.get_ticks()
        if now - self.lastupdate > 70:
            self.lastupdate = now
            self.current_frames = self.walking_frames
            self.current = (self.current + 1) % (len(self.current_frames))

    def load_attack(self):
        now = game.time.get_ticks()
        if now - self.lastupdate > 100:
            self.lastupdate = now
            self.current_frames = self.attacking_frames
            self.current = (self.current + 1) % (len(self.current_frames))

    def move(self, dt):
        self.image = self.current_frames[self.current]
        self.rect = self.current_frames[self.current].get_rect(
            midleft=(int(self.starting_point - self.movement_speed * dt), 39 * CELL))
        self.starting_point -= self.movement_speed * dt
        if self.rect.right < 0:
            self.kill()

    def update(self, dt):
        self.check_collision()
        self.check_state()
        self.move(dt)
        self.check_health()

class PlayerCloseCombatUnit(pygame.sprite.Sprite):
    def __init__(self, level, walking_frames, attacking_frames, idle_frames, health, damage, defense, movementspeed):
        super().__init__()
        self.level = level
        self.walking_frames = walking_frames
        self.attacking_frames = attacking_frames
        self.idle_frames = idle_frames
        self.current_frames = []
        self.current = 0
        self.health = health
        self.damage = damage
        self.defense = defense
        self.image = self.walking_frames[self.current]
        self.rect = self.image.get_rect(midright=(12 * CELL, 39 * CELL))
        self.starting_point = self.rect.centerx
        self.walking = True
        self.attacking = False
        self.idle = False
        self.movement_speed = movementspeed
        self.orig_movement_speed = self.movement_speed
        self.lastupdate = 0
        self.back_health_bar = HealthBar(self, "back", self.rect.centerx, self.rect.top)
        self.front_health_bar = HealthBar(self, "front", self.rect.centerx, self.rect.top)
        self.level.all_sprites.add(self)
        self.level.player_sprites.add(self)

    def check_collision(self):

        self.enemy_collisions = game.sprite.spritecollide(self, self.level.ai_sprites, False)

        if self.enemy_collisions:
            self.idle = False
            self.attacking = True
            self.walking = False
            if self.current == 6:
                closest_enemy = self.enemy_collisions[0]
                closest_enemy.health -= self.damage
                self.current = 0
        else:
            self.idle = False
            self.walking = True
            self.attacking = False

        p_sprites_list = [sprite for sprite in self.level.player_sprites if
                          sprite is not self.level.player]

        if len(p_sprites_list) > 1:
            for i in range(1, len(p_sprites_list)):
                if p_sprites_list[i].rect.right - p_sprites_list[i - 1].rect.left >= -10:
                    p_sprites_list[i].idle = True
                    p_sprites_list[i].walking = False
                    p_sprites_list[i].attacking = False
                else:
                    p_sprites_list[i].idle = False
                    p_sprites_list[i].walking = True
                    p_sprites_list[i].attacking = False

    def check_state(self):
        if self.walking:
            self.movement_speed = self.orig_movement_speed
            self.load_walk()
        elif self.attacking:
            self.movement_speed = 0
            self.load_attack()
        elif self.idle:
            self.movement_speed = 0
            self.load_idle()

    def check_health(self):
        if self.health <= 0:
            self.health = 0
            self.back_health_bar.kill()
            self.front_health_bar.kill()
            self.level.player.money += 20
            self.level.player.xp += 70
            self.kill()

    def load_idle(self):
        now = game.time.get_ticks()
        if now - self.lastupdate > 70:
            self.lastupdate = now
            self.current_frames = self.idle_frames
            self.current = (self.current + 1) % (len(self.current_frames))

    def load_walk(self):
        now = game.time.get_ticks()
        if now - self.lastupdate > 70:
            self.lastupdate = now
            self.current_frames = self.walking_frames
            self.current = (self.current + 1) % (len(self.current_frames))

    def load_attack(self):
        now = game.time.get_ticks()
        if now - self.lastupdate > 100:
            self.lastupdate = now
            self.current_frames = self.attacking_frames
            self.current = (self.current + 1) % (len(self.current_frames))

    def move(self, dt):
        self.image = self.current_frames[self.current]
        self.rect = self.current_frames[self.current].get_rect(
            midleft=(int(self.starting_point + self.movement_speed * dt), 39 * CELL))
        self.starting_point += self.movement_speed * dt
        if self.rect.left > SCREEN_WIDTH:
            self.kill()

    def update(self, dt):
        self.check_collision()
        self.check_state()
        self.move(dt)
        self.check_health()


class EnemyCloseCombatUnit(pygame.sprite.Sprite):

    def __init__(self, level, walking_frames, attacking_frames, idle_frames, health, damage, defense, movementspeed):
        super().__init__()
        self.level = level
        self.walking_frames = walking_frames
        self.attacking_frames = attacking_frames
        self.idle_frames = idle_frames
        self.current_frames = []
        self.current = 0
        self.health = health
        self.damage = damage
        self.defense = defense
        self.image = self.walking_frames[self.current]
        self.rect = self.image.get_rect(midleft=(106 * CELL, 39 * CELL))
        self.starting_point = self.rect.centerx
        self.walking = True
        self.attacking = False
        self.idle = False
        self.movement_speed = movementspeed
        self.orig_movement_speed = self.movement_speed
        self.lastupdate = 0
        self.back_health_bar = HealthBar(self, "back", self.rect.centerx, self.rect.top)
        self.front_health_bar = HealthBar(self, "front", self.rect.centerx, self.rect.top)
        self.level.all_sprites.add(self)
        self.level.ai_sprites.add(self)

    def check_collision(self):

        self.enemy_collisions = game.sprite.spritecollide(self, self.level.player_sprites, False)

        if self.enemy_collisions:

            self.idle = False
            self.attacking = True
            self.walking = False
            if self.current == 6:
                closest_enemy = self.enemy_collisions[0]
                closest_enemy.health -= self.damage
                self.current = 0
        else:
            self.idle = False
            self.walking = True
            self.attacking = False

        ai_sprites_list = [sprite for sprite in self.level.ai_sprites if
                           sprite is not self.level.ai]

        if len(ai_sprites_list) > 1:
            for i in range(1, len(ai_sprites_list)):
                if ai_sprites_list[i].rect.left - ai_sprites_list[i - 1].rect.right <= -10:
                    ai_sprites_list[i].idle = True
                    ai_sprites_list[i].walking = False
                    ai_sprites_list[i].attacking = False
                else:
                    ai_sprites_list[i].idle = False
                    ai_sprites_list[i].walking = True
                    ai_sprites_list[i].attacking = False

    def check_state(self):
        if self.walking:
            self.movement_speed = self.orig_movement_speed
            self.load_walk()
        elif self.attacking:
            self.movement_speed = 0
            self.load_attack()
        elif self.idle:
            self.movement_speed = 0
            self.load_idle()

    def check_health(self):
        if self.health <= 0:
            self.health = 0
            self.front_health_bar.kill()
            self.back_health_bar.kill()
            self.level.player.money += 80
            self.level.player.xp += 70
            self.kill()

    def load_idle(self):
        now = game.time.get_ticks()
        if now - self.lastupdate > 70:
            self.lastupdate = now
            self.current_frames = self.idle_frames
            self.current = (self.current + 1) % (len(self.current_frames))

    def load_walk(self):
        now = game.time.get_ticks()
        if now - self.lastupdate > 70:
            self.lastupdate = now
            self.current_frames = self.walking_frames
            self.current = (self.current + 1) % (len(self.current_frames))

    def load_attack(self):
        now = game.time.get_ticks()
        if now - self.lastupdate > 100:
            self.lastupdate = now
            self.current_frames = self.attacking_frames
            self.current = (self.current + 1) % (len(self.current_frames))

    def move(self, dt):
        self.image = self.current_frames[self.current]
        self.rect = self.current_frames[self.current].get_rect(
            midleft=(int(self.starting_point - self.movement_speed * dt), 39 * CELL))
        self.starting_point -= self.movement_speed * dt
        if self.rect.right < 0:
            self.kill()

    def update(self, dt):
        self.check_collision()
        self.check_state()
        self.move(dt)
        self.check_health()


class EnemyLightPirate(EnemyCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_LIGHT_SATYR_WALKING, ENEMY_LIGHT_SATYR_ATTACKING, ENEMY_LIGHT_SATYR_IDLE, 100,
                         8, 8, 55)


class EnemyHeavyPirate(EnemyCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_HEAVY_SATYR_WALKING, ENEMY_HEAVY_SATYR_ATTACKING, ENEMY_HEAVY_SATYR_IDLE, 160,
                         10, 10, 55)


class EnemyHeroPirate(EnemyRangedCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_HERO_SATYR_WALKING, ENEMY_HERO_SATYR_ATTACKING, ENEMY_HERO_SATYR_IDLE, 190,
                         20, 20, 55, 3)


class EnemyRangedPirate(EnemyCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_RANGED_SATYR_WALKING, ENEMY_RANGED_SATYR_ATTACKING, ENEMY_RANGED_SATYR_IDLE,
                         180, 15, 15, 550)


class EnemyLightWarrior(EnemyCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_LIGHT_GOLEM_WALKING, ENEMY_LIGHT_GOLEM_ATTACKING, ENEMY_LIGHT_GOLEM_IDLE,
                         130, 20, 15, 60)


class EnemyHeavyWarrior(EnemyCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_HEAVY_GOLEM_WALKING, ENEMY_HEAVY_GOLEM_ATTACKING, ENEMY_HEAVY_GOLEM_IDLE,
                         190, 35, 20, 60)


class EnemyRangedWarrior(EnemyCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_RANGED_GOLEM_WALKING, ENEMY_RANGED_GOLEM_ATTACKING,
                         ENEMY_RANGED_GOLEM_IDLE, 200, 40, 10, 60)

class EnemyHeroWarrior(EnemyRangedCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_HERO_GOLEM_WALKING, ENEMY_HERO_GOLEM_ATTACKING,
                         ENEMY_HERO_GOLEM_IDLE, 220, 50, 20, 60, 3)


class EnemyLightFairy(EnemyCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_LIGHT_ELF_WALKING, ENEMY_LIGHT_ELF_ATTACKING, ENEMY_LIGHT_ELF_IDLE, 150, 50,
                         20, 65)


class EnemyHeavyFairy(EnemyCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_HEAVY_ELF_WALKING, ENEMY_HEAVY_ELF_ATTACKING, ENEMY_HEAVY_ELF_IDLE, 240, 75,
                         28, 65)


class EnemyRangedFairy(EnemyRangedCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_RANGED_ELF_WALKING, ENEMY_RANGED_ELF_ATTACKING, ENEMY_RANGED_ELF_IDLE, 130, 100,
                         14, 65, 3)

class EnemyHeroFairy(EnemyRangedCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_HERO_ELF_WALKING, ENEMY_HERO_ELF_ATTACKING, ENEMY_HERO_ELF_IDLE, 240, 150,
                         32, 65, 3)

class EnemyLightAngel(EnemyCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_LIGHT_ANGEL_WALKING, ENEMY_LIGHT_ANGEL_ATTACKING, ENEMY_LIGHT_ANGEL_IDLE, 150, 150,
                         20, 70)
        
class EnemyHeavyAngel(EnemyCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_HEAVY_ANGEL_WALKING, ENEMY_HEAVY_ANGEL_ATTACKING, ENEMY_HEAVY_ANGEL_IDLE, 150, 175,
                         20, 70)

class EnemyRangedAngel(EnemyCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_RANGED_ANGEL_WALKING, ENEMY_RANGED_ANGEL_ATTACKING, ENEMY_RANGED_ANGEL_IDLE, 150, 200,
                         20, 70)

class EnemyHeroAngel(EnemyCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_HERO_ANGEL_WALKING, ENEMY_HERO_ANGEL_ATTACKING, ENEMY_HERO_ANGEL_IDLE, 150, 250,
                         20, 70)

class EnemyLightWraith(EnemyRangedCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_LIGHT_WRAITH_WALKING, ENEMY_LIGHT_WRAITH_ATTACKING, ENEMY_LIGHT_WRAITH_IDLE, 150, 250,
                         20, 75, 3)
        
class EnemyHeavyWraith(EnemyRangedCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_HEAVY_WRAITH_WALKING, ENEMY_HEAVY_WRAITH_ATTACKING, ENEMY_HEAVY_WRAITH_IDLE, 150, 275,
                         20, 75, 3)

class EnemyRangedWraith(EnemyRangedCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_RANGED_WRAITH_WALKING, ENEMY_RANGED_WRAITH_ATTACKING, ENEMY_RANGED_WRAITH_IDLE, 150, 300,
                         20, 75, 3)

class EnemyHeroWraith(EnemyRangedCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_HERO_WRAITH_WALKING, ENEMY_HERO_WRAITH_ATTACKING, ENEMY_HERO_WRAITH_IDLE, 150, 350,
                         20, 75, 3)


class EnemyLightVillager(EnemyCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_LIGHT_VILLAGER_WALKING, ENEMY_LIGHT_VILLAGER_ATTACKING, ENEMY_LIGHT_VILLAGER_IDLE, 150, 350,
                         20, 80)
        
class EnemyHeavyVillager(EnemyCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_HEAVY_VILLAGER_WALKING, ENEMY_HEAVY_VILLAGER_ATTACKING, ENEMY_HEAVY_VILLAGER_IDLE, 150, 375,
                         20, 80)

class EnemyRangedVillager(EnemyCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_RANGED_VILLAGER_WALKING, ENEMY_RANGED_VILLAGER_ATTACKING, ENEMY_RANGED_VILLAGER_IDLE, 150, 400,
                         20, 80)

class EnemyHeroVillager(EnemyCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_HERO_VILLAGER_WALKING, ENEMY_HERO_VILLAGER_ATTACKING, ENEMY_HERO_VILLAGER_IDLE, 150, 500,
                         20, 80)


class RangeBox(game.sprite.Sprite):
    def __init__(self, unit, range, type):
        super().__init__()
        self.unit = unit
        self.type = type
        self.range = range
        self.image = game.Surface((self.unit.image.get_width() * self.range, self.unit.image.get_height()))
        self.image.fill((0, 255, 0))
        self.image.set_alpha(0)
        if self.type == "player":
            self.rect = self.image.get_rect(bottomleft=self.unit.rect.bottomleft)
        if self.type == "enemy":
            self.rect = self.image.get_rect(bottomright=self.unit.rect.bottomright)
        self.unit.level.all_sprites.add(self)

    def is_in_range(self):
        if self.type == "player":
            return game.sprite.spritecollide(self, self.unit.level.ai_sprites, False)
        if self.type == "enemy":
            return game.sprite.spritecollide(self, self.unit.level.player_sprites, False)
        else:
            return False

    def update(self, dt):
        if self.type == "player":
            self.rect = self.image.get_rect(bottomleft=self.unit.rect.bottomleft)
        if self.type == "enemy":
            self.rect = self.image.get_rect(bottomright=self.unit.rect.bottomright)


class PlayerRangedCombatUnit(pygame.sprite.Sprite):
    def __init__(self, level, walking_frames, attacking_frames, idle_frames, health, damage, defense, movementspeed,
                 range):
        super().__init__()
        self.level = level
        self.walking_frames = walking_frames
        self.attacking_frames = attacking_frames
        self.idle_frames = idle_frames
        self.current_frames = []
        self.current = 0
        self.health = health
        self.damage = damage
        self.defense = defense
        self.image = self.walking_frames[self.current]
        self.rect = self.image.get_rect(midright=(12 * CELL, 39 * CELL))
        self.movement_speed = movementspeed
        self.orig_movement_speed = self.movement_speed
        self.range_box = RangeBox(self, range, "player")
        self.starting_point = self.rect.centerx
        self.walking = True
        self.attacking = False
        self.walking_attacking = False
        self.idle_attacking = False
        self.idle = False
        self.movement_speed = movementspeed
        self.orig_movement_speed = self.movement_speed
        self.lastupdate = 0
        self.back_health_bar = HealthBar(self, "back", self.rect.centerx, self.rect.top)
        self.front_health_bar = HealthBar(self, "front", self.rect.centerx, self.rect.top)
        self.level.all_sprites.add(self)
        self.level.player_sprites.add(self)

    def check_collision(self):

        self.enemy_collisions = game.sprite.spritecollide(self, self.level.ai_sprites, False)

        if self.enemy_collisions:
            self.idle = False
            self.attacking = True
            self.walking = False
            if self.current == 6:
                closest_enemy = self.enemy_collisions[0]
                closest_enemy.health -= self.damage
                self.current = 0
        else:
            self.idle = False
            self.walking = True
            self.attacking = False

        p_sprites_list = [sprite for sprite in self.level.player_sprites if
                          sprite is not self.level.player]

        if len(p_sprites_list) > 1:
            for i in range(1, len(p_sprites_list)):
                if p_sprites_list[i].rect.right - p_sprites_list[i - 1].rect.left >= -10:
                    p_sprites_list[i].idle = True
                    p_sprites_list[i].walking = False
                    p_sprites_list[i].attacking = False
                else:
                    p_sprites_list[i].idle = False
                    p_sprites_list[i].walking = True
                    p_sprites_list[i].attacking = False

        if self.range_box.is_in_range() and self.idle:
            self.idle_attacking = True
            self.walking_attacking = False
            self.attacking = False
            self.walking = False
            self.idle = False
            if self.current == 6:
                enemy = [enemy for enemy in list(self.level.ai_sprites) if not enemy == self.level.ai]
                enemy.append(self.level.ai)
                if enemy:
                    enemy[0].health -= self.damage
                    self.current = 0

        if self.range_box.is_in_range() and self.walking:
            self.walking_attacking = True
            self.idle_attacking = False
            self.attacking = False
            self.walking = False
            self.idle = False
            if self.current == 6:
                enemy = [enemy for enemy in list(self.level.ai_sprites) if not enemy == self.level.ai]
                enemy.append(self.level.ai)
                if enemy:
                    enemy[0].health -= self.damage
                    self.current = 0

    def check_state(self):
        if self.walking:
            self.movement_speed = self.orig_movement_speed
            self.load_walk()
        elif self.attacking:
            self.movement_speed = 0
            self.load_attack()
        elif self.idle:
            self.movement_speed = 0
            self.load_idle()
        elif self.walking_attacking:
            self.movement_speed = self.orig_movement_speed
            self.load_attack()
        elif self.idle_attacking:
            self.movement_speed = 0
            self.load_attack()

    def check_health(self):
        if self.health <= 0:
            self.health = 0
            self.range_box.kill()
            self.back_health_bar.kill()
            self.front_health_bar.kill()
            self.level.player.money += 20
            self.level.player.xp += 70
            self.kill()

    def load_idle(self):
        now = game.time.get_ticks()
        if now - self.lastupdate > 70:
            self.lastupdate = now
            self.current_frames = self.idle_frames
            self.current = (self.current + 1) % (len(self.current_frames))

    def load_walk(self):
        now = game.time.get_ticks()
        if now - self.lastupdate > 70:
            self.lastupdate = now
            self.current_frames = self.walking_frames
            self.current = (self.current + 1) % (len(self.current_frames))

    def load_attack(self):
        now = game.time.get_ticks()
        if now - self.lastupdate > 100:
            self.lastupdate = now
            self.current_frames = self.attacking_frames
            self.current = (self.current + 1) % (len(self.current_frames))

    def move(self, dt):
        self.image = self.current_frames[self.current]
        self.rect = self.current_frames[self.current].get_rect(
            midleft=(int(self.starting_point + self.movement_speed * dt), 39 * CELL))
        self.starting_point += self.movement_speed * dt
        if self.rect.left > SCREEN_WIDTH:
            self.kill()

    def update(self, dt):
        self.check_collision()
        self.check_state()
        self.move(dt)
        self.check_health()


class PlayerLightPirate(PlayerCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_LIGHT_SATYR_WALKING, PLAYER_LIGHT_SATYR_ATTACKING, PLAYER_LIGHT_SATYR_IDLE,
                         100, 8, 8, 55)

class PlayerHeavyPirate(PlayerCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_HEAVY_SATYR_WALKING, PLAYER_HEAVY_SATYR_ATTACKING, PLAYER_HEAVY_SATYR_IDLE,
                         160, 10, 10, 55)

class PlayerRangedPirate(PlayerCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_RANGED_SATYR_WALKING, PLAYER_RANGED_SATYR_ATTACKING, PLAYER_RANGED_SATYR_IDLE,
                         180, 15, 15, 55)

class PlayerHeroPirate(PlayerRangedCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_HERO_SATYR_WALKING, PLAYER_HERO_SATYR_ATTACKING, PLAYER_HERO_SATYR_IDLE,
                         190, 20, 20, 55, 3)


class PlayerLightWarrior(PlayerCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_LIGHT_GOLEM_WALIKNG, PLAYER_LIGHT_GOLEM_ATTACKING, PLAYER_LIGHT_GOLEM_IDLE,
                         130, 20, 15, 60)


class PlayerHeavyWarrior(PlayerCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_HEAVY_GOLEM_WALIKNG, PLAYER_HEAVY_GOLEM_ATTACKING, PLAYER_HEAVY_GOLEM_IDLE,
                         190, 35, 20, 60)


class PlayerRangedWarrior(PlayerCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_RANGED_GOLEM_WALIKNG, PLAYER_RANGED_GOLEM_ATTACKING,
                         PLAYER_RANGED_GOLEM_IDLE, 200, 40, 10, 60)
        
        
class PlayerHeroWarrior(PlayerRangedCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_HERO_GOLEM_WALIKNG, PLAYER_HERO_GOLEM_ATTACKING, PLAYER_HERO_GOLEM_IDLE,
                         220, 50, 20, 60, 3)


class PlayerLightFairy(PlayerCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_LIGHT_ELF_WALKING, PLAYER_LIGHT_ELF_ATTACKING, PLAYER_LIGHT_ELF_IDLE, 150, 50,
                         20, 65)


class PlayerHeavyFairy(PlayerCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_HEAVY_ELF_WALKING, PLAYER_HEAVY_ELF_ATTACKING, PLAYER_HEAVY_ELF_IDLE, 240, 75,
                         28, 65)


class PlayerRangedFairy(PlayerRangedCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_RANGED_ELF_WALKING, PLAYER_RANGED_ELF_ATTACKING, PLAYER_RANGED_ELF_IDLE, 230, 100,
                         14, 65, 3)

class PlayerHeroFairy(PlayerRangedCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_HERO_ELF_WALKING, PLAYER_HERO_ELF_ATTACKING, PLAYER_HERO_ELF_IDLE, 240, 150,
                         32, 65, 3)

class PlayerLightAngel(PlayerCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_LIGHT_ANGEL_WALKING, PLAYER_LIGHT_ANGEL_ATTACKING, PLAYER_LIGHT_ANGEL_IDLE, 150, 150,
                         20, 70)
        
class PlayerHeavyAngel(PlayerCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_HEAVY_ANGEL_WALKING, PLAYER_HEAVY_ANGEL_ATTACKING, PLAYER_HEAVY_ANGEL_IDLE, 150, 175,
                         20, 70)

class PlayerRangedAngel(PlayerCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_RANGED_ANGEL_WALKING, PLAYER_RANGED_ANGEL_ATTACKING, PLAYER_RANGED_ANGEL_IDLE, 150, 200,
                         20, 70)

class PlayerHeroAngel(PlayerCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_HERO_ANGEL_WALKING, PLAYER_HERO_ANGEL_ATTACKING, PLAYER_HERO_ANGEL_IDLE, 150, 250,
                         20, 70)

class PlayerLightWraith(PlayerRangedCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_LIGHT_WRAITH_WALKING, PLAYER_LIGHT_WRAITH_ATTACKING, PLAYER_LIGHT_WRAITH_IDLE, 150, 250,
                         20, 75, 3)
        
class PlayerHeavyWraith(PlayerRangedCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_HEAVY_WRAITH_WALKING, PLAYER_HEAVY_WRAITH_ATTACKING, PLAYER_HEAVY_WRAITH_IDLE, 150, 275,
                         20, 75, 3)

class PlayerRangedWraith(PlayerRangedCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_RANGED_WRAITH_WALKING, PLAYER_RANGED_WRAITH_ATTACKING, PLAYER_RANGED_WRAITH_IDLE, 150, 300,
                         20, 75, 3)

class PlayerHeroWraith(PlayerRangedCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_HERO_WRAITH_WALKING, PLAYER_HERO_WRAITH_ATTACKING, PLAYER_HERO_WRAITH_IDLE, 150, 350,
                         20, 75, 3)


class PlayerLightVillager(PlayerCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_LIGHT_VILLAGER_WALKING, PLAYER_LIGHT_VILLAGER_ATTACKING, PLAYER_LIGHT_VILLAGER_IDLE, 150, 350,
                         20, 80)
        
class PlayerHeavyVillager(PlayerCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_HEAVY_VILLAGER_WALKING, PLAYER_HEAVY_VILLAGER_ATTACKING, PLAYER_HEAVY_VILLAGER_IDLE, 150, 375,
                         20, 80)

class PlayerRangedVillager(PlayerCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_RANGED_VILLAGER_WALKING, PLAYER_RANGED_VILLAGER_ATTACKING, PLAYER_RANGED_VILLAGER_IDLE, 150, 400,
                         20, 80)

class PlayerHeroVillager(PlayerCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_HERO_VILLAGER_WALKING, PLAYER_HERO_VILLAGER_ATTACKING, PLAYER_HERO_VILLAGER_IDLE, 150, 500,
                         20, 80)

