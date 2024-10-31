from pico2d import load_image

global speed
speed = 4


class Background:
    def __init__(self):
        self.image = load_image('background_image/Background1.png')
        self.speed = speed
        self.dx = 0
        if self.image is None:
            print("배경 이미지 로드 실패")
    def draw(self):
        self.image.clip_draw(0, 0, 567, 320, 400 - self.dx, 300, 800, 600)
        self.image.clip_draw(0, 0, 567, 320, 1200 - self.dx, 300, 800, 600)
    def update(self):
        if self.dx > 800:
            self.dx = 0
        else:
            self.dx += self.speed


class Flame:
    def __init__(self):
        self.image = load_image('background_image/flame.png')
        self.dx = 0
        self.speed = speed
        if self.image is None:
            print("불꽃 이미지 로드 실패")
    def draw(self):
        self.image.clip_draw(0, 0, 860, 316, 400 - int(self.dx), 200, 800, 400)
        self.image.clip_draw(0, 0, 860, 316, 1200 - int(self.dx), 200, 800, 400)
    def update(self):
        if self.dx > 800:
            self.dx = 0
        else:
            self.dx += self.speed
