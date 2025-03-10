import pygame
from classes import GameObject,Player

class Simulation:
    def __init__(self, app):
        self.app = app
        self.debug = False
        self.bg_color = (33, 33, 33)
        self.window = self.app.screen
        self.buttons = []
        self.width=self.app.width
        self.height=self.app.height
        self.side_margin = int(20 * self.app.scale)
        self.objects=[]
        self.selected_button = None


        self.w=False
        self.s = False
        self.a = False
        self.d = False
        self.q=False
        self.left=False
        self.right=False
        self.mouse_pos = pygame.mouse.get_pos()
        self.player=Player.Player(self,0,0,100,100,None)
    def render(self):
        self.window.fill(self.bg_color)
        for object in self.objects:
            if type(object)==Player.Player:
                object.move()
                object.plan_wall()
            object.render()

    # Overrides the default events function in app.py
    def events(self):
        self.mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.run = False
                pygame.quit()

            if event.type==pygame.MOUSEBUTTONDOWN:
                a=pygame.mouse.get_pressed()
                if a[0]:
                    self.left=True

                if a[2]:
                    self.right=True
                    self.player.build_wall()


            if event.type==pygame.MOUSEBUTTONUP:
                a=pygame.mouse.get_pressed()
                if not a[0]:
                    self.left=False
                if not a[2]:
                    self.right=False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    pass
                elif event.key==pygame.K_w:
                    self.w=True
                elif event.key==pygame.K_s:
                    self.s=True
                elif event.key==pygame.K_a:
                    self.a=True
                elif event.key==pygame.K_d:
                    self.d=True
                elif event.key==pygame.K_q:
                    if self.q:
                        self.q=False
                    else:
                        self.q=True

            if event.type == pygame.KEYUP:

                if event.key==pygame.K_w:
                    self.w=False
                elif event.key==pygame.K_s:
                    self.s=False
                elif event.key==pygame.K_a:
                    self.a=False
                elif event.key==pygame.K_d:
                    self.d=False
