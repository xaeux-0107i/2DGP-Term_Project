from pico2d import load_image
import game_world
global speed
speed = 4

class Energy:
    def __init__(self, x, y):
        self.image = load_image('object_image/jelly_and_items/energy_item.png')
        self.x = x #50
        self.y = y
        self.dx = 2*speed
        self.frame = 0
        self.count = 0
        if self.image is None:
            print("포션 이미지 로드 실패")
    def draw(self):
        self.image.clip_draw(146 * self.frame, 0, 140, 142, self.x, self.y, 100, 100)
    def update(self):
        #self.x -= self.dx
        self.count += 1
        if self.count % 8 ==0:
            self.frame = (self.frame+1)%4
    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25
    def handle_collision(self, group, other):
        # fill here
        if group == 'cookie:energy':
            game_world.remove_object(self)

class Giant:
    def __init__(self, x, y):
        self.image = load_image('object_image/jelly_and_items/giant_item.png')
        self.x = x #50
        self.y = y
        self.dx = 2*speed
        self.frame = 0
        self.count = 0
        if self.image is None:
            print("거대화 이미지 로드 실패")
    def draw(self):
        self.image.clip_draw(91 * self.frame, 0, 90, 88, self.x, self.y, 100, 100)
    def update(self):
        #self.x -= self.dx
        self.count += 1
        if self.count % 8 ==0:
            self.frame = (self.frame+1)%4
    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25
    def handle_collision(self, group, other):
        # fill here
        if group == 'cookie:giant':
            game_world.remove_object(self)

class Sprint:
    def __init__(self, x, y):
        self.image = load_image('object_image/jelly_and_items/dash_item.png')
        self.x = x #50
        self.y = y
        self.dx = 2*speed
        self.frame = 0
        self.count = 0
        if self.image is None:
            print("질주화 이미지 로드 실패")
    def draw(self):
        self.image.clip_draw(146 * self.frame, 0, 140, 142, self.x, self.y, 100, 100)
    def update(self):
        #self.x -= self.dx
        self.count += 1
        if self.count % 8 ==0:
            self.frame = (self.frame+1)%4
    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25
    def handle_collision(self, group, other):
        # fill here
        if group == 'cookie:sprint':
            game_world.remove_object(self)