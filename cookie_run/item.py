from pico2d import load_image
global speed
speed = 4

class Energy:
    def __init__(self, x):
        self.image = load_image('object_image/jelly_and_items/energy_item.png')
        self.x = x #50
        self.dx = 2*speed
        self.frame = 0
        self.count = 0
        if self.image is None:
            print("포션 이미지 로드 실패")
    def draw(self):
        self.image.clip_draw(146 * self.frame, 0, 140, 142, self.x, 300, 100, 100)
    def update(self):
        #self.x -= self.dx
        self.count += 1
        if self.count % 8 ==0:
            self.frame = (self.frame+1)%4
        pass
    pass

class Giant:
    pass

class Sprint:
    pass