from pico2d import *

from backgound import Background, Flame
from cookie import Cookie
from mapSeed import create_map

global speed
speed = 4

def handle_events():
    global running
    global cookie
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            if cookie.state == 0 or cookie.state == 2 :
                cookie.state = 1  # 점프
                cookie.jump_count = 0
                cookie.frame = 0
                cookie.dy = 15
            elif cookie.state == 1:
                cookie.state = 3  # 2단 점프
                cookie.jump_count = 0
                cookie.frame = 0
                cookie.dy = 15
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            cookie.state = 2 # 슬라이딩
        elif event.type == SDL_KEYUP and event.key == SDLK_DOWN:
            cookie.state = 0 # 달리기

def reset_world():
    global running
    global back_ground
    global world
    global flame
    global cookie
    global map1, map2

    running = True
    world = []

    back_ground = Background()
    world.append(back_ground)
    flame = Flame()

    map1 = create_map(0)
    map2 = create_map(2)

    world += map1
    world += map2
    # 쿠키 그리기

    cookie = Cookie()
    world.append(cookie)

def update_world():
    for o in world:
        o.update()
    pass

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

open_canvas()
reset_world()

# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()

