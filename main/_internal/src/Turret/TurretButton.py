from src.settings import *
from random import randrange
import pygame
from random import randrange
from src.Turret.CannonBall import *
from src.Button.CooldownBar import CooldownBar
from src.Turret.CannonBall import CannonBall1, CannonBall2, CannonBall3, CannonBall4, CannonBall5, CannonBall6

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
                    if self.race == "satyrs":
                        if isinstance(self, TurretButton1):
                            turret = Turret(self.level, tower.rect.topleft, 600, 48, 44, 400, PLAYER_SATYR_TURRET)
                        elif isinstance(self, TurretButton2):
                            turret = Turret(self.level, tower.rect.topleft, 500, 55, 48, 1250, PLAYER_GOLEM_TURRET)
                        elif isinstance(self, TurretButton3):
                            turret = Turret(self.level, tower.rect.topleft, 400, 68, 52, 2500, PLAYER_ELF_TURRET)
                    elif self.race == "golems":
                        if isinstance(self, TurretButton4):
                            turret = Turret(self.level, tower.rect.topleft, 600, 48, 44, 400, PLAYER_TURRET)
                        elif isinstance(self, TurretButton5):
                            turret = Turret(self.level, tower.rect.topleft, 500, 55, 48, 1250, PLAYER_TURRET1)
                        elif isinstance(self, TurretButton6):
                            turret = Turret(self.level, tower.rect.topleft, 400, 68, 52, 2500, PLAYER_TURRET2)
                    elif self.race == "elfs":
                        if isinstance(self, TurretButton7):
                            turret = Turret(self.level, tower.rect.topleft, 600, 48, 44, 400, PLAYER_TURRET3)
                        elif isinstance(self, TurretButton8):
                            turret = Turret(self.level, tower.rect.topleft, 500, 55, 48, 1250, PLAYER_TURRET4)
                        elif isinstance(self, TurretButton9):
                            turret = Turret(self.level, tower.rect.topleft, 400, 68, 52, 2500, PLAYER_TURRET5)
                    elif self.race == "angel":
                        if isinstance(self, TurretButton10):
                            turret = Turret(self.level, tower.rect.topleft, 600, 48, 44, 400, PLAYER_TURRET6)
                        elif isinstance(self, TurretButton11):
                            turret = Turret(self.level, tower.rect.topleft, 500, 55, 48, 1250, PLAYER_TURRET7)
                        elif isinstance(self, TurretButton12):
                            turret = Turret(self.level, tower.rect.topleft, 400, 68, 52, 2500, PLAYER_TURRET8)
                    elif self.race == "wraith":
                        if isinstance(self, TurretButton13):
                            turret = Turret(self.level, tower.rect.topleft, 600, 48, 44, 400, PLAYER_TURRET9)
                        elif isinstance(self, TurretButton14):
                            turret = Turret(self.level, tower.rect.topleft, 500, 55, 48, 1250, PLAYER_TURRET10)
                        elif isinstance(self, TurretButton15):
                            turret = Turret(self.level, tower.rect.topleft, 400, 68, 52, 2500, PLAYER_TURRET11)
                    elif self.race == "villager":
                        if isinstance(self, TurretButton16):
                            turret = Turret(self.level, tower.rect.topleft, 600, 48, 44, 400, PLAYER_TURRET12)
                        elif isinstance(self, TurretButton17):
                            turret = Turret(self.level, tower.rect.topleft, 500, 55, 48, 1250, PLAYER_TURRET13)
                        elif isinstance(self, TurretButton18):
                            turret = Turret(self.level, tower.rect.topleft, 400, 68, 52, 2500, PLAYER_TURRET14)
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
    def __init__(self, image, sprite_group, rect, price,race):
        super().__init__(image, sprite_group, rect,active=True,price=price,race=race)

class TurretButton4(TurretButton):
    def __init__(self, image, sprite_group, rect, price):
        super().__init__(image, sprite_group, rect,active=True,price=price)
        self.race = "golems"
        self.unit_type = "turret4"

class TurretButton5(TurretButton):
    def __init__(self, image, sprite_group, rect, price):
        super().__init__(image, sprite_group, rect,active=True,price=price)
        self.race = "golems"
        self.unit_type = "turret5"

class TurretButton6(TurretButton):
    def __init__(self, image, sprite_group, rect, price):
        super().__init__(image, sprite_group, rect,active=True,price=price)
        self.race = "golems"
        self.unit_type = "turret6"


class TurretButton7(TurretButton):
    def __init__(self, image, sprite_group, rect, price):
        super().__init__(image, sprite_group, rect,active=True,price=price)
        self.race = "elfs"
        self.unit_type = "turret7"

class TurretButton8(TurretButton):
    def __init__(self, image, sprite_group, rect, price):
        super().__init__(image, sprite_group, rect,active=True,price=price)
        self.race = "elfs"
        self.unit_type = "turret8"

class TurretButton9(TurretButton):
    def __init__(self, image, sprite_group, rect, price):
        super().__init__(image, sprite_group, rect,active=True,price=price)
        self.race = "elfs"
        self.unit_type = "turret9"


class TurretButton10(TurretButton):
    def __init__(self, image, sprite_group, rect, price):
        super().__init__(image, sprite_group, rect,active=True,price=price)
        self.race = "angel"
        self.unit_type = "turret10"

class TurretButton11(TurretButton):
    def __init__(self, image, sprite_group, rect, price):
        super().__init__(image, sprite_group, rect,active=True,price=price)
        self.race = "angel"
        self.unit_type = "turret11"

class TurretButton12(TurretButton):
    def __init__(self, image, sprite_group, rect, price):
        super().__init__(image, sprite_group, rect,active=True,price=price)
        self.race = "angel"
        self.unit_type = "turret12"


class TurretButton13(TurretButton):
    def __init__(self, image, sprite_group, rect, price):
        super().__init__(image, sprite_group, rect,active=True,price=price)
        self.race = "wraith"
        self.unit_type = "turret13"

class TurretButton14(TurretButton):
    def __init__(self, image, sprite_group, rect, price):
        super().__init__(image, sprite_group, rect,active=True,price=price)
        self.race = "wraith"
        self.unit_type = "turret14"

class TurretButton15(TurretButton):
    def __init__(self, image, sprite_group, rect, price):
        super().__init__(image, sprite_group, rect,active=True,price=price)
        self.race = "wraith"
        self.unit_type = "turret15"


class TurretButton16(TurretButton):
    def __init__(self, image, sprite_group, rect, price):
        super().__init__(image, sprite_group, rect,active=True,price=price)
        self.race = "villager"
        self.unit_type = "turret16"

class TurretButton17(TurretButton):
    def __init__(self, image, sprite_group, rect, price):
        super().__init__(image, sprite_group, rect,active=True,price=price)
        self.race = "villager"
        self.unit_type = "turret17"

class TurretButton18(TurretButton):
    def __init__(self, image, sprite_group, rect, price):
        super().__init__(image, sprite_group, rect,active=True,price=price)
        self.race = "villager"
        self.unit_type = "turret18"

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
    def __init__(self, level, topleft, speed, range_X, range_Y, price, image):
        super().__init__()
        self.level = level
        self.image = image
        self.rect = self.image.get_rect(topleft=topleft)
        self.range_point_X = range_X * CELL
        self.range_point_Y = range_Y * CELL
        self.shooting_speed = speed
        self.price = price
        self.lastshot = 0
        self.enemies = [sprite for sprite in self.level.ai_sprites if sprite is not self.level.ai]
        self.level.all_sprites.add(self)

        self.states = {
            1: {"damage": 40},
            2: {"damage": 100},
            3: {"damage": 250}
        }
        self.current_state = 1

    def change_state(self, new_state):
        if new_state in self.states:
            self.current_state = new_state

    def shoot(self):
        x_dist = self.range_point_X - self.rect.centerx
        y_dist = self.range_point_Y - self.rect.centery
        self.angle = math.atan2(y_dist, x_dist)
        now = pygame.time.get_ticks()
        if self.enemies and self.enemies[0].rect.midbottom[0] < 48 * CELL:
            if now - self.lastshot > self.shooting_speed:
                self.lastshot = now
                x_dist = self.enemies[0].rect.midbottom[0] - self.rect.centerx
                y_dist = self.enemies[0].rect.midbottom[1] - self.rect.centery
                self.angle = math.atan2(y_dist, x_dist)

                if self.level.player.state == "satyrs":
                    cannonball = CannonBall1(self, self.angle, 100, 250)
                elif self.level.player.state == "golems":
                    cannonball = CannonBall2(self, self.angle, 200, 250)
                elif self.level.player.state == "elfs":
                    cannonball = CannonBall3(self, self.angle, 300, 250)
                elif self.level.player.state == "angel":
                    cannonball = CannonBall4(self, self.angle, 400, 250)
                elif self.level.player.state == "wraith":
                    cannonball = CannonBall5(self, self.angle, 500, 250)
                elif self.level.player.state == "villager":
                    cannonball = CannonBall6(self, self.angle, 600, 250)

                self.level.all_sprites.add(cannonball)

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