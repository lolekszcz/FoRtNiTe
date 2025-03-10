from classes.GameObject import GameObject
from classes.Obstacles import Wall
max_health=100
player_speed=5
class Player(GameObject):
    def __init__(self,game,x,y,w,h,image):
        super().__init__(game,x,y,w,h,image)
        self.health=max_health
        self.speed=player_speed
        self.vwall = GameObject(self.game, self.game.mouse_pos[0], self.game.mouse_pos[1], 100, 50, None,
                                color=(100, 0, 0), server=False, visible=False)
    def move(self):

        if self.game.w:
            self.y-=self.speed
        elif self.game.s:
            self.y+=self.speed
        if self.game.a:
            self.x-=self.speed
        elif self.game.d:
            self.x+=self.speed
        self.borders()
        self.update()
    def borders(self):
        if self.x<0:
            self.x=0
        if self.x>=self.game.width-self.w:
            self.x=self.game.width-self.w
        if self.y<0:
            self.y=0
        if self.y>=self.game.height-self.h:
            self.y=self.game.height-self.h
    def plan_wall(self):
        if self.game.q:

            self.vwall.visible=True
        else:
            self.vwall.visible = False
    def build_wall(self):
        pass