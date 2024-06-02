import pygame, sys
from src.settings import *
from src.sprites import *
from src.player import Player
from src.ai import AI
from src.Button.ActionBar import ActionBar

class Level:
    def __init__(self, state="satyrs"):
        self.mode = None
        self.game = game
        self.display_surface = pygame.display.get_surface()
        self.background = BACKGROUND
        self.background_rect = self.background.get_rect()
        self.all_sprites = pygame.sprite.Group()
        self.player_sprites = pygame.sprite.Group()
        self.ai_sprites = pygame.sprite.Group()
        self.player = Player(self, state)
        self.player_sprites.add(self.player)
        self.ai = AI(self, state)
        self.ai_sprites.add(self.ai)
        self.all_sprites.add(self.player, self.ai)
        self.action_bar = ActionBar(self, state)
        
        self.speed_multiplier = 1
        self.speed_options = [1, 2, 4]
        self.current_speed_index = 0
        self.font = pygame.font.Font("arial-unicode-ms.ttf", 25)
        self.speed_button_rect = pygame.Rect(10, 10, 40, 40)
        self.speed_button_pressed = False
        
    def draw_speed_button(self):
        button_text = f"x{self.speed_options[self.current_speed_index]}"
        if self.speed_multiplier == 4:
            button_color = (0, 0, 255)
        else:
            button_color = (255, 0, 0) if self.speed_multiplier > 1 else (0, 255, 0)
        pygame.draw.rect(self.display_surface, button_color, self.speed_button_rect)
        text_surface = self.font.render(button_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.speed_button_rect.center)
        self.display_surface.blit(text_surface, text_rect)
        
    def toggle_speed(self):
        self.current_speed_index = (self.current_speed_index + 1) % len(self.speed_options)
        self.speed_multiplier = self.speed_options[self.current_speed_index]
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.speed_button_rect.collidepoint(event.pos):
                    self.toggle_speed()
    
    def run(self, dt, mode):
        self.mode = mode
        self.ai.set_mode(mode)
        self.handle_events()
        self.display_surface.blit(self.background, self.background_rect)
        self.ai.update(dt)
        self.all_sprites.draw(self.display_surface)
        
        adjusted_dt = dt * self.speed_multiplier
        
        self.all_sprites.update(adjusted_dt)
        
        self.draw_speed_button()
            
    def end_game(self):
        if self.ai.health <= 0:
            return "win"
        elif self.player.health <= 0:
            return "lose"
        return None

    def game_over(self):
        if self.player.health <= 0 or self.ai.health <= 0:
            return True