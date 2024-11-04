from pico2d import *
import random
from boy import *
import game_world
# 클래스 단위로 분리
# Game object class here


 
#event_boy=0
def handle_events():
    global running
    #global event_boy
    events = get_events()
    for event in events:
        #if event.type==SDL_KEYDOWN:
            #if event.key ==SDLK_RIGHT:
                #event_boy=1

        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            if event.type == SDL_KEYDOWN or event.type == SDL_KEYUP:
                boy.handle_event(event)
            


def create_world():
    global running
    global grass1
    global grass2
    global boy

    running = True
    grass1 = Grass(30)
    game_world.add_object(grass1,0) 
    boy =  Boy()
    game_world.add_object(boy,1)
    grass2 = Grass(20)
    game_world.add_object(grass2,1)



def update_world():
    game_world.update()


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


open_canvas()
create_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
