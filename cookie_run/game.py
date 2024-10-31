from pico2d import *

from backgound import Background, Flame
from cookie import Cookie
from object import Fence, Jelly, Olive, Fork, ForkS1, ForkS2

global speed
speed = 4

def create_map():
    global fences1, fences2
    global jelly1, jelly2
    global olive1
    global forkS1, forkS2, fork
    fences1 = [Fence(i * 100 + 50) for i in range (0, 9)]
    fences2 = [Fence(i * 100 + 950) for i in range(0, 9)]
    jelly1 = [Jelly(100 * i + 50) for i in range(0, 18)]
    jelly2 = [Jelly(100 * i + 950) for i in range(0, 18)]
    olive1 = [Olive(100 * i + 50) for i in range(0, 9)]
    fork = [Fork(100 * i + 50) for i in range(0, 9)]
    forkS1 = [ForkS1(100 * i + 50) for i in range(0, 9)]
    forkS2 = [ForkS2(100 * i + 50) for i in range(0, 9)]
    pass

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

    running = True
    world = []
    create_map()

    back_ground = Background()
    world.append(back_ground)
    flame = Flame()
    world.append(flame)
    world += fences1
    world += fences2
    #world += jelly1
    #world += jelly2
    #world += olive1
    #world += forkS1
    #world += forkS2
    #world += fork

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

