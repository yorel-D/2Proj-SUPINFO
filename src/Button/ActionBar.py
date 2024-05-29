from src.settings import *
import pygame
from src.sprites import *
from src.Button.SellButton import SellButton
from src.Button.UpgradeButton import UpgradeButton
from src.Button.UnitButton import *
from src.Turret.TurretButton import *

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
        self.turret_button1 = TurretButton1(SATYR_TURRET_ICON, self.level,
                                                      SATYR_TURRET_ICON.get_rect(topright=(105 * CELL, 9 * CELL)),
                                                      price=400, race="satyr")
        self.turret_button2 = TurretButton2(GOLEM_TURRET_ICON, self.level,
                                                       GOLEM_TURRET_ICON.get_rect(topright=(115 * CELL, 9 * CELL)),
                                                       price=2000, race="satyr")
        self.turret_button3 = TurretButton3(ELF_TURRET_ICON, self.level,
                                                   ELF_TURRET_ICON.get_rect(topright=(125 * CELL, 9 * CELL)),
                                                   price=4000, race="satyr")

        self.sell_button = SellButton(self.level,self.turret_button1,self.turret_button2,self.turret_button3)
        self.upgrade_button = UpgradeButton(self)
        if self.state == "satyrs":
            self.light_unit_button = LightPirateButton(LIGHT_SATYR_ICON, self.level,
                                                       LIGHT_SATYR_ICON.get_rect(topright=(95 * CELL, 1 * CELL)))
            self.ranged_unit_button = RangedPirateButton(RANGED_SATYR_ICON, self.level,
                                                         RANGED_SATYR_ICON.get_rect(topright=(105 * CELL, 1 * CELL)))
            self.heavy_unit_button = HeavyPirateButton(HEAVY_SATYR_ICON, self.level,
                                                       HEAVY_SATYR_ICON.get_rect(topright=(115 * CELL, 1 * CELL)))
            self.hero_unit_button = HeroPirateButton(HERO_SATYR_ICON, self.level,
                                                       HERO_SATYR_ICON.get_rect(topright=(125 * CELL, 1 * CELL)))
            self.special_button = SpecialButton(SPECIAL_ICON, self.level,
                                                       SPECIAL_ICON.get_rect(topright=(85 * CELL, 5* CELL)))
        elif self.state == "golems":
            self.light_unit_button = LightWarriorButton(LIGHT_GOLEM_ICON, self.level,
                                                        LIGHT_GOLEM_ICON.get_rect(topright=(95 * CELL, 1 * CELL)))
            self.ranged_unit_button = RangedWarriorButton(RANGED_GOLEM_ICON, self.level,
                                                          RANGED_GOLEM_ICON.get_rect(topright=(105 * CELL, 1 * CELL)))
            self.heavy_unit_button = HeavyWarriorButton(HEAVY_GOLEM_ICON, self.level,
                                                        HEAVY_GOLEM_ICON.get_rect(topright=(115 * CELL, 1 * CELL)))
            self.hero_unit_button = HeroWarriorButton(HERO_GOLEM_ICON, self.level,
                                                       HERO_GOLEM_ICON.get_rect(topright=(125 * CELL, 1 * CELL)))
            self.special_button = Special1Button(SPECIAL1_ICON, self.level,
                                                       SPECIAL1_ICON.get_rect(topright=(85 * CELL, 5* CELL)))
        elif self.state == "elfs":
            self.light_unit_button = LightFairyButton(LIGHT_ELF_ICON, self.level,
                                                    LIGHT_ELF_ICON.get_rect(topright=(95 * CELL, 1 * CELL)))
            self.ranged_unit_button = RangedFairyButton(RANGED_ELF_ICON, self.level,
                                                      RANGED_ELF_ICON.get_rect(topright=(105 * CELL, 1 * CELL)))
            self.heavy_unit_button = HeavyFairyButton(HEAVY_ELF_ICON, self.level,
                                                    HEAVY_ELF_ICON.get_rect(topright=(115 * CELL, 1 * CELL)))
            self.hero_unit_button = HeroFairyButton(HERO_ELF_ICON, self.level,
                                                       HERO_ELF_ICON.get_rect(topright=(125 * CELL, 1 * CELL)))
            self.special_button = Special2Button(SPECIAL2_ICON, self.level,
                                                       SPECIAL2_ICON.get_rect(topright=(85 * CELL, 5* CELL)))
        elif self.state == "angel":
            self.light_unit_button = LightAngelButton(LIGHT_ANGEL_ICON, self.level,
                                                    LIGHT_ANGEL_ICON.get_rect(topright=(95 * CELL, 1 * CELL)))
            self.ranged_unit_button = RangedAngelButton(RANGED_ANGEL_ICON, self.level,
                                                    RANGED_ANGEL_ICON.get_rect(topright=(105 * CELL, 1 * CELL)))
            self.heavy_unit_button = HeavyAngelButton(HEAVY_ANGEL_ICON, self.level,
                                                    HEAVY_ANGEL_ICON.get_rect(topright=(115 * CELL, 1 * CELL)))
            self.hero_unit_button = HeroAngelButton(HERO_ANGEL_ICON, self.level,
                                                    HERO_ANGEL_ICON.get_rect(topright=(125 * CELL, 1 * CELL)))
            self.special_button = Special3Button(SPECIAL3_ICON, self.level,
                                                       SPECIAL3_ICON.get_rect(topright=(85 * CELL, 5* CELL)))
        elif self.state == "wraith":
            self.light_unit_button = LightWraithButton(LIGHT_WRAITH_ICON, self.level,
                                                    LIGHT_WRAITH_ICON.get_rect(topright=(95 * CELL, 1 * CELL)))
            self.ranged_unit_button = RangedWraithButton(RANGED_WRAITH_ICON, self.level,
                                                    RANGED_WRAITH_ICON.get_rect(topright=(105 * CELL, 1 * CELL)))
            self.heavy_unit_button = HeavyWraithButton(HEAVY_WRAITH_ICON, self.level,
                                                    HEAVY_WRAITH_ICON.get_rect(topright=(115 * CELL, 1 * CELL)))
            self.hero_unit_button = HeroWraithButton(HERO_WRAITH_ICON, self.level,
                                                    HERO_WRAITH_ICON.get_rect(topright=(125 * CELL, 1 * CELL)))
            self.special_button = Special4Button(SPECIAL4_ICON, self.level,
                                                       SPECIAL4_ICON.get_rect(topright=(85 * CELL, 5* CELL)))
        elif self.state == "villager":
            self.light_unit_button = LightVillagerButton(LIGHT_VILLAGER_ICON, self.level,
                                                    LIGHT_VILLAGER_ICON.get_rect(topright=(95 * CELL, 1 * CELL)))
            self.ranged_unit_button = RangedVillagerButton(RANGED_VILLAGER_ICON, self.level,
                                                    RANGED_VILLAGER_ICON.get_rect(topright=(105 * CELL, 1 * CELL)))
            self.heavy_unit_button = HeavyVillagerButton(HEAVY_VILLAGER_ICON, self.level,
                                                    HEAVY_VILLAGER_ICON.get_rect(topright=(115 * CELL, 1 * CELL)))
            self.hero_unit_button = HeroVillagerButton(HERO_VILLAGER_ICON, self.level,
                                                    HERO_VILLAGER_ICON.get_rect(topright=(125 * CELL, 1 * CELL)))
            self.special_button = Special5Button(SPECIAL5_ICON, self.level,
                                                       SPECIAL5_ICON.get_rect(topright=(85 * CELL, 5* CELL)))
