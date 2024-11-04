from pico2d import *
import game_world

class Ball:
    def __init__(self,x,y,speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = load_image('ball21x21.png')
    def draw(self):
        self.image.draw(self.x,self.y,20,20)
    def update(self):
        self.x += self.speed
        if self.x < 25 or self.x > 775:
            game_world.remove_object(self)