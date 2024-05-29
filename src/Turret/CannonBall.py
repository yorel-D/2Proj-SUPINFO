from src.settings import *
import math
import pygame

class CannonBall(pygame.sprite.Sprite):
    def __init__(self, turret, image, angle, damage, speed):
        super().__init__()
        self.turret = turret
        self.image = image
        self.rect = self.image.get_rect(center=self.turret.rect.center)
        self.angle = angle
        self.damage = damage
        self.speed = speed
        self.x = self.rect.centerx
        self.y = self.rect.centery
        self.dx = (math.cos(self.angle) * self.speed)
        self.dy = (math.sin(self.angle) * self.speed)
        self.turret.level.all_sprites.add(self)

    def update(self, dt):
        if self.rect.x > self.turret.range_point_X or self.rect.y > self.turret.range_point_Y:
            self.kill()
        enemy_collision = game.sprite.spritecollide(self, self.turret.enemies, False)
        if enemy_collision:
            enemy_collision[0].health -= self.damage
            self.kill()

        self.x += self.dx * dt
        self.y += self.dy * dt
        self.rect.centerx = self.x
        self.rect.centery = self.y


class Turret3(pygame.sprite.Sprite):
    def __init__(self, level, topleft):
        super().__init__()
        self.image = PLAYER_ELF_TURRET
        self.level = level
        self.rect = self.image.get_rect(topleft=topleft)
        self.range_point = (62 * CELL, 44 * CELL)
        self.shooting_speed = 400
        self.price = 2400
        self.lastshot = 0
        self.enemies = [sprite for sprite in self.level.ai_sprites if sprite is not self.level.ai]
        self.level.all_sprites.add(self)

    def shoot(self):
        x_dist = 62 * CELL - self.rect.centerx
        y_dist = 44 * CELL - self.rect.centery
        self.angle = math.atan2(y_dist, x_dist)
        now = game.time.get_ticks()
        if self.enemies and self.enemies[0].rect.midbottom[0] < 62 * CELL:
            if now - self.lastshot > self.shooting_speed:
                self.lastshot = now
                x_dist = self.enemies[0].rect.midbottom[0] - self.rect.centerx
                y_dist = self.enemies[0].rect.midbottom[1] - self.rect.centery
                self.angle = math.atan2(y_dist, x_dist)
                cannonball = CannonBall3(self, self.angle)

    def sell(self):
        self.level.player.money += self.price / 2
        self.kill()

    def update(self, dt):
        self.enemies = [sprite for sprite in self.level.ai_sprites if sprite is not self.level.ai]
        self.shoot()


class CannonBall3(CannonBall):
    def __init__(self, turret, angle, damage, speed):
        super().__init__(turret, ELF_CANNONBALL, angle, damage=damage, speed=speed)


class Turret2(pygame.sprite.Sprite):
    def __init__(self, level, topleft):
        super().__init__()
        self.image = PLAYER_GOLEM_TURRET
        self.level = level
        self.rect = self.image.get_rect(topleft=topleft)
        self.range_point = (55 * CELL, 44 * CELL)
        self.shooting_speed = 500
        self.price = 1500
        self.lastshot = 0
        self.enemies = [sprite for sprite in self.level.ai_sprites if sprite is not self.level.ai]
        self.level.all_sprites.add(self)

    def shoot(self):
        x_dist = 55 * CELL - self.rect.centerx
        y_dist = 44 * CELL - self.rect.centery
        self.angle = math.atan2(y_dist, x_dist)
        now = game.time.get_ticks()
        if self.enemies and self.enemies[0].rect.midbottom[0] < 55 * CELL:
            if now - self.lastshot > self.shooting_speed:
                self.lastshot = now
                x_dist = self.enemies[0].rect.midbottom[0] - self.rect.centerx
                y_dist = self.enemies[0].rect.midbottom[1] - self.rect.centery
                self.angle = math.atan2(y_dist, x_dist)
                cannonball = CannonBall2(self, self.angle)

    def sell(self):
        self.level.player.money += self.price / 2
        self.kill()

    def update(self, dt):
        self.enemies = [sprite for sprite in self.level.ai_sprites if sprite is not self.level.ai]
        self.shoot()


class CannonBall2(CannonBall):
    def __init__(self, turret, angle, damage, speed):
        super().__init__(turret, GOLEM_CANNONBALL, angle, damage=damage, speed=speed)


class Turret1(pygame.sprite.Sprite):
    def __init__(self, level, topleft):
        super().__init__()
        self.level = level
        self.image = PLAYER_SATYR_TURRET
        self.rect = self.image.get_rect(topleft=topleft)
        self.range_point = (48 * CELL, 44 * CELL)
        self.shooting_speed = 600
        self.price = 400
        self.lastshot = 0
        self.enemies = [sprite for sprite in self.level.ai_sprites if sprite is not self.level.ai]
        self.level.all_sprites.add(self)

    def shoot(self):
        x_dist = 48 * CELL - self.rect.centerx
        y_dist = 44 * CELL - self.rect.centery
        self.angle = math.atan2(y_dist, x_dist)
        now = game.time.get_ticks()
        if self.enemies and self.enemies[0].rect.midbottom[0] < 48 * CELL:
            if now - self.lastshot > self.shooting_speed:
                self.lastshot = now
                x_dist = self.enemies[0].rect.midbottom[0] - self.rect.centerx
                y_dist = self.enemies[0].rect.midbottom[1] - self.rect.centery
                self.angle = math.atan2(y_dist, x_dist)
                cannonball = CannonBall1(self, self.angle)

    def sell(self):
        self.level.player.money += self.price / 2
        self.kill()

    def update(self, dt):
        self.enemies = [sprite for sprite in self.level.ai_sprites if sprite is not self.level.ai]
        self.shoot()


class CannonBall1(CannonBall):
    def __init__(self, turret, angle,damage, speed):
        super().__init__(turret, SATYR_CANNONBALL, angle, damage=damage, speed=speed)


class CannonBall2(CannonBall):
    def __init__(self, turret, angle,damage, speed):
        super().__init__(turret, CANNONBALL1, angle, damage=damage, speed=speed)


class CannonBall3(CannonBall):
    def __init__(self, turret, angle,damage, speed):
        super().__init__(turret, CANNONBALL2, angle, damage=damage, speed=speed)


class CannonBall4(CannonBall):
    def __init__(self, turret, angle,damage, speed):
        super().__init__(turret, CANNONBALL3, angle, damage=damage, speed=speed)


class CannonBall5(CannonBall):
    def __init__(self, turret, angle,damage, speed):
        super().__init__(turret, CANNONBALL4, angle, damage=damage, speed=speed)


class CannonBall6(CannonBall):
    def __init__(self, turret, angle,damage, speed):
        super().__init__(turret, CANNONBALL5, angle, damage=damage, speed=speed)
