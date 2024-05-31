from src.settings import *
from random import randrange
import pygame
from random import randrange
from src.Button.CooldownBar import CooldownBar
from src.sprites import *
from src.Special.Special import *

class UnitButton(pygame.sprite.Sprite):
    def __init__(self, image, level, rect, cooldown=1000, unlocked=True):
        super().__init__()
        self.level = level
        self.image = image
        self.rect = rect
        self.active = True
        self.unlocked = unlocked
        self.lastupdate = 0
        self.cooldown = cooldown
        self.cooldown_bar = CooldownBar(self, self.level)
        self.now = 0
        self.race = None
        self.unit_type = None
        self.level.all_sprites.add(self)
        print(self.active)

    def click(self):
        m_pos = pygame.mouse.get_pos()
        self.now = pygame.time.get_ticks()
        if self.active and self.rect.collidepoint(m_pos) and pygame.mouse.get_pressed()[0]:
            print(self.active)
            if self.race == "satyr":
                if self.unit_type == "light":
                    if self.level.player.money >= 50:
                        self.level.player.money -= 50
                        player_light_satyr = PlayerLightPirate(self.level)
                elif self.unit_type == "heavy":
                    if self.level.player.money >= 90:
                        self.level.player.money -= 90
                        player_heavy_satyr = PlayerHeavyPirate(self.level)
                elif self.unit_type == "ranged":
                    if self.level.player.money >= 70:
                        self.level.player.money -= 70
                        player_ranged_satyr = PlayerRangedPirate(self.level)
                elif self.unit_type == "hero" and self.unlocked:
                    if self.level.player.money >= 110:
                        self.level.player.money -= 110
                        player_hero_satyr = PlayerHeroPirate(self.level)
                elif self.unit_type == "special":
                    if self.level.player.money >= 70:
                        self.level.player.money -= 70
                        for _ in range(15):
                            special_satyr = Special(self.level)
                            special_satyr.rect.topleft = (randrange(0, SCREEN_WIDTH - special_satyr.rect.width), 0)
                            self.level.all_sprites.add(special_satyr)
                            self.level.player_sprites.add(special_satyr)
                elif self.unit_type == "hero" and not self.unlocked:
                    if self.level.player.money >= 450:
                        self.level.player.money -= 450
                        self.unlocked = True

            if self.race == "golem":
                if self.unit_type == "light":
                    if self.level.player.money >= 90:
                        self.level.player.money -= 90
                    player_light_golem = PlayerLightWarrior(self.level)
                elif self.unit_type == "heavy":
                    if self.level.player.money >= 150:
                        self.level.player.money -= 150
                        player_heavy_golem = PlayerHeavyWarrior(self.level)
                elif self.unit_type == "ranged":
                    if self.level.player.money >= 120:
                        self.level.player.money -= 120
                        player_ranged_golem = PlayerRangedWarrior(self.level)
                elif self.unit_type == "hero" and self.unlocked == True:
                    if self.level.player.money >= 180:
                        self.level.player.money -= 180
                        player_hero_golem = PlayerHeroWarrior(self.level)
                elif self.unit_type == "special":
                    if self.level.player.money >= 70:
                        self.level.player.money -= 70
                        for _ in range(15):
                            special_satyr = Special1(self.level)
                            special_satyr.rect.topleft = (randrange(0, SCREEN_WIDTH - special_satyr.rect.width), 0)
                            self.level.all_sprites.add(special_satyr)
                            self.level.player_sprites.add(special_satyr)
                
                elif self.unit_type == "hero" and self.unlocked == False:
                     if self.level.player.money >= 450:
                        self.level.player.money -= 450
                        self.unlocked = True

            if self.race == "elf":
                if self.unit_type == "light":
                    if self.level.player.money >= 150:
                        self.level.player.money -= 150
                        player_light_elf = PlayerLightFairy(self.level)
                if self.unit_type == "heavy":
                    if self.level.player.money >= 240:
                        self.level.player.money -= 240
                        player_heavy_elf = PlayerHeavyFairy(self.level)
                if self.unit_type == "ranged":
                    if self.level.player.money >= 180:
                        self.level.player.money -= 180
                        player_ranged_elf = PlayerRangedFairy(self.level)
                if self.unit_type == "hero" and self.unlocked == True:
                    if self.level.player.money >= 240:
                        self.level.player.money -= 240
                        player_heavy_elf = PlayerHeroFairy(self.level)
                elif self.unit_type == "special":
                    if self.level.player.money >= 70:
                        self.level.player.money -= 70
                        for _ in range(15):
                            special_satyr = Special2(self.level)
                            special_satyr.rect.topleft = (randrange(0, SCREEN_WIDTH - special_satyr.rect.width), 0)
                            self.level.all_sprites.add(special_satyr)
                            self.level.player_sprites.add(special_satyr)
                
                elif self.unit_type == "hero" and self.unlocked == False:
                     if self.level.player.money >= 450:
                        self.level.player.money -= 450
                        self.unlocked = True


            if self.race == "angel":
                if self.unit_type == "light":
                    if self.level.player.money >= 150:
                        self.level.player.money -= 150
                        player_light_angel = PlayerLightAngel(self.level)
                if self.unit_type == "heavy":
                    if self.level.player.money >= 240:
                        self.level.player.money -= 240
                        player_heavy_angel = PlayerHeavyAngel(self.level)
                if self.unit_type == "ranged":
                    if self.level.player.money >= 180:
                        self.level.player.money -= 180
                        player_ranged_angel = PlayerRangedAngel(self.level)
                if self.unit_type == "hero" and self.unlocked == True:
                    if self.level.player.money >= 240:
                        self.level.player.money -= 240
                        player_hero_angel = PlayerHeroAngel(self.level)
                elif self.unit_type == "special":
                    if self.level.player.money >= 70:
                        self.level.player.money -= 70
                        for _ in range(15):
                            special_satyr = Special3(self.level)
                            special_satyr.rect.topleft = (randrange(0, SCREEN_WIDTH - special_satyr.rect.width), 0)
                            self.level.all_sprites.add(special_satyr)
                            self.level.player_sprites.add(special_satyr)
                
                elif self.unit_type == "hero" and self.unlocked == False:
                     if self.level.player.money >= 450:
                        self.level.player.money -= 450
                        self.unlocked = True

            if self.race == "wraith":
                if self.unit_type == "light":
                    if self.level.player.money >= 150:
                        self.level.player.money -= 150
                        player_light_wraith = PlayerLightWraith(self.level)
                if self.unit_type == "heavy":
                    if self.level.player.money >= 240:
                        self.level.player.money -= 240
                        player_heavy_wraith = PlayerHeavyWraith(self.level)
                if self.unit_type == "ranged":
                    if self.level.player.money >= 180:
                        self.level.player.money -= 180
                        player_ranged_wraith = PlayerRangedWraith(self.level)
                if self.unit_type == "hero" and self.unlocked == True:
                    if self.level.player.money >= 240:
                        self.level.player.money -= 240
                        player_hero_wraith = PlayerHeroWraith(self.level)
                elif self.unit_type == "special":
                    if self.level.player.money >= 70:
                        self.level.player.money -= 70
                        for _ in range(15):
                            special_satyr = Special4(self.level)
                            special_satyr.rect.topleft = (randrange(0, SCREEN_WIDTH - special_satyr.rect.width), 0)
                            self.level.all_sprites.add(special_satyr)
                            self.level.player_sprites.add(special_satyr)
                
                elif self.unit_type == "hero" and self.unlocked == False:
                     if self.level.player.money >= 450:
                        self.level.player.money -= 450
                        self.unlocked = True

            if self.race == "villager":
                if self.unit_type == "light":
                    if self.level.player.money >= 150:
                        self.level.player.money -= 150
                        player_light_villager = PlayerLightVillager(self.level)
                if self.unit_type == "heavy":
                    if self.level.player.money >= 240:
                        self.level.player.money -= 240
                        player_heavy_villager = PlayerHeavyVillager(self.level)
                if self.unit_type == "ranged":
                    if self.level.player.money >= 180:
                        self.level.player.money -= 180
                        player_ranged_villager = PlayerRangedVillager(self.level)
                if self.unit_type == "hero" and self.unlocked == True:
                    if self.level.player.money >= 240:
                        self.level.player.money -= 240
                        player_hero_villager = PlayerHeroVillager(self.level)
                elif self.unit_type == "special":
                    if self.level.player.money >= 70:
                        self.level.player.money -= 70
                        for _ in range(15):
                            special_satyr = Special5(self.level)
                            special_satyr.rect.topleft = (randrange(0, SCREEN_WIDTH - special_satyr.rect.width), 0)
                            self.level.all_sprites.add(special_satyr)
                            self.level.player_sprites.add(special_satyr)
                
                elif self.unit_type == "hero" and self.unlocked == False:
                     if self.level.player.money >= 450:
                        self.level.player.money -= 450
                        self.unlocked = True

            self.lastupdate = self.now
            self.active = False
        if self.unlocked:
            if self.now - self.lastupdate >= self.cooldown or self.cooldown == 0:
                self.active = True

    def update(self, dt):
        self.click()
        if self.active and self.unlocked:
            self.image.set_alpha(255)
        else:
            self.image.set_alpha(128)


class RangedPirateButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=2000)
        self.race = "satyr"
        self.unit_type = "ranged"


class HeavyPirateButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=3500)
        self.race = "satyr"
        self.unit_type = "heavy"


class LightPirateButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=1500)
        self.race = "satyr"
        self.unit_type = "light"


class HeroPirateButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=4500, unlocked=False)
        self.race = "satyr"
        self.unit_type = "hero"

class SpecialButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=7000)
        self.race = "satyr"
        self.unit_type = "special"

class LightWarriorButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=1800)
        self.race = "golem"
        self.unit_type = "light"


class RangedWarriorButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=2200)
        self.race = "golem"
        self.unit_type = "ranged"


class HeavyWarriorButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=4000)
        self.race = "golem"
        self.unit_type = "heavy"

class HeroWarriorButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=4500, unlocked=False)
        self.race = "golem"
        self.unit_type = "hero"

class Special1Button(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=7000)
        self.race = "golem"
        self.unit_type = "special"


class LightFairyButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=2100)
        self.race = "elf"
        self.unit_type = "light"


class HeavyFairyButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=4500)
        self.race = "elf"
        self.unit_type = "heavy"

class HeroFairyButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=4500, unlocked=False)
        self.race = "elf"
        self.unit_type = "hero"

class Special2Button(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=7000)
        self.race = "elf"
        self.unit_type = "special"

class RangedFairyButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=2600)
        self.race = "elf"
        self.unit_type = "ranged"


class LightAngelButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=2100)
        self.race = "angel"
        self.unit_type = "light"

class RangedAngelButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=2600)
        self.race = "angel"
        self.unit_type = "ranged"

class HeavyAngelButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=4500)
        self.race = "angel"
        self.unit_type = "heavy"

class HeroAngelButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=4500, unlocked=False)
        self.race = "angel"
        self.unit_type = "hero"

class Special3Button(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=7000)
        self.race = "angel"
        self.unit_type = "special"

class LightWraithButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=2100)
        self.race = "wraith"
        self.unit_type = "light"

class RangedWraithButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=2600)
        self.race = "wraith"
        self.unit_type = "ranged"

class HeavyWraithButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=4500)
        self.race = "wraith"
        self.unit_type = "heavy"

class HeroWraithButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=4500, unlocked=False)
        self.race = "wraith"
        self.unit_type = "hero"

class Special4Button(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=7000)
        self.race = "wraith"
        self.unit_type = "special"

class LightVillagerButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=2100)
        self.race = "villager"
        self.unit_type = "light"

class RangedVillagerButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=2600)
        self.race = "villager"
        self.unit_type = "ranged"

class HeavyVillagerButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=4500)
        self.race = "villager"
        self.unit_type = "heavy"

class HeroVillagerButton(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=4500, unlocked=False)
        self.race = "villager"
        self.unit_type = "hero"

class Special5Button(UnitButton):
    def __init__(self, image, sprite_group, rect):
        super().__init__(image, sprite_group, rect, cooldown=7000)
        self.race = "villager"
        self.unit_type = "special"

