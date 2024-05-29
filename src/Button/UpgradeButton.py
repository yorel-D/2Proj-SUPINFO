from src.settings import *
from random import randrange
import pygame
from random import randrange
from src.sprites import *
from src.Button.UnitButton import *
from src.Turret.TurretButton import *

class UpgradeButton(pygame.sprite.Sprite):
    def __init__(self, action_bar):
        super().__init__()
        self.action_bar = action_bar
        self.image = UPGRADE_BUTTON
        self.rect = self.image.get_rect(topleft=(60 * CELL, 3 * CELL))
        self.action_bar.level.all_sprites.add(self)
        self.state = "satyrs"
        self.active = True
        self.last_update = 0

    def check_click(self):
        if not self.state == "villager":
            m_pos = pygame.mouse.get_pos()
            now = game.time.get_ticks()
            if now - self.last_update > 5000:
                self.last_update = 0
                if self.state == "satyrs":
                    if self.active and self.rect.collidepoint(m_pos) and pygame.mouse.get_pressed()[0]:
                        self.action_bar.level.player.xp -= 5000
                        self.active = False
                        self.action_bar.light_unit_button.cooldown_bar.kill()
                        self.action_bar.ranged_unit_button.cooldown_bar.kill()
                        self.action_bar.heavy_unit_button.cooldown_bar.kill()
                        self.action_bar.hero_unit_button.cooldown_bar.kill()
                        self.action_bar.special_button.cooldown_bar.kill()
                        self.action_bar.light_unit_button.kill()
                        self.action_bar.ranged_unit_button.kill()
                        self.action_bar.heavy_unit_button.kill()
                        self.action_bar.hero_unit_button.kill()
                        self.action_bar.special_button.kill()
                        self.action_bar.turret_button1.kill()
                        self.action_bar.turret_button2.kill()
                        self.action_bar.turret_button3.kill()
                        self.action_bar.light_unit_button = LightWarriorButton(LIGHT_GOLEM_ICON, self.action_bar.level,
                                                                               LIGHT_GOLEM_ICON.get_rect(
                                                                                   topright=(95 * CELL, 1 * CELL)))
                        self.action_bar.ranged_unit_button = RangedWarriorButton(RANGED_GOLEM_ICON, self.action_bar.level,
                                                                                 RANGED_GOLEM_ICON.get_rect(
                                                                                     topright=(105 * CELL, 1 * CELL)))
                        self.action_bar.heavy_unit_button = HeavyWarriorButton(HEAVY_GOLEM_ICON, self.action_bar.level,
                                                                               HEAVY_GOLEM_ICON.get_rect(
                                                                                   topright=(115 * CELL, 1 * CELL)))
                        self.action_bar.hero_unit_button = HeroWarriorButton(HERO_GOLEM_ICON, self.action_bar.level,
                                                                               HERO_GOLEM_ICON.get_rect(
                                                                                   topright=(125 * CELL, 1 * CELL)))
                        self.action_bar.special_button = Special1Button(SPECIAL1_ICON, self.action_bar.level,
                                                                               SPECIAL1_ICON.get_rect(
                                                                                   topright=(85 * CELL, 5 * CELL)))
                        self.action_bar.turret_button1 = TurretButton4(TURRET_ICON, self.action_bar.level,
                                                                      TURRET_ICON.get_rect(topright=(105 * CELL, 9 * CELL)),
                                                                      price=400)
                        self.action_bar.turret_button2 = TurretButton5(TURRET1_ICON, self.action_bar.level,
                                                                       TURRET1_ICON.get_rect(topright=(115 * CELL, 9 * CELL)),
                                                                       price=2000)
                        self.action_bar.turret_button3 = TurretButton6(TURRET2_ICON, self.action_bar.level,
                                                                   TURRET2_ICON.get_rect(topright=(125 * CELL, 9 * CELL)),
                                                                   price=4000)
                        self.state = "golems"
                        self.action_bar.level.player.state = self.state
                        self.action_bar.level.player.update_image()
                elif self.state == "golems":
                    if self.active and self.rect.collidepoint(m_pos) and pygame.mouse.get_pressed()[0]:
                        self.active = False
                        self.action_bar.level.player.xp -= 5000
                        self.action_bar.light_unit_button.cooldown_bar.kill()
                        self.action_bar.ranged_unit_button.cooldown_bar.kill()
                        self.action_bar.heavy_unit_button.cooldown_bar.kill()
                        self.action_bar.hero_unit_button.cooldown_bar.kill()
                        self.action_bar.special_button.cooldown_bar.kill()
                        self.action_bar.light_unit_button.kill()
                        self.action_bar.ranged_unit_button.kill()
                        self.action_bar.heavy_unit_button.kill()
                        self.action_bar.hero_unit_button.kill()
                        self.action_bar.special_button.kill()
                        self.action_bar.turret_button1.kill()
                        self.action_bar.turret_button2.kill()
                        self.action_bar.turret_button3.kill()
                        self.action_bar.light_unit_button = LightFairyButton(LIGHT_ELF_ICON, self.action_bar.level,
                                                                           LIGHT_ELF_ICON.get_rect(
                                                                               topright=(95 * CELL, 1 * CELL)))
                        self.action_bar.ranged_unit_button = RangedFairyButton(RANGED_ELF_ICON, self.action_bar.level,
                                                                             RANGED_ELF_ICON.get_rect(
                                                                                 topright=(105 * CELL, 1 * CELL)))
                        self.action_bar.heavy_unit_button = HeavyFairyButton(HEAVY_ELF_ICON, self.action_bar.level,
                                                                           HEAVY_ELF_ICON.get_rect(
                                                                               topright=(115 * CELL, 1 * CELL)))
                        self.action_bar.hero_unit_button = HeroFairyButton(HERO_ELF_ICON, self.action_bar.level,
                                                                           HERO_ELF_ICON.get_rect(
                                                                               topright=(125 * CELL, 1 * CELL)))
                        self.action_bar.special_button = Special2Button(SPECIAL2_ICON, self.action_bar.level,
                                                                               SPECIAL2_ICON.get_rect(
                                                                                   topright=(85 * CELL, 5 * CELL)))
                        self.action_bar.turret_button1 = TurretButton7(TURRET3_ICON, self.action_bar.level,
                                                                       TURRET3_ICON.get_rect(topright=(105 * CELL, 9 * CELL)),
                                                                       price=400)
                        self.action_bar.turret_button2 = TurretButton8(TURRET4_ICON, self.action_bar.level,
                                                                       TURRET4_ICON.get_rect(topright=(115 * CELL, 9 * CELL)),
                                                                       price=2000)
                        self.action_bar.turret_button3 = TurretButton9(TURRET5_ICON, self.action_bar.level,
                                                                       TURRET5_ICON.get_rect(topright=(125 * CELL, 9 * CELL)),
                                                                       price=4000)
                        self.state = "elfs"
                        self.action_bar.level.player.state = self.state
                        self.action_bar.level.player.update_image()
                elif self.state == "elfs":
                    if self.active and self.rect.collidepoint(m_pos) and pygame.mouse.get_pressed()[0]:
                        self.active = False
                        self.action_bar.level.player.xp -= 5000
                        self.action_bar.light_unit_button.cooldown_bar.kill()
                        self.action_bar.ranged_unit_button.cooldown_bar.kill()
                        self.action_bar.heavy_unit_button.cooldown_bar.kill()
                        self.action_bar.hero_unit_button.cooldown_bar.kill()
                        self.action_bar.special_button.cooldown_bar.kill()
                        self.action_bar.light_unit_button.kill()
                        self.action_bar.ranged_unit_button.kill()
                        self.action_bar.heavy_unit_button.kill()
                        self.action_bar.hero_unit_button.kill()
                        self.action_bar.special_button.kill()
                        self.action_bar.turret_button1.kill()
                        self.action_bar.turret_button2.kill()
                        self.action_bar.turret_button3.kill()
                        self.action_bar.light_unit_button = LightAngelButton(LIGHT_ANGEL_ICON, self.action_bar.level,
                                                                           LIGHT_ANGEL_ICON.get_rect(
                                                                               topright=(95 * CELL, 1 * CELL)))
                        self.action_bar.ranged_unit_button = RangedAngelButton(RANGED_ANGEL_ICON, self.action_bar.level,
                                                                           RANGED_ANGEL_ICON.get_rect(
                                                                               topright=(105 * CELL, 1 * CELL)))
                        self.action_bar.heavy_unit_button = HeavyAngelButton(HEAVY_ANGEL_ICON, self.action_bar.level,
                                                                           HEAVY_ANGEL_ICON.get_rect(
                                                                               topright=(115 * CELL, 1 * CELL)))
                        self.action_bar.hero_unit_button = HeroAngelButton(HERO_ANGEL_ICON, self.action_bar.level,
                                                                           HERO_ANGEL_ICON.get_rect(
                                                                               topright=(125 * CELL, 1 * CELL)))
                        self.action_bar.special_button = Special3Button(SPECIAL3_ICON, self.action_bar.level,
                                                                               SPECIAL3_ICON.get_rect(
                                                                                   topright=(85 * CELL, 5 * CELL)))
                        self.action_bar.turret_button1 = TurretButton10(TURRET6_ICON, self.action_bar.level,
                                                                        TURRET6_ICON.get_rect(topright=(105 * CELL, 9 * CELL)),
                                                                        price=400)
                        self.action_bar.turret_button2 = TurretButton11(TURRET7_ICON, self.action_bar.level,
                                                                        TURRET7_ICON.get_rect(topright=(115 * CELL, 9 * CELL)),
                                                                        price=2000)
                        self.action_bar.turret_button3 = TurretButton12(TURRET8_ICON, self.action_bar.level,
                                                                        TURRET8_ICON.get_rect(topright=(125 * CELL, 9 * CELL)),
                                                                        price=4000)
                        self.state = "angel"
                        self.action_bar.level.player.state = self.state
                        self.action_bar.level.player.update_image()

                elif self.state == "angel":
                    if self.active and self.rect.collidepoint(m_pos) and pygame.mouse.get_pressed()[0]:
                        self.active = False
                        self.action_bar.level.player.xp -= 5000
                        self.action_bar.light_unit_button.cooldown_bar.kill()
                        self.action_bar.ranged_unit_button.cooldown_bar.kill()
                        self.action_bar.heavy_unit_button.cooldown_bar.kill()
                        self.action_bar.hero_unit_button.cooldown_bar.kill()
                        self.action_bar.special_button.cooldown_bar.kill()
                        self.action_bar.light_unit_button.kill()
                        self.action_bar.ranged_unit_button.kill()
                        self.action_bar.heavy_unit_button.kill()
                        self.action_bar.hero_unit_button.kill()
                        self.action_bar.special_button.kill()
                        self.action_bar.turret_button1.kill()
                        self.action_bar.turret_button2.kill()
                        self.action_bar.turret_button3.kill()
                        self.action_bar.light_unit_button = LightWraithButton(LIGHT_WRAITH_ICON, self.action_bar.level,
                                                                           LIGHT_WRAITH_ICON.get_rect(
                                                                               topright=(95 * CELL, 1 * CELL)))
                        self.action_bar.ranged_unit_button = RangedWraithButton(RANGED_WRAITH_ICON, self.action_bar.level,
                                                                           RANGED_WRAITH_ICON.get_rect(
                                                                               topright=(105 * CELL, 1 * CELL)))
                        self.action_bar.heavy_unit_button = HeavyWraithButton(HEAVY_WRAITH_ICON, self.action_bar.level,
                                                                           HEAVY_WRAITH_ICON.get_rect(
                                                                               topright=(115 * CELL, 1 * CELL)))
                        self.action_bar.hero_unit_button = HeroWraithButton(HERO_WRAITH_ICON, self.action_bar.level,
                                                                           HERO_WRAITH_ICON.get_rect(
                                                                               topright=(125 * CELL, 1 * CELL)))
                        self.action_bar.special_button = Special4Button(SPECIAL4_ICON, self.action_bar.level,
                                                                               SPECIAL4_ICON.get_rect(
                                                                                   topright=(85 * CELL, 5 * CELL)))
                        self.action_bar.turret_button1 = TurretButton13(TURRET9_ICON, self.action_bar.level,
                                                                        TURRET9_ICON.get_rect(topright=(105 * CELL, 9 * CELL)),
                                                                        price=400)
                        self.action_bar.turret_button2 = TurretButton14(TURRET10_ICON, self.action_bar.level,
                                                                        TURRET10_ICON.get_rect(topright=(115 * CELL, 9 * CELL)),
                                                                        price=2000)
                        self.action_bar.turret_button3 = TurretButton15(TURRET11_ICON, self.action_bar.level,
                                                                        TURRET11_ICON.get_rect(topright=(125 * CELL, 9 * CELL)),
                                                                        price=4000)
                        self.state = "wraith"
                        self.action_bar.level.player.state = self.state
                        self.action_bar.level.player.update_image()
                elif self.state == "wraith":
                    if self.active and self.rect.collidepoint(m_pos) and pygame.mouse.get_pressed()[0]:
                        self.active = False
                        self.action_bar.level.player.xp -= 5000
                        self.action_bar.light_unit_button.cooldown_bar.kill()
                        self.action_bar.ranged_unit_button.cooldown_bar.kill()
                        self.action_bar.heavy_unit_button.cooldown_bar.kill()
                        self.action_bar.hero_unit_button.cooldown_bar.kill()
                        self.action_bar.special_button.cooldown_bar.kill()
                        self.action_bar.light_unit_button.kill()
                        self.action_bar.ranged_unit_button.kill()
                        self.action_bar.heavy_unit_button.kill()
                        self.action_bar.hero_unit_button.kill()
                        self.action_bar.special_button.kill()
                        self.action_bar.turret_button1.kill()
                        self.action_bar.turret_button2.kill()
                        self.action_bar.turret_button3.kill()
                        self.action_bar.light_unit_button = LightVillagerButton(LIGHT_VILLAGER_ICON, self.action_bar.level,
                                                                           LIGHT_VILLAGER_ICON.get_rect(
                                                                               topright=(95 * CELL, 1 * CELL)))
                        self.action_bar.ranged_unit_button = RangedVillagerButton(RANGED_VILLAGER_ICON, self.action_bar.level,
                                                                           RANGED_VILLAGER_ICON.get_rect(
                                                                               topright=(105 * CELL, 1 * CELL)))
                        self.action_bar.heavy_unit_button = HeavyVillagerButton(HEAVY_VILLAGER_ICON, self.action_bar.level,
                                                                           HEAVY_VILLAGER_ICON.get_rect(
                                                                               topright=(115 * CELL, 1 * CELL)))
                        self.action_bar.hero_unit_button = HeroVillagerButton(HERO_VILLAGER_ICON, self.action_bar.level,
                                                                           HERO_VILLAGER_ICON.get_rect(
                                                                               topright=(125 * CELL, 1 * CELL)))
                        self.action_bar.special_button = Special5Button(SPECIAL5_ICON, self.action_bar.level,
                                                                               SPECIAL5_ICON.get_rect(
                                                                                   topright=(85 * CELL, 5 * CELL)))
                        self.action_bar.turret_button1 = TurretButton13(TURRET12_ICON, self.action_bar.level,
                                                                        TURRET12_ICON.get_rect(topright=(105 * CELL, 9 * CELL)),
                                                                        price=400)
                        self.action_bar.turret_button2 = TurretButton14(TURRET13_ICON, self.action_bar.level,
                                                                        TURRET13_ICON.get_rect(topright=(115 * CELL, 9 * CELL)),
                                                                        price=2000)
                        self.action_bar.turret_button3 = TurretButton15(TURRET14_ICON, self.action_bar.level,
                                                                        TURRET14_ICON.get_rect(topright=(125 * CELL, 9 * CELL)),
                                                                        price=4000)
                        self.state = "villager"
                        self.action_bar.level.player.state = self.state
                        self.action_bar.level.player.update_image()

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
