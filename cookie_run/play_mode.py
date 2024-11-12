from pico2d import *
import game_world
import game_framework
from random import randint
from backgound import Background, Flame
from cookie import Cookie
from mapSeed import create_map, max_num
from UI import HealthBar, ScoreUI

global speed
global count
global change

count = 0
change = 0
speed = 4

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            cookie.handle_event(event)


def init():
    global cookie
    global map1, map2
    global healthBar, scoreUI

    back_ground = Background()
    game_world.add_object(back_ground, 0)
    flame = Flame()
    game_world.add_object(flame, 0)

    map1 = create_map(0)
    map2 = create_map(randint(1, max_num))

    game_world.world[1] += map1
    game_world.world[2] += map2
    # 쿠키 생성
    cookie = Cookie()
    game_world.add_object(cookie, 3)

    # 체력바 생성
    healthBar = HealthBar()
    scoreUI = ScoreUI()

    game_world.add_object(healthBar, 4)
    game_world.add_object(scoreUI, 4)

def finish():
    game_world.clear()
    pass

def update():
    global map1, map2, count, speed, change

    count += 2 * speed
    if count % 800 == 0:
        if change % 2 == 0:
            game_world.world[1].clear()
            #map1 = create_map(randint(1, max_num))
            map1 = create_map(4)
            change += 1
            game_world.world[1] += map1
            print('map1 초기화')
        else:
            game_world.world[2].clear()
            #map2 = create_map(randint(1, max_num))
            map2 = create_map(4)
            change += 1
            game_world.world[2] += map2
            print('map2 초기화')

    game_world.update()
    delay(0.03)

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

