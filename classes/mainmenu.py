import pygame
from classes import buttons
from classes import inputBox
class MainMenu:
    def __init__(self, app):
        self.app = app
        self.debug = False

        self.main_text_rect_center = (self.app.width // 2, 250 * self.app.scale)
        self.font = "fonts/main_font.ttf"

        self.pgfont = pygame.font.Font(self.font, 84)


        self.font_color = (255, 255, 255)
        self.bg_color = (33, 33, 33)
        self.buttons = [
            buttons.Button(200 * self.app.scale, 75 * self.app.scale, self.app.width / 2 - 100 * self.app.scale,
                           self.app.height / 2 - 75 * self.app.scale / 2, False, self.font, "Play", (0, 0, 0),
                           self.font_color, 'play', self.app),
            buttons.Button(200 * self.app.scale, 75 * self.app.scale, self.app.width / 2 - 100 * self.app.scale,
                           self.app.height / 2 - 275 * self.app.scale / 2, False, self.font, "Start Server", (0, 0, 0),
                           self.font_color, 'start_server', self.app)
        ]
        self.window = self.app.screen


        self.serverbox = inputBox.InputBox(200, 500,
                                    800, 110, self.pgfont, max_length=20, font_color=(255, 255, 255), text="192.168.12.13")

    def render(self):
        self.window.fill(self.bg_color)
        for button in self.buttons:
            button.render()
        font = pygame.font.Font(self.font, int(72 * self.app.scale))
        display_text = font.render("P R O J E C T  T E M P L A T E", True, self.font_color)
        display_text_rect = display_text.get_rect()
        display_text_rect.center = self.main_text_rect_center
        self.app.screen.blit(display_text, display_text_rect)
        self.serverbox.draw(self.app.screen)



    # Overrides the default events function in app.py
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.app.run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click_pos = pygame.mouse.get_pos()
                for button in self.buttons:
                    if button.rect.collidepoint(click_pos[0], click_pos[1]):
                        button.click()
            self.serverbox.handle_event(event)