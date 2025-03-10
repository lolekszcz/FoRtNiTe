import socket

import pygame

from classes import GameObject,Player
from classes.Obstacles import Wall


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

        self.socket = socket.socket()
        print("aaaa")
        self.socket.connect(('127.0.0.1', 12345))

        self.players = {}
        self.buildings = []

        self.w=False
        self.s = False
        self.a = False
        self.d = False
        self.q=False
        self.left=False
        self.right=False
        self.mouse_pos = pygame.mouse.get_pos()
        self.player=Player.Player(self,0,0,100,100,None, isLocal=True)
    def render(self):
        self.socket.send(f"UPDATE_OWN_POSITION|X={self.player.x};Y={self.player.y}".encode())

        # Receive response from server
        response = self.socket.recv(1024).decode()

        if ";" in response:
            print(response)
            data = response.split("\n")
            pl_data = data[0]
            building_data = data[1]

            # Player stuff
            if ";" in pl_data:
                player_data = pl_data.split(";")
                p_id = player_data[2]
                print(self.players.keys())
                if p_id not in self.players.keys():
                    self.players[p_id] = Player.Player(self, 0, 0, 100, 100, None, color=(200, 0,0))
                else:
                    player = self.players[p_id]
                    posX = int(player_data[0][2:])
                    posY = int(player_data[1][2:])

                    player.x = posX
                    player.y = posY

            # Building stuff
            if ";" in building_data:
                self.clear_buildings()
                buildings = building_data.split('|')
                print(len(buildings))
                buildings.pop(-1)
                print(buildings)
                for building in buildings:
                        building_data = building.split(';')
                        posX = int(building_data[0][2:])
                        posY = int(building_data[1][2:])

                        width = int(building_data[2][2:])
                        height = int(building_data[3][2:])

                        health = int(building_data[4][3:])

                        self.buildings.append(Wall(self, posX, posY,width,height,None))

        self.window.fill(self.bg_color)
        for object in self.objects:
            if type(object)==Player.Player and object.isLocal:
                object.move()
                object.plan_wall()
            elif type(object)==Player.Player:
                object.update()
                #object.borders()
            object.render()

        for player in self.players.values():
            player.render()

        #print(response)
    def clear_buildings(self):
        for build in self.buildings:
            self.objects.remove(build)
            del build
        self.buildings = []
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
                    if self.q:
                        self.buildings.append(self.player.build_wall())



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

                if event.key == pygame.K_f:
                    print(self.socket.recv(1024).decode())