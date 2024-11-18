from pico2d import *
import game_world
import game_framework
from random import randint
from backgound import Background, Flame
from cookie import Cookie
from mapSeed import create_map, max_num, create_energy_map
from UI import HealthBar, ScoreUI
from item import Energy

global speed
global count
global change
global collision_box

count = 0
change = 0
speed = 4
collision_box = False

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_c:
            global collision_box
            if collision_box:
                collision_box = False
            else:
                collision_box = True
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

    create_map(0, 1)
    create_map(randint(1, max_num), 2)

    # 쿠키 생성
    cookie = Cookie()
    game_world.add_object(cookie, 4)

    # 체력바 생성
    healthBar = HealthBar()
    scoreUI = ScoreUI()

    game_world.add_object(healthBar, 4)
    game_world.add_object(scoreUI, 4)

    game_world.add_collision_pairs('cookie:obstacle', cookie, None)
    game_world.add_collision_pairs('cookie:jelly', cookie, None)
    game_world.add_collision_pairs('cookie:energy', cookie, None)
    game_world.add_collision_pairs('cookie:giant', cookie, None)
    game_world.add_collision_pairs('cookie:sprint', cookie, None)

def finish():
    game_world.clear()
    pass

def update():
    global count, speed, change

    count += 2 * speed
    if count % 800 == 0:
        if change % 10 == 0 and change >= 10:
            if change % 2 == 0:
                for o in game_world.objects[1]:
                    game_world.remove_object(o)
                create_energy_map(0, 1)
                change += 1
                print('map1 물약 생성')
            else:
                for o in game_world.objects[2]:
                    game_world.remove_object(o)
                create_energy_map(0, 2)
                change += 1
                print('map2 물약 생성')
        else :
            if change % 2 == 0:
                for o in game_world.objects[1]:
                    game_world.remove_object(o)
                create_map(randint(1, max_num), 1)
                change += 1
                print('map1 초기화')
            else:
                for o in game_world.objects[2]:
                    game_world.remove_object(o)
                create_map(randint(1, max_num), 2)
                change += 1
                print('map2 초기화')

    game_world.update()
    game_world.handle_collisions()
    delay(0.02)

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

