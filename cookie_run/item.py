from pico2d import load_image, draw_rectangle, load_wav
import game_world
import play_mode
global speed
speed = 4

class Energy:
    energy_sound = None

    def __init__(self, x, y):
        self.image = load_image('object_image/jelly_and_items/energy_item.png')
        self.x = x #50
        self.y = y
        self.dx = 2*speed
        self.frame = 0
        self.count = 0
        if self.image is None:
            print("포션 이미지 로드 실패")
        if not Energy.energy_sound:
            Energy.energy_sound = load_wav('sounds/get_energy.wav')
    def draw(self):
        self.image.clip_draw(146 * self.frame, 0, 140, 142, self.x, self.y, 100, 100)
        if play_mode.collision_box:
            draw_rectangle(*self.get_bb())
    def update(self):
        self.x -= self.dx
        self.count += 1
        if self.count % 8 ==0:
            self.frame = (self.frame+1)%4
    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25
    def handle_collision(self, group, other):
        # fill here
        if group == 'cookie:energy':
            game_world.remove_object(self)
            Energy.energy_sound.play(1)

class Giant:
    giant_sound = None

    def __init__(self, x, y):
        self.image = load_image('object_image/jelly_and_items/giant_item.png')
        self.x = x #50
        self.y = y
        self.dx = 2*speed
        self.frame = 0
        self.count = 0
        if self.image is None:
            print("거대화 이미지 로드 실패")
        if not Giant.giant_sound:
            Giant.giant_sound = load_wav('sounds/get_jelly.wav')
    def draw(self):
        self.image.clip_draw(92 * self.frame, 0, 88, 88, self.x, self.y, 100, 100)
        if play_mode.collision_box:
            draw_rectangle(*self.get_bb())
    def update(self):
        self.x -= self.dx
        self.count += 1
        if self.count % 8 ==0:
            self.frame = (self.frame+1)%4
    def get_bb(self):
        return self.x - 45, self.y - 50, self.x + 45, self.y + 45
    def handle_collision(self, group, other):
        # fill here
        if group == 'cookie:giant':
            game_world.remove_object(self)
            Giant.giant_sound.play(1)

class Sprint:
    sprint_sound = None

    def __init__(self, x, y):
        self.image = load_image('object_image/jelly_and_items/dash_item.png')
        self.x = x #50
        self.y = y
        self.dx = 2*speed
        self.frame = 0
        self.count = 0
        if self.image is None:
            print("질주화 이미지 로드 실패")
        if not Sprint.sprint_sound:
            Sprint.sprint_sound = load_wav('sounds/get_jelly.wav')
    def draw(self):
        self.image.clip_draw(92 * self.frame, 0, 88, 88, self.x, self.y, 100, 100)
        if play_mode.collision_box:
            draw_rectangle(*self.get_bb())
    def update(self):
        self.x -= self.dx
        self.count += 1
        if self.count % 8 ==0:
            self.frame = (self.frame+1)%4
    def get_bb(self):
        return self.x - 45, self.y - 50, self.x + 45, self.y + 45
    def handle_collision(self, group, other):
        # fill here
        if group == 'cookie:sprint':
            game_world.remove_object(self)
            Sprint.sprint_sound.play(1)