from settings import *
from random import randrange
import math
import pygame


class ActionBar(pygame.sprite.Sprite):
    def __init__(self, level, state):
        super().__init__()
        self.state = state
        self.level = level
        self.image = pygame.Surface((1280, 170))
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        self.level.all_sprites.add(self)
        self.unlock_turret_placemant = UnlockTurretPlacemant(TURRET_UPGRADE_ICON, self.level,
                                                             TURRET_UPGRADE_ICON.get_rect(topright=(95 * CELL, 9 * CELL)))
        self.pirate_turret_button = PirateTurretButton(PIRATE_TURRET_ICON, self.level,
                                                       PIRATE_TURRET_ICON.get_rect(topright=(105 * CELL, 9 * CELL)))
        self.warrior_turret_button = WarriorTurretButton(WARRIOR_TURRET_ICON, self.level,
                                                         WARRIOR_TURRET_ICON.get_rect(topright=(115 * CELL, 9 * CELL)))
        self.elf_turret_button = ElfTurretButton(ELF_TURRET_ICON, self.level,
                                                 ELF_TURRET_ICON.get_rect(topright=(125 * CELL, 9 * CELL)))
        #self.elf_turret_button.active = True # for testing
        #c'est ici que les tourelle sont initialis?,et le # en haut permet de debloquer une tourrelle sans etre lvl 2 ou autre


        self.sell_button = SellButton(self.level, self.pirate_turret_button, self.warrior_turret_button,
                                      self.elf_turret_button)
        self.upgrade_button = UpgradeButton(self)
        if self.state == "pirates":
            self.light_unit_button = LightPirateButton(LIGHT_PIRATE_ICON, self.level,
                                                       LIGHT_PIRATE_ICON.get_rect(topright=(105 * CELL, 1 * CELL)))
            self.ranged_unit_button = RangedPirateButton(RANGED_PIRATE_ICON, self.level,
                                                         RANGED_PIRATE_ICON.get_rect(topright=(115 * CELL, 1 * CELL)))
            self.heavy_unit_button = HeavyPirateButton(HEAVY_PIRATE_ICON, self.level,
                                                       HEAVY_PIRATE_ICON.get_rect(topright=(125 * CELL, 1 * CELL)))
        elif self.state == "warriors":
            self.light_unit_button = LightWarriorButton(LIGHT_WARRIOR_ICON, self.level,
                                                        LIGHT_WARRIOR_ICON.get_rect(topright=(105 * CELL, 1 * CELL)))
            self.ranged_unit_button = RangedWarriorButton(RANGED_WARRIOR_ICON, self.level,
                                                          RANGED_WARRIOR_ICON.get_rect(topright=(115 * CELL, 1 * CELL)))
            self.heavy_unit_button = HeavyWarriorButton(HEAVY_WARRIOR_ICON, self.level,
                                                        HEAVY_WARRIOR_ICON.get_rect(topright=(125 * CELL, 1 * CELL)))
        elif self.state == "elfs":
            self.light_unit_button = LightElfButton(LIGHT_ELF_ICON, self.level,
                                                    LIGHT_ELF_ICON.get_rect(topright=(105 * CELL, 1 * CELL)))
            self.ranged_unit_button = RangedElfButton(RANGED_ELF_ICON, self.level,
                                                      RANGED_ELF_ICON.get_rect(topright=(115 * CELL, 1 * CELL)))
            self.heavy_unit_button = HeavyElfButton(HEAVY_ELF_ICON, self.level,
                                                    HEAVY_ELF_ICON.get_rect(topright=(125 * CELL, 1 * CELL)))



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


class MoneyText(pygame.sprite.Sprite):
    def __init__(self, text, level):
        super().__init__()
        font = pygame.font.SysFont(None, 50)
        self.image = font.render("Money: " + text, True, "white")
        self.rect = self.image.get_rect(topleft=(5 * CELL, 10 * CELL))
        level.all_sprites.add(self)


class SellButton(pygame.sprite.Sprite):
    def __init__(self, level, tb1, tb2, tb3):
        super().__init__()
        self.level = level
        self.tb1 = tb1
        self.tb2 = tb2
        self.tb3 = tb3
        self.image = SELL_BUTTON
        self.rect = self.image.get_rect(topleft=(45 * CELL, 3 * CELL))
        self.level.all_sprites.add(self)
        self.clicked = False

    def check_click(self):
        m_pos = game.mouse.get_pos()
        if self.clicked == False and self.rect.collidepoint(m_pos) and game.mouse.get_pressed()[0]:
            self.image.set_alpha(128)
            #print(self.tb1.tower1.rect)
            #print(m_pos)
            self.clicked = not self.clicked

        if self.clicked and self.tb1.tower1.rect.collidepoint(m_pos) and game.mouse.get_pressed()[0]:
            #print("should sell")
            try:
                self.tb1.tower1.turret.sell()
            except AttributeError:
                pass
            self.tb1.towers[self.tb1.tower1] = "available"

        if self.clicked and self.tb1.tower2.rect.collidepoint(m_pos) and game.mouse.get_pressed()[0]:
            #print("should sell")
            try:
                self.tb1.tower2.turret.sell()
            except AttributeError:
                pass
            self.tb1.towers[self.tb1.tower2] = "available"

        if self.clicked and self.tb1.tower3.rect.collidepoint(m_pos) and game.mouse.get_pressed()[0]:
            #print("should sell")
            try:
                self.tb1.tower3.turret.sell()
            except AttributeError:
                pass
            self.tb1.towers[self.tb1.tower3] = "available"

        if self.clicked and self.tb1.tower4.rect.collidepoint(m_pos) and game.mouse.get_pressed()[0]:
            #print("should sell")
            try:
                self.tb1.tower4.turret.sell()
            except AttributeError:
                pass
            self.tb1.towers[self.tb1.tower4] = "available"

        if self.clicked and self.tb2.tower1.rect.collidepoint(m_pos) and game.mouse.get_pressed()[0]:
            #print("should sell")
            try:
                self.tb2.tower1.turret.sell()
            except AttributeError:
                pass
            self.tb2.towers[self.tb2.tower1] = "available"

        if self.clicked and self.tb2.tower2.rect.collidepoint(m_pos) and game.mouse.get_pressed()[0]:
            print("should sell")
            try:
                self.tb2.tower2.turret.sell()
            except AttributeError:
                pass
            self.tb2.towers[self.tb2.tower2] = "available"

        if self.clicked and self.tb2.tower3.rect.collidepoint(m_pos) and game.mouse.get_pressed()[0]:
            print("should sell")
            try:
                self.tb2.tower3.turret.sell()
            except AttributeError:
                pass
            self.tb2.towers[self.tb2.tower3] = "available"

        if self.clicked and self.tb2.tower4.rect.collidepoint(m_pos) and game.mouse.get_pressed()[0]:
            print("should sell")
            try:
                self.tb2.tower4.turret.sell()
            except AttributeError:
                pass
            self.tb2.towers[self.tb2.tower4] = "available"

        if self.clicked and self.tb3.tower1.rect.collidepoint(m_pos) and game.mouse.get_pressed()[0]:
            print("should sell")
            try:
                self.tb3.tower1.turret.sell()
            except AttributeError:
                pass
            self.tb3.towers[self.tb3.tower1] = "available"

        if self.clicked and self.tb3.tower2.rect.collidepoint(m_pos) and game.mouse.get_pressed()[0]:
            print("should sell")
            try:
                self.tb3.tower2.turret.sell()
            except AttributeError:
                pass
            self.tb3.towers[self.tb3.tower2] = "available"

        if self.clicked and self.tb3.tower3.rect.collidepoint(m_pos) and game.mouse.get_pressed()[0]:
            print("should sell")
            try:
                self.tb3.tower3.turret.sell()
            except AttributeError:
                pass
            self.tb3.towers[self.tb3.tower3] = "available"

        if self.clicked and self.tb3.tower4.rect.collidepoint(m_pos) and game.mouse.get_pressed()[0]:
            print("should sell")
            try:
                self.tb3.tower4.turret.sell()
            except AttributeError:
                pass
            self.tb3.towers[self.tb3.tower4] = "available"

        if self.clicked and not self.rect.collidepoint(m_pos) and game.mouse.get_pressed()[0]:
            self.clicked = not self.clicked
            self.image.set_alpha(255)

    def update(self, dt):
        self.check_click()


class UpgradeButton(pygame.sprite.Sprite):
    def __init__(self, action_bar):
        super().__init__()
        self.action_bar = action_bar
        self.image = UPGRADE_BUTTON
        self.rect = self.image.get_rect(topleft=(60 * CELL, 3 * CELL))
        self.action_bar.level.all_sprites.add(self)
        self.state = "pirates"
        self.active = True
        self.last_update = 0

    def check_click(self):
        if not self.state == "elfs":
            m_pos = pygame.mouse.get_pos()
            now = game.time.get_ticks()
            if now - self.last_update > 5000:
                self.last_update = now
                if self.state == "warriors":
                    if self.active and self.rect.collidepoint(m_pos) and pygame.mouse.get_pressed()[0]:
                        self.action_bar.level.player.xp -= 5000
                        self.active = False
                        self.action_bar.light_unit_button.cooldown_bar.kill()
                        self.action_bar.ranged_unit_button.cooldown_bar.kill()
                        self.action_bar.heavy_unit_button.cooldown_bar.kill()
                        self.action_bar.light_unit_button.kill()
                        self.action_bar.ranged_unit_button.kill()
                        self.action_bar.heavy_unit_button.kill()
                        self.action_bar.light_unit_button = LightElfButton(LIGHT_ELF_ICON, self.action_bar.level,
                                                                           LIGHT_ELF_ICON.get_rect(
                                                                               topright=(105 * CELL, 1 * CELL)))
                        self.action_bar.ranged_unit_button = RangedElfButton(RANGED_ELF_ICON, self.action_bar.level,
                                                                             RANGED_ELF_ICON.get_rect(
                                                                                 topright=(115 * CELL, 1 * CELL)))
                        self.action_bar.heavy_unit_button = HeavyElfButton(HEAVY_ELF_ICON, self.action_bar.level,
                                                                           HEAVY_ELF_ICON.get_rect(
                                                                               topright=(125 * CELL, 1 * CELL)))
                        self.action_bar.elf_turret_button.active = True
                        self.state = "elfs"
                if self.state == "pirates":
                    if self.active and self.rect.collidepoint(m_pos) and pygame.mouse.get_pressed()[0]:
                        #print("clicked")
                        self.active = False
                        self.action_bar.level.player.xp -= 5000
                        self.action_bar.light_unit_button.cooldown_bar.kill()
                        self.action_bar.ranged_unit_button.cooldown_bar.kill()
                        self.action_bar.heavy_unit_button.cooldown_bar.kill()
                        self.action_bar.light_unit_button.kill()
                        self.action_bar.ranged_unit_button.kill()
                        self.action_bar.heavy_unit_button.kill()
                        self.action_bar.light_unit_button = LightWarriorButton(LIGHT_WARRIOR_ICON, self.action_bar.level,
                                                                               LIGHT_WARRIOR_ICON.get_rect(
                                                                                   topright=(105 * CELL, 1 * CELL)))
                        self.action_bar.ranged_unit_button = RangedWarriorButton(RANGED_WARRIOR_ICON, self.action_bar.level,
                                                                                 RANGED_WARRIOR_ICON.get_rect(
                                                                                     topright=(115 * CELL, 1 * CELL)))
                        self.action_bar.heavy_unit_button = HeavyWarriorButton(HEAVY_WARRIOR_ICON, self.action_bar.level,
                                                                               HEAVY_WARRIOR_ICON.get_rect(
                                                                                   topright=(125 * CELL, 1 * CELL)))
                        self.action_bar.warrior_turret_button.active = True
                        self.state = "warriors"

            if not self.active and not self.rect.collidepoint(m_pos) and pygame.mouse.get_pressed()[0]:
                self.active = True

    def update(self, dt):
        if self.action_bar.level.player.xp >= 5000:
            self.active = True
        else:
            self.active = False
        self.check_click()
        if self.active:
            self.image.set_alpha(255)
        else:
            self.image.set_alpha(128)
        #print(self.active)
        #print(self.state)


class PirateTurret(pygame.sprite.Sprite):
    def __init__(self, level, topleft):
        super().__init__()
        self.level = level
        self.image = PLAYER_PIRATE_TURRET
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
                cannonball = PirateCannonBall(self, self.angle)

    def sell(self):
        self.level.player.money += self.price / 2
        self.kill()

    def update(self, dt):
        self.enemies = [sprite for sprite in self.level.ai_sprites if sprite is not self.level.ai]
        self.shoot()


class WarriorTurret(pygame.sprite.Sprite):
    def __init__(self, level, topleft):
        super().__init__()
        self.image = PLAYER_WARRIOR_TURRET
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
                cannonball = WarriorCannonBall(self, self.angle)

    def sell(self):
        self.level.player.money += self.price / 2
        self.kill()

    def update(self, dt):
        self.enemies = [sprite for sprite in self.level.ai_sprites if sprite is not self.level.ai]
        self.shoot()


class HealthBar(pygame.sprite.Sprite):
    def __init__(self, unit, position, x, y):
        super().__init__()
        self.unit = unit
        self.position = position
        self.image = pygame.Surface((80, 3))
        self.topleft = self.unit.rect.topleft
        self.rect = self.image.get_rect(topleft=self.topleft)
        self.max = self.unit.health
        #   self.rect.left = x - 10
        #   self.rect.centery = y
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



class ElfTurret(pygame.sprite.Sprite):
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
                cannonball = ElfCannonBall(self, self.angle)

    def sell(self):
        self.level.player.money += self.price / 2
        self.kill()

    def update(self, dt):
        self.enemies = [sprite for sprite in self.level.ai_sprites if sprite is not self.level.ai]
        self.shoot()


class TurretButton(pygame.sprite.Sprite):
    def __init__(self, image, level, rect, race="", active=False, price=0):
        super().__init__()
        self.image = image
        self.rect = rect
        self.race = race
        self.price = price
        self.level = level
        self.level.all_sprites.add(self)
        self.turret = None
        self.level.all_sprites.add(self)
        self.tower1 = AvailableTurretSpot(self.level, 55, 270, 40, 40)
        self.tower2 = AvailableTurretSpot(self.level, 87, 295, 40, 40)
        self.tower3 = AvailableTurretSpot(self.level, 45, 350, 40, 40)
        self.tower4 = AvailableTurretSpot(self.level, 0, 330, 40, 40)
        # c'est ici que les cadre vert apparaissent
        # ducoup faut faire un systeme de upgrade pour qu'ils apparaissent
        self.towers = {self.tower1: "available", self.tower2: "unavailable", self.tower3: "unavailable",
                       self.tower4: "unavailable"}

        self.is_clicked = False
        self.active = active

    def check_click_to_unlock(self):
        for key, value in self.towers.items():
            if value == "unavailable":
                self.towers[key] = "available"
                #TODO : changer le prix de la tourelle
                break
        

    def check_click(self):
        m_pos = game.mouse.get_pos()
        if not self.is_clicked and (self.rect.collidepoint(m_pos) and game.mouse.get_pressed()[0]):
            self.is_clicked = True
            return
        if self.is_clicked and (self.tower1.rect.collidepoint(m_pos) and game.mouse.get_pressed()[0]):
            if self.towers[self.tower1] == "available":
                if self.race == "pirate":
                    if self.level.player.money >= self.price:
                        self.level.player.money -= self.price
                        turret = PirateTurret(self.level, self.tower1.rect.topleft)
                        self.tower1.set_turret(turret)
                        self.towers[self.tower1] = "unavailable"
                elif self.race == "warrior":
                    if self.level.player.money >= self.price:
                        self.level.player.money -= self.price
                        turret = WarriorTurret(self.level, self.tower1.rect.topleft)
                        self.tower1.set_turret(turret)
                        self.towers[self.tower1] = "unavailable"
                elif self.race == "elf":
                    if self.level.player.money >= self.price:
                        self.level.player.money -= self.price
                        turret = ElfTurret(self.level, self.tower1.rect.topleft)
                        self.tower1.set_turret(turret)
                        self.towers[self.tower1] = "unavailable"

            self.is_clicked = False
        if self.is_clicked and (self.tower2.rect.collidepoint(m_pos) and game.mouse.get_pressed()[0]):
            if self.towers[self.tower2] == "available":
                if self.race == "pirate":
                    if self.level.player.money >= self.price:
                        turret = PirateTurret(self.level, self.tower2.rect.topleft)
                        self.tower2.set_turret(turret)
                        self.towers[self.tower2] = "unavailable"
                elif self.race == "warrior":
                    if self.level.player.money >= self.price:
                        turret = WarriorTurret(self.level, self.tower2.rect.topleft)
                        self.tower2.set_turret(turret)
                        self.towers[self.tower2] = "unavailable"
                elif self.race == "elf":
                    if self.level.player.money >= self.price:
                        turret = ElfTurret(self.level, self.tower2.rect.topleft)
                        self.tower2.set_turret(turret)
                        self.towers[self.tower2] = "unavailable"


            self.is_clicked = False
        if self.is_clicked and (self.tower3.rect.collidepoint(m_pos) and game.mouse.get_pressed()[0]):
            if self.towers[self.tower3] == "available":
                if self.race == "pirate":
                    if self.level.player.money >= self.price:
                        turret = PirateTurret(self.level, self.tower3.rect.topleft)
                        self.tower3.set_turret(turret)
                        self.towers[self.tower3] = "unavailable"
                elif self.race == "warrior":
                    if self.level.player.money >= self.price:
                        turret = WarriorTurret(self.level, self.tower3.rect.topleft)
                        self.tower3.set_turret(turret)
                        self.towers[self.tower3] = "unavailable"
                elif self.race == "elf":
                    if self.level.player.money >= self.price:
                        turret = ElfTurret(self.level, self.tower3.rect.topleft)
                        self.tower3.set_turret(turret)
                        self.towers[self.tower3] = "unavailable"
            self.is_clicked = False
        if self.is_clicked and (self.tower4.rect.collidepoint(m_pos) and game.mouse.get_pressed()[0]):
            if self.towers[self.tower4] == "available":
                if self.race == "pirate":
                    turret = PirateTurret(self.level, self.tower4.rect.topleft)
                    self.tower4.set_turret(turret)
                elif self.race == "warrior":
                    turret = WarriorTurret(self.level, self.tower4.rect.topleft)
                    self.tower4.set_turret(turret)
                elif self.race == "elf":
                    turret = ElfTurret(self.level, self.tower4.rect.topleft)
                    self.tower4.set_turret(turret)
            self.towers[self.tower4] = "unavailable"
            self.is_clicked = False
        elif self.is_clicked and not self.rect.collidepoint(m_pos) and game.mouse.get_pressed()[0]:
            self.check_click_to_unlock()
            self.is_clicked = False

    def update(self, dt):
        if not self.active:
            self.image.set_alpha(100)
        elif self.active:
            new_mouse_pos = game.mouse.get_pos()
            self.check_click()
            if self.is_clicked:
                self.image.set_alpha(200)
                for key, value in self.towers.items():
                    if value == "available":
                        key.set_visible()
            else:
                self.image.set_alpha(255)
                for tower in self.towers.keys():
                    tower.set_invisible()




class AvailableTurretSpot(pygame.sprite.Sprite):
    def __init__(self, level, x_pos, y_pos, width, height):
        super().__init__()
        self.turret = None
        self.level = level
        self.image = pygame.Surface((width, height))
        self.image.fill("Green")
        self.image.set_alpha(0)
        self.rect = self.image.get_rect(topleft=(x_pos, y_pos))
        self.level.all_sprites.add(self)

    def set_turret(self, turret):
        self.turret = turret

    def set_visible(self):
        self.image.set_alpha(128)

    def set_invisible(self):
        self.image.set_alpha(0)


class PirateTurretButton(TurretButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, race="pirate", active=True, price=400)

class UnlockTurretPlacemant(TurretButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, race="", active=True, price=400)

class WarriorTurretButton(TurretButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, race="warrior", price=1500)


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
        if self.rect.x > self.turret.range_point[0] or self.rect.y > self.turret.range_point[1]:
            self.kill()
        enemy_collision = game.sprite.spritecollide(self, self.turret.enemies, False)
        if enemy_collision:
            enemy_collision[0].health -= self.damage
            self.kill()

        self.x += self.dx * dt
        self.y += self.dy * dt
        #print(self.x, self.y)
        self.rect.centerx = self.x
        self.rect.centery = self.y


class PirateCannonBall(CannonBall):
    def __init__(self, turret, angle):
        super().__init__(turret, PIRATE_CANNONBALL, angle, 8, 250)


class WarriorCannonBall(CannonBall):
    def __init__(self, turret, angle):
        super().__init__(turret, WARRIOR_CANNONBALL, angle, 10, 280)


class ElfCannonBall(CannonBall):
    def __init__(self, turret, angle):
        super().__init__(turret, ELF_CANNONBALL, angle, 17, 340)


class ElfTurretButton(TurretButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, race="elf", price=2400)


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

            #   print("Collision")
            self.idle = False
            self.attacking = True
            self.walking = False
            if self.current == 6:
                closest_enemy = self.enemy_collisions[0]
                closest_enemy.health -= (self.damage + 2) / (closest_enemy.defense + 2) * randrange(10, 13)
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
            #   print("Collision")
            self.idle = False
            self.attacking = True
            self.walking = False
            if self.current == 6:
                closest_enemy = self.enemy_collisions[0]
                closest_enemy.health -= (self.damage + 2) / (closest_enemy.defense + 2) * randrange(10, 13)
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

            #   print("Collision")
            self.idle = False
            self.attacking = True
            self.walking = False
            if self.current == 6:
                closest_enemy = self.enemy_collisions[0]
                closest_enemy.health -= (self.damage + 2) / (closest_enemy.defense + 2) * randrange(10, 13)
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
        super().__init__(level, ENEMY_LIGHT_PIRATE_WALKING, ENEMY_LIGHT_PIRATE_ATTACKING, ENEMY_LIGHT_PIRATE_IDLE, 100,
                         10, 10, 60)


class EnemyHeavyPirate(EnemyCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_HEAVY_PIRATE_WALKING, ENEMY_HEAVY_PIRATE_ATTACKING, ENEMY_HEAVY_PIRATE_IDLE, 160,
                         8, 15, 40)


class EnemyRangedPirate(EnemyRangedCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_RANGED_PIRATE_WALKING, ENEMY_RANGED_PIRATE_ATTACKING, ENEMY_RANGED_PIRATE_IDLE,
                         80, 15, 8, 50, 3)


class EnemyLightWarrior(EnemyCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_LIGHT_WARRIOR_WALKING, ENEMY_LIGHT_WARRIOR_ATTACKING, ENEMY_LIGHT_WARRIOR_IDLE,
                         130, 13, 15, 65)


class EnemyHeavyWarrior(EnemyCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_HEAVY_WARRIOR_WALKING, ENEMY_HEAVY_WARRIOR_ATTACKING, ENEMY_HEAVY_WARRIOR_IDLE,
                         190, 11, 20, 40)


class EnemyRangedWarrior(EnemyRangedCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_RANGED_WARRIOR_WALKING, ENEMY_RANGED_WARRIOR_ATTACKING,
                         ENEMY_RANGED_WARRIOR_IDLE, 100, 18, 10, 55, 3)


class EnemyLightElf(EnemyCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_LIGHT_ELF_WALKING, ENEMY_LIGHT_ELF_ATTACKING, ENEMY_LIGHT_ELF_IDLE, 150, 18,
                         20, 70)


class EnemyHeavyElf(EnemyCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_HEAVY_ELF_WALKING, ENEMY_HEAVY_ELF_ATTACKING, ENEMY_HEAVY_ELF_IDLE, 240, 14,
                         28, 44)


class EnemyRangedElf(EnemyRangedCombatUnit):
    def __init__(self, level):
        super().__init__(level, ENEMY_RANGED_ELF_WALKING, ENEMY_RANGED_ELF_ATTACKING, ENEMY_RANGED_ELF_IDLE, 130, 23,
                         14, 60, 3)


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
                closest_enemy.health -= (self.damage + 2) / (closest_enemy.defense + 2) * randrange(10, 13)
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


class PlayerRangedPirate(PlayerRangedCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_RANGED_PIRATE_WALKING, PLAYER_RANGED_PIRATE_ATTACKING, PLAYER_RANGED_PIRATE_IDLE,
                         80, 15, 8, 50, 3)


class PlayerLightPirate(PlayerCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_LIGHT_PIRATE_WALKING, PLAYER_LIGHT_PIRATE_ATTACKING, PLAYER_LIGHT_PIRATE_IDLE,
                         100, 10, 10, 60)


class PlayerHeavyPirate(PlayerCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_HEAVY_PIRATE_WALKING, PLAYER_HEAVY_PIRATE_ATTACKING, PLAYER_HEAVY_PIRATE_IDLE,
                         160, 8, 15, 40)


class PlayerLightWarrior(PlayerCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_LIGHT_WARRIOR_WALIKNG, PLAYER_LIGHT_WARRIOR_ATTACKING, PLAYER_LIGHT_WARRIOR_IDLE,
                         130, 13, 15, 65)


class PlayerHeavyWarrior(PlayerCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_HEAVY_WARRIOR_WALIKNG, PLAYER_HEAVY_WARRIOR_ATTACKING, PLAYER_HEAVY_WARRIOR_IDLE,
                         190, 11, 20, 40)


class PlayerRangedWarrior(PlayerRangedCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_RANGED_WARRIOR_WALIKNG, PLAYER_RANGED_WARRIOR_ATTACKING,
                         PLAYER_RANGED_WARRIOR_IDLE, 100, 18, 10, 55, 3)


class PlayerLightElf(PlayerCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_LIGHT_ELF_WALKING, PLAYER_LIGHT_ELF_ATTACKING, PLAYER_LIGHT_ELF_IDLE, 150, 18,
                         20, 70)


class PlayerHeavyElf(PlayerCloseCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_HEAVY_ELF_WALKING, PLAYER_HEAVY_ELF_ATTACKING, PLAYER_HEAVY_ELF_IDLE, 240, 14,
                         28, 44)


class PlayerRangedElf(PlayerRangedCombatUnit):
    def __init__(self, level):
        super().__init__(level, PLAYER_RANGED_ELF_WALKING, PLAYER_RANGED_ELF_ATTACKING, PLAYER_RANGED_ELF_IDLE, 130, 23,
                         14, 60, 3)


class UnitButton(pygame.sprite.Sprite):
    def __init__(self, image, level, rect, cooldown=1000):
        super().__init__()
        self.level = level
        self.image = image
        self.rect = rect
        self.active = True
        self.lastupdate = 0
        self.cooldown = cooldown
        self.cooldown_bar = CooldownBar(self, self.level)
        self.now = 0
        self.race = None
        self.unit_type = None
        self.level.all_sprites.add(self)

    def click(self):
        m_pos = pygame.mouse.get_pos()
        self.now = pygame.time.get_ticks()
        if self.active and self.rect.collidepoint(m_pos) and pygame.mouse.get_pressed()[0]:
            if self.race == "pirate":
                if self.unit_type == "light":
                    if self.level.player.money >= 50:
                        self.level.player.money -= 50
                        player_light_pirate = PlayerLightPirate(self.level)
                elif self.unit_type == "heavy":
                    if self.level.player.money >= 90:
                        self.level.player.money -= 90
                        player_heavy_pirate = PlayerHeavyPirate(self.level)
                elif self.unit_type == "ranged":
                    if self.level.player.money >= 70:
                        self.level.player.money -= 70
                        player_ranged_pirate = PlayerRangedPirate(self.level)

            if self.race == "warrior":
                if self.unit_type == "light":
                    if self.level.player.money >= 90:
                        self.level.player.money -= 90
                    player_light_warrior = PlayerLightWarrior(self.level)
                elif self.unit_type == "heavy":
                    if self.level.player.money >= 150:
                        self.level.player.money -= 150
                        player_heavy_warrior = PlayerHeavyWarrior(self.level)
                elif self.unit_type == "ranged":
                    if self.level.player.money >= 120:
                        self.level.player.money -= 120
                        player_ranged_warrior = PlayerRangedWarrior(self.level)

            if self.race == "elf":
                if self.unit_type == "light":
                    if self.level.player.money >= 150:
                        self.level.player.money -= 150
                        player_light_elf = PlayerLightElf(self.level)
                if self.unit_type == "heavy":
                    if self.level.player.money >= 240:
                        self.level.player.money -= 240
                        player_heavy_elf = PlayerHeavyElf(self.level)
                if self.unit_type == "ranged":
                    if self.level.player.money >= 180:
                        self.level.player.money -= 180
                        player_ranged_elf = PlayerRangedElf(self.level)

            self.lastupdate = self.now
            self.active = False
        if self.now - self.lastupdate >= self.cooldown or self.cooldown == 0:
            self.active = True

    def update(self, dt):
        self.click()
        if self.active:
            self.image.set_alpha(255)
        else:
            self.image.set_alpha(128)


class RangedPirateButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=2000)
        self.race = "pirate"
        self.unit_type = "ranged"


class HeavyPirateButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=3500)
        self.race = "pirate"
        self.unit_type = "heavy"


class LightPirateButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=1500)
        self.race = "pirate"
        self.unit_type = "light"


class LightWarriorButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=1800)
        self.race = "warrior"
        self.unit_type = "light"


class RangedWarriorButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=2200)
        self.race = "warrior"
        self.unit_type = "ranged"


class HeavyWarriorButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=4000)
        self.race = "warrior"
        self.unit_type = "heavy"


class LightElfButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=2100)
        self.race = "elf"
        self.unit_type = "light"


class HeavyElfButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=4500)
        self.race = "elf"
        self.unit_type = "heavy"


class RangedElfButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=2600)
        self.race = "elf"
        self.unit_type = "ranged"


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
