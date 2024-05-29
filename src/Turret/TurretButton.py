from src.settings import *
from random import randrange
import pygame
from random import randrange
from src.Turret.CannonBall import *

class TurretButton(pygame.sprite.Sprite):
    towers = None
    tower1 = None
    tower2 = None
    tower3 = None
    tower4 = None
    count = 1

    def __init__(self, image, level, rect, race="", active=False, Unclocker=False, price=0):
        super().__init__()
        self.image = image
        self.rect = rect
        self.race = race
        self.price = price
        self.level = level
        self.Unclocker = Unclocker
        self.level.all_sprites.add(self)
        self.turret = None

        if not TurretButton.towers:
            TurretButton.tower1 = AvailableTurretSpot(self.level, 55, 270, 40, 40)
            TurretButton.tower2 = AvailableTurretSpot(self.level, 87, 295, 40, 40)
            TurretButton.tower3 = AvailableTurretSpot(self.level, 45, 350, 40, 40)
            TurretButton.tower4 = AvailableTurretSpot(self.level, 0, 330, 40, 40)

            TurretButton.towers = {
                TurretButton.tower1: "available",
                TurretButton.tower2: "unavailable",
                TurretButton.tower3: "unavailable",
                TurretButton.tower4: "unavailable"
            }

        self.is_clicked = False
        self.active = active

    def check_click_to_unlock(self):
        """Débloque le premier emplacement indisponible si les fonds le permettent."""
        unlocked = False

        if self.level.player.money >= self.price and TurretButton.count < 4:
            for key, value in list(TurretButton.towers.items())[TurretButton.count:]:
                if value == "unavailable":
                    TurretButton.towers[key] = "available"
                    key.set_visible()
                    self.level.player.money -= self.price
                    unlocked = True
                    TurretButton.count += 1
                    break
            if unlocked:
                self.print_tower_status("Towers après déblocage:")

    def check_click(self):
        """Vérifie les clics pour le déblocage et la création des tourelles."""
        m_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]

        if not self.is_clicked and (self.rect.collidepoint(m_pos) and mouse_pressed):
            self.is_clicked = True
            self.print_tower_status("Bouton cliqué, état actuel des tours:")
            return

        for tower, status in TurretButton.towers.items():
            if self.is_clicked and tower.rect.collidepoint(m_pos) and mouse_pressed:
                if status == "available" and self.level.player.money >= self.price:
                    turret = None
                    if self.race == "satyr":
                        if isinstance(self, TurretButton1):
                            turret = Turret(self.level, tower.rect.topleft, 600, 48, 44, 400, PLAYER_SATYR_TURRET)
                        elif isinstance(self, TurretButton2):
                            turret = Turret(self.level, tower.rect.topleft, 500, 55, 48, 1250, PLAYER_GOLEM_TURRET)
                        elif isinstance(self, TurretButton3):
                            turret = Turret(self.level, tower.rect.topleft, 400, 68, 52, 2500, PLAYER_ELF_TURRET)
                    elif self.race == "golem":
                        if isinstance(self, TurretButton1):
                            turret = Turret(self.level, tower.rect.topleft, 600, 48, 44, 400, PLAYER_SATYR_TURRET)
                        elif isinstance(self, TurretButton2):
                            turret = Turret(self.level, tower.rect.topleft, 500, 55, 48, 1250, PLAYER_GOLEM_TURRET)
                        elif isinstance(self, TurretButton3):
                            turret = Turret(self.level, tower.rect.topleft, 400, 68, 52, 2500, PLAYER_ELF_TURRET)
                    elif self.race == "elf":
                        if isinstance(self, TurretButton1):
                            turret = Turret(self.level, tower.rect.topleft, 600, 48, 44, 400, PLAYER_SATYR_TURRET)
                        elif isinstance(self, TurretButton2):
                            turret = Turret(self.level, tower.rect.topleft, 500, 55, 48, 1250, PLAYER_GOLEM_TURRET)
                        elif isinstance(self, TurretButton3):
                            turret = Turret(self.level, tower.rect.topleft, 400, 68, 52, 2500, PLAYER_ELF_TURRET)
                    elif self.race == "angel":
                        if isinstance(self, TurretButton1):
                            turret = Turret(self.level, tower.rect.topleft, 600, 48, 44, 400, PLAYER_SATYR_TURRET)
                        elif isinstance(self, TurretButton2):
                            turret = Turret(self.level, tower.rect.topleft, 500, 55, 48, 1250, PLAYER_GOLEM_TURRET)
                        elif isinstance(self, TurretButton3):
                            turret = Turret(self.level, tower.rect.topleft, 400, 68, 52, 2500, PLAYER_ELF_TURRET)
                    elif self.race == "wrath":
                        if isinstance(self, TurretButton1):
                            turret = Turret(self.level, tower.rect.topleft, 600, 48, 44, 400, PLAYER_SATYR_TURRET)
                        elif isinstance(self, TurretButton2):
                            turret = Turret(self.level, tower.rect.topleft, 500, 55, 48, 1250, PLAYER_GOLEM_TURRET)
                        elif isinstance(self, TurretButton3):
                            turret = Turret(self.level, tower.rect.topleft, 400, 68, 52, 2500, PLAYER_ELF_TURRET)
                    elif self.race == "villager":
                        if isinstance(self, TurretButton1):
                            turret = Turret(self.level, tower.rect.topleft, 600, 48, 44, 400, PLAYER_SATYR_TURRET)
                        elif isinstance(self, TurretButton2):
                            turret = Turret(self.level, tower.rect.topleft, 500, 55, 48, 1250, PLAYER_GOLEM_TURRET)
                        elif isinstance(self, TurretButton3):
                            turret = Turret(self.level, tower.rect.topleft, 400, 68, 52, 2500, PLAYER_ELF_TURRET)
                    if turret:
                        self.level.player.money -= self.price
                        tower.set_turret(turret)
                        TurretButton.towers[tower] = "unavailable"
                self.is_clicked = False
                break

        if self.is_clicked and not self.rect.collidepoint(m_pos) and mouse_pressed:
            if self.Unclocker:
                self.check_click_to_unlock()
            self.is_clicked = False

    def print_tower_status(self, message=""):
        print("-------------------------------------------")
        print(message, TurretButton.towers)
        print("-------------------------------------------")

    def update(self, dt):
        if not self.active:
            self.image.set_alpha(100)
        elif self.active:
            new_mouse_pos = pygame.mouse.get_pos()
            self.check_click()
            if self.is_clicked:
                self.image.set_alpha(200)
                for key, value in TurretButton.towers.items():
                    if value == "available":
                        key.set_visible()
            elif self.Unclocker:
                self.image.set_alpha(255)
                for tower in TurretButton.towers.keys():
                        tower.set_invisible()
            else:
                self.image.set_alpha(255)
                for key, value in TurretButton.towers.items():
                    if value == "unavailable":
                        key.set_invisible()

class TurretButton1(TurretButton):
    def __init__(self, image, sprite_group, rect,price,race):
        super().__init__(image, sprite_group, rect,active=True,price=price,race=race)

class UnlockTurretPlacemant(TurretButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, race="", Unclocker=True, active=True, price=400)


class TurretButton2(TurretButton):
    def __init__(self, image, sprite_group, rect,price,race):
        super().__init__(image, sprite_group, rect,active=True,price=price,race=race)


class TurretButton3(TurretButton):
    def __init__(self, image, sprite_group, rect,price,race):
        super().__init__(image, sprite_group, rect,active=True,price=price,race=race)


class Turret(pygame.sprite.Sprite):
    def __init__(self, level, topleft,speed,range_X,range_Y,price,image):
        super().__init__()
        self.level = level
        self.image = image
        self.rect = self.image.get_rect(topleft=topleft)
        self.range_point_X = range_X * CELL
        self.range_point_Y = range_Y * CELL
        self.shooting_speed=speed
        self.price = price
        self.lastshot = 0
        self.enemies = [sprite for sprite in self.level.ai_sprites if sprite is not self.level.ai]
        self.level.all_sprites.add(self)

    def shoot(self):
        x_dist = self.range_point_X - self.rect.centerx
        y_dist = self.range_point_Y- self.rect.centery
        self.angle = math.atan2(y_dist, x_dist)
        now = game.time.get_ticks()
        if self.enemies and self.enemies[0].rect.midbottom[0] < 48 * CELL:
            if now - self.lastshot > self.shooting_speed:
                self.lastshot = now
                x_dist = self.enemies[0].rect.midbottom[0] - self.rect.centerx
                y_dist = self.enemies[0].rect.midbottom[1] - self.rect.centery
                self.angle = math.atan2(y_dist, x_dist)
                cannonball = CannonBall1(self, self.angle,10,250,)

    def sell(self):
        self.level.player.money += self.price / 2
        self.kill()

    def update(self, dt):
        self.enemies = [sprite for sprite in self.level.ai_sprites if sprite is not self.level.ai]
        self.shoot()



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