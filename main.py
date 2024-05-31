import pygame, sys, src.level as level
from src.sprites import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Age Of War - ish")
        self.clock = pygame.time.Clock()
        self.starting = True
        self.running = False
        self.game_over = False
        self.game_won = False
        self.game_won_image = pygame.image.load("Resources/game_won.png").convert_alpha()
        self.game_over_image = pygame.image.load("Resources/game_over.png").convert_alpha()
        self.languages = {
            "English": ["Solo Play", "Multiplayer", "Easy", "Normal", "Hard", "Impossible", "Settings", "Back", "Music: On", "Music: Off", "Language: English"],
            "Français": ["Jeu Solo", "Multijoueur", "Facile", "Normal", "Difficile", "Impossible", "Paramètres", "Retour", "Musique : Activée", "Musique : Désactivée", "Langue : Français"],
            "Русский": ["Одиночная игра", "Многопользовательская", "Легко", "Нормально", "Трудно", "Невозможно", "Настройки", "Назад", "Музыка: Вкл", "Музыка: Выкл", "Язык: Русский"],
            "עברית": ["משחק בודד", "רשת משחקים", "קל", "נורמלי", "קשה", "בלתי אפשרי", "הגדרות", "חזור", "מוזיקה: פועל", "מוזיקה: כבוי", "שפה: עברית"],
            "العربية": ["لعب فردي", "متعدد اللاعبين", "سهل", "عادي", "صعب", "مستحيل", "الإعدادات", "عودة", "الموسيقى: تشغيل", "الموسيقى: إيقاف", "اللغة: العربية"],
            "हिन्दी": ["एकल खेल", "बहुप्रयोक्ता", "आसान", "सामान्य", "कठिन", "असंभव", "सेटिंग्स", "वापस", "संगीत: चालू", "संगीत: बंद", "भाषा: हिन्दी"],
            "中文": ["单人游戏", "多人游戏", "简单", "普通", "困难", "不可能", "设置", "返回", "音乐：开启", "音乐：关闭", "语言：中文"]
        }
        self.language_index = 0
        self.music_enabled = True
        self.font = pygame.font.Font("arial-unicode-ms.ttf", 75)
        
        self.init_music()

    def init_music(self):
        self.music_file = "Resources/01. Age of War - Theme Song.mp3"
        pygame.mixer.music.load(self.music_file)
        if self.music_enabled:
            pygame.mixer.music.play(-1)

    def start_menu(self):
        while self.starting:
            solo_text = self.languages[self.get_current_language()][0]
            solo = self.font.render(solo_text, True, "white")
            solo_rect = solo.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 75))
            multi_joueur_text = self.languages[self.get_current_language()][1]
            multi_joueur = self.font.render(multi_joueur_text, True, "white")
            multi_joueur_rect = multi_joueur.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
            settings_text = self.languages[self.get_current_language()][6]
            settings = self.font.render(settings_text, True, "white")
            settings_rect = settings.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 75))

            m_pos = pygame.mouse.get_pos()
            self.screen.fill("#720E00")
            self.screen.blit(solo, solo_rect)
            self.screen.blit(multi_joueur, multi_joueur_rect)
            self.screen.blit(settings, settings_rect)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if solo_rect.collidepoint(m_pos) and pygame.mouse.get_pressed()[0]:
                        self.solo_menu()
                    elif multi_joueur_rect.collidepoint(m_pos) and pygame.mouse.get_pressed()[0]:
                        self.run("multijoueur")
                    elif settings_rect.collidepoint(m_pos) and pygame.mouse.get_pressed()[0]:
                        self.settings_menu()

            pygame.display.update()

    def solo_menu(self):
        while True:
            easy_text = self.languages[self.get_current_language()][2]
            easy = self.font.render(easy_text, True, "white")
            easy_rect = easy.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 75))
            normal_text = self.languages[self.get_current_language()][3]
            normal = self.font.render(normal_text, True, "white")
            normal_rect = normal.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 0))
            hard_text = self.languages[self.get_current_language()][4]
            hard = self.font.render(hard_text, True, "white")
            hard_rect = hard.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 75))
            impossible_text = self.languages[self.get_current_language()][5]
            impossible = self.font.render(impossible_text, True, "white")
            impossible_rect = impossible.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 150))
            back_text = self.languages[self.get_current_language()][7]
            back = self.font.render(back_text, True, "white")
            back_rect = back.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 -150))

            m_pos = pygame.mouse.get_pos()
            self.screen.fill("#720E00")
            self.screen.blit(easy, easy_rect)
            self.screen.blit(normal, normal_rect)
            self.screen.blit(hard, hard_rect)
            self.screen.blit(impossible, impossible_rect)
            self.screen.blit(back, back_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if easy_rect.collidepoint(m_pos) and pygame.mouse.get_pressed()[0]:
                        self.starting = False
                        self.run("easy")
                    elif normal_rect.collidepoint(m_pos) and pygame.mouse.get_pressed()[0]:
                        self.starting = False
                        self.run("normal")
                    elif hard_rect.collidepoint(m_pos) and pygame.mouse.get_pressed()[0]:
                        self.starting = False
                        self.run("hard")
                    elif impossible_rect.collidepoint(m_pos) and pygame.mouse.get_pressed()[0]:
                        self.starting = False
                        self.run("impossible")
                    elif back_rect.collidepoint(m_pos) and pygame.mouse.get_pressed()[0]:
                        return

            pygame.display.update()

    def settings_menu(self):
        while True:
            language_keys = list(self.languages.keys())
            back_text = self.languages[language_keys[self.language_index]][7]
            music_on_text = self.languages[language_keys[self.language_index]][8]
            music_off_text = self.languages[language_keys[self.language_index]][9]
            language_text = self.languages[language_keys[self.language_index]][10]

            back = self.font.render(back_text, True, "white")
            back_rect = back.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 50))
            music = self.font.render(music_on_text if self.music_enabled else music_off_text, True, "white")
            music_rect = music.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 25))
            language = self.font.render(language_text, True, "white")
            language_rect = language.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 100))

            self.screen.fill("#720E00")
            self.screen.blit(back, back_rect)
            self.screen.blit(music, music_rect)
            self.screen.blit(language, language_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_rect.collidepoint(event.pos):
                        return
                    elif music_rect.collidepoint(event.pos):
                        self.toggle_music()
                    elif language_rect.collidepoint(event.pos):
                        self.cycle_language()

            pygame.display.update()

    def cycle_language(self):
        self.language_index = (self.language_index + 1) % len(self.languages)

    def get_current_language(self):
        return list(self.languages.keys())[self.language_index]

    def toggle_music(self):
        self.music_enabled = not self.music_enabled
        if self.music_enabled:
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.stop()

    def run(self, mode):
        self.level = level.Level()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            game_outcome = self.level.end_game()
            if game_outcome:
                self.end(game_outcome)
                break
            dt = self.clock.tick(60) / 1000
            self.level.run(dt, mode)
            pygame.display.update()

    def end(self, outcome):
        self.display_end_message(outcome)

    def display_end_message(self, outcome):
        image = self.game_won_image if outcome == "win" else self.game_over_image
        image_rect = image.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        while True:
            self.screen.fill("#720E00")
            self.screen.blit(image, image_rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.start_menu()
