
from pico2d import *
def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key==SDLK_SPACE
def space_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key==SDLK_SPACE
def time_out(e):
    return e[0]=='TIME_OUT'

def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key==SDLK_RIGHT
def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key==SDLK_RIGHT
def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key==SDLK_LEFT
def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key==SDLK_LEFT
def a_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key ==SDLK_a


class StateMachine:
    def __init__(self,o):
        self.o = o
        self.event_que=[]

    def start(self , state):
        self.cur_state = state
        print(f'Enter into state')        
        self.cur_state.enter(self.o,('START',0))

        pass
    def add_event(self,e):
        print(f'event = {e}')
        self.event_que.append(e)
    def set_transitions(self,transitions):
        self.transitions = transitions

    def update(self):
        self.cur_state.do(self.o)
        if self.event_que:
            event=self.event_que.pop(0)
            self.handle_event(event)

    def draw(self):
        self.cur_state.draw(self.o)
    def handle_event(self,e):
        for event,next_state in self.transitions[self.cur_state].items():
            if event(e):
                self.cur_state.exit(self.o,e)
                
                self.cur_state = next_state
                self.cur_state.enter(self.o,e)
                return
            #이 시점으로 왔다는건 event에 따른 전환 못함
        print(f'    Warning : {e}not gandled at State{self.cur_state}')
