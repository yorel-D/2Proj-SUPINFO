from src.settings import *
import pygame
from src.sprites import *

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
            self.clicked = not self.clicked

        if self.clicked and self.tb1.tower1.rect.collidepoint(m_pos) and game.mouse.get_pressed()[0]:
            try:
                self.tb1.tower1.turret.sell()
            except AttributeError:
                pass
            self.tb1.towers[self.tb1.tower1] = "available"

        if self.clicked and self.tb1.tower2.rect.collidepoint(m_pos) and game.mouse.get_pressed()[0]:
            try:
                self.tb1.tower2.turret.sell()
            except AttributeError:
                pass
            self.tb1.towers[self.tb1.tower2] = "available"

        if self.clicked and self.tb1.tower3.rect.collidepoint(m_pos) and game.mouse.get_pressed()[0]:
            try:
                self.tb1.tower3.turret.sell()
            except AttributeError:
                pass
            self.tb1.towers[self.tb1.tower3] = "available"

        if self.clicked and self.tb1.tower4.rect.collidepoint(m_pos) and game.mouse.get_pressed()[0]:
            try:
                self.tb1.tower4.turret.sell()
            except AttributeError:
                pass
            self.tb1.towers[self.tb1.tower4] = "available"

        if self.clicked and self.tb2.tower1.rect.collidepoint(m_pos) and game.mouse.get_pressed()[0]:
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
