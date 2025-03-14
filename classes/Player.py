from classes.GameObject import GameObject
from classes.Obstacles import Wall
from classes.bullet import Bullet
import math
max_health=100
player_speed=5
class Player(GameObject):
    def __init__(self,game,x,y,w,h,image, color=(255,255,255), isLocal=False):
        super().__init__(game,x,y,w,h,image, color=color, isLocal=isLocal)
        self.health=max_health
        self.speed=player_speed
        self.vwall = GameObject(self.game, self.game.mouse_pos[0], self.game.mouse_pos[1], 100, 50, None,
                                color=(100, 0, 0), server=False, visible=False)
        self.mode = 0
        self.timer=0
        self.range=300
    def move(self):
        self.dx=0
        self.dy=0
        if self.game.w:
            self.y-=self.speed
            self.dy = -self.speed
        elif self.game.s:
            self.y+=self.speed
            self.dy = self.speed
        if self.game.a:
            self.x-=self.speed
            self.dx = -self.speed
        elif self.game.d:
            self.x+=self.speed
            self.dx = self.speed
        self.update()
        self.borders()

    def borders(self):
        for object in self.game.objects:
            if type(object)==Wall:
                if self.rect.colliderect(object.rect):
                    self.x-=3*self.dx
                    self.y-=3*self.dy

        if self.x<0:
            self.x=0
        if self.x>=self.game.width-self.w:
            self.x=self.game.width-self.w
        if self.y<0:
            self.y=0
        if self.y>=self.game.height-self.h:
            self.y=self.game.height-self.h
    def plan_wall(self):
        self.timer+=1
        if self.game.mouse_pos[0]>=self.x and self.game.mouse_pos[0]<=self.x+self.w:
            self.mode=0
        elif self.game.mouse_pos[1]>=self.y and self.game.mouse_pos[1]<=self.y+self.h:
            self.mode=1
        if self.mode==1:

            self.vwall.x=self.game.mouse_pos[0]-10
            self.vwall.y = self.game.mouse_pos[1]-50
            self.vwall.w = 20
            self.vwall.h = 100
            self.vwall.update()
        elif self.mode==0:

            self.vwall.x = self.game.mouse_pos[0]-50
            self.vwall.y = self.game.mouse_pos[1]-10

            self.vwall.w = 100
            self.vwall.h = 20
            self.vwall.update()
        if self.game.q:
            print()

            self.vwall.visible=True
        else:
            self.vwall.visible = False
        if math.sqrt((self.x - self.game.mouse_pos[0]) ** 2 + (self.y - self.game.mouse_pos[1]) ** 2) > self.range:
            self.vwall.visible=False

    def build_wall(self):
        if self.timer>=20:
            self.timer=0
            wall = Wall(self.game,self.vwall.x,self.vwall.y,self.vwall.w,self.vwall.h,None)
            self.game.socket.send(f"ADD_BUILDING|X={self.vwall.x};Y={self.vwall.y};Y={self.vwall.w};Y={self.vwall.h};".encode())
            return wall

    def fire_bullet(self):
        bullet = Bullet(self.game, self.x, self.y, 5, 20,None, 1, 50, self.dx, self.dy)
        return bullet