from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('Background1.png')
        if self.image is None:
            print("이미지 로드 실패")

    def draw(self):
        self.image.clip_draw(0, 0, 567, 320, 400, 300, 800, 600)

open_canvas()

back_ground = Background()

back_ground.draw()

update_canvas()
delay(10)

close_canvas()

