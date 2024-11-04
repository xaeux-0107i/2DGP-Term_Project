from pico2d import *

from backgound import Background, Flame
from cookie import Cookie
from mapSeed import create_map, max_num
from random import randint

global speed
global count
global change

count = 0
change = 0
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
    world.append(flame)

    map1 = create_map(0)
    map2 = create_map(4)

    # 쿠키 그리기
    cookie = Cookie()

def update_world():
    global count
    global change
    global map1
    global map2

    count += 2*speed
    if count % 800 == 0:
        if change % 2 == 0:
            map1.clear()
            map1 = create_map(randint(1, max_num))
            change += 1
            print('map1 초기화')
        else:
            map2.clear
            map2 = create_map(randint(1, max_num))
            change += 1
            print('map2 초기화')

    for o in world:
        o.update()

    for o in map1:
        o.update()

    for o in map2:
        o.update()

    cookie.update()

    pass

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    for o in map1:
        o.draw()
    for o in map2:
        o.draw()
    cookie.draw()
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

