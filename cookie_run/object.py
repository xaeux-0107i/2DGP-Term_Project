from pico2d import load_image, draw_rectangle, load_music, load_wav
import game_world
import play_mode
global speed
from random import randint

speed = 4

class Fence:
    def __init__(self, x):
        self.image = load_image('object_image/obstacles/oven_fence.png')
        self.x = x #50
        self.dx = 2*speed
        if self.image is None:
            print("펜스 이미지 로드 실패")
    def draw(self):
        self.image.clip_draw(0, 0, 124, 120, self.x, 40, 100, 80)
    def update(self):
        self.x -= self.dx
        pass

class Jelly:
    jelly_sound = None

    def __init__(self, x, y):
        self.image = load_image('object_image/jelly_and_items/jelly.png')
        self.x = x #50
        self.y = y # 130
        self.dx = 2*speed
        if not Jelly.jelly_sound:
            Jelly.jelly_sound = load_wav('sounds/get_jelly.wav')
            Jelly.jelly_sound.set_volume(32)
        if self.image is None:
            print("젤리 이미지 로드 실패")
    def draw(self):
        self.image.clip_draw(0, 0, 55, 52, self.x, self.y, 40, 40)
        if play_mode.collision_box:
            draw_rectangle(*self.get_bb())
    def update(self):
        self.x -= self.dx
    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
    def handle_collision(self, group, other):
        # fill here
        if group == 'cookie:jelly':
            game_world.remove_object(self)
            Jelly.jelly_sound.play(1)

class Olive:
    def __init__(self, x):
        self.image = load_image('object_image/obstacles/olive.png')
        self.x = x #50
        self.y = 115
        self.dx = 2*speed
        if self.image is None:
            print("장애물 이미지 로드 실패")
    def draw(self):
        self.image.clip_draw(0, 0, 68, 99, self.x, 115, 50, 75)
        if play_mode.collision_box:
            draw_rectangle(*self.get_bb())
    def update(self):
        self.x -= self.dx
    def get_bb(self):
        return self.x - 20, self.y - 35, self.x + 20, self.y + 20
    def handle_collision(self, group, other):
        # fill here
        if group == 'cookie:obstacle':
            if play_mode.cookie.mode != 0:
                game_world.remove_object(self)

class Fork:
    def __init__(self, x):
        self.image = load_image('object_image/obstacles/fork.png')
        self.x = x #50
        self.dx = 2*speed
        if self.image is None:
            print("장애물 이미지 로드 실패")
    def draw(self):
        self.image.clip_draw(0, 0, 80, 113, self.x, 125, 60, 90)
        if play_mode.collision_box:
            draw_rectangle(*self.get_bb())
    def update(self):
        self.x -= self.dx
    def get_bb(self):
        return self.x - 20, 125 - 45, self.x + 20, 125 + 40
    def handle_collision(self, group, other):
        # fill here
        if group == 'cookie:obstacle':
            if play_mode.cookie.mode != 0:
                game_world.remove_object(self)



class ForkS1:
    def __init__(self, x):
        self.image = load_image('object_image/obstacles/fork_with_sausage.png')
        self.x = x #50
        self.dx = 2*speed
        if self.image is None:
            print("장애물 이미지 로드 실패")
    def draw(self):
        self.image.clip_draw(0, 0, 106, 193, self.x, 160, 80, 160)
        if play_mode.collision_box:
            draw_rectangle(*self.get_bb())
    def update(self):
        self.x -= self.dx
    def get_bb(self):
        return self.x - 30, 160 - 80, self.x + 10, 160 + 75
    def handle_collision(self, group, other):
        # fill here
        if group == 'cookie:obstacle':
            if play_mode.cookie.mode != 0:
                game_world.remove_object(self)

class ForkS2:
    def __init__(self, x):
        self.image = load_image('object_image/obstacles/fork_with_sausage2.png')
        self.x = x #50
        self.dx = 2*speed
        if self.image is None:
            print("장애물 이미지 로드 실패")
    def draw(self):
        self.image.clip_draw(0, 0, 134, 482, self.x, 400, 100, 500)
        if play_mode.collision_box:
            draw_rectangle(*self.get_bb())
    def update(self):
        self.x -= self.dx
    def get_bb(self):
        return self.x - 40, 400 - 240, self.x + 40, 400 + 250
    def handle_collision(self, group, other):
        # fill here
        if group == 'cookie:obstacle':
            if play_mode.cookie.mode != 0:
                game_world.remove_object(self)

class Poision:
    def __init__(self, x, y):
        self.image = load_image('object_image/obstacles/poision.png')
        self.x = x # 50
        self.y = y # 400
        self.frame = randint(0, 1)
        self.count = 0
        self.dx = 2*speed
        if self.image is None:
            print("장애물 이미지 로드 실패")
    def draw(self):
        self.image.clip_draw(self.frame*180, 0, 180, 214, self.x, self.y, 180, 200)
        if play_mode.collision_box:
            draw_rectangle(*self.get_bb())
    def update(self):
        self.x -= self.dx
        self.count += 1
        if self.count % 3 == 0:
            self.frame = int(self.frame + 1) % 2
    def get_bb(self):
        return self.x - 55, self.y - 35, self.x - 5, self.y + 15
    def handle_collision(self, group, other):
        # fill here
        if group == 'cookie:obstacle':
            if play_mode.cookie.mode != 0:
                game_world.remove_object(self)

class Hole:
    def __init__(self, x):
        self.x = x #50
        self.y = 40
        self.dx = 2*speed
    def draw(self):
        if play_mode.collision_box:
            draw_rectangle(*self.get_bb())
    def update(self):
        self.x -= self.dx
    def get_bb(self):
        return self.x - 20, self.y - 40, self.x + 20, self.y + 60
    def handle_collision(self, group, other):
        # fill here
        if group == 'cookie:hole':
            pass