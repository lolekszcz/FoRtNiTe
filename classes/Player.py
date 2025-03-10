from classes.GameObject import GameObject
max_health=100
player_speed=5
class Player(GameObject):
    def __init__(self,game,x,y,w,h,image):
        super().__init__(game,x,y,w,h,image)
        self.health=max_health
        self.speed=player_speed
    def move(self):
        print('xx')
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
    def build_wall(self):
        pass
