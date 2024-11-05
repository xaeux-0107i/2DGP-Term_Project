from pico2d import load_image, load_font

class HealthBar:
    def __init__(self):
        self.image_empty = load_image('UI_image/empty_gauge.png') # 282 x 42
        self.image_bar = load_image('UI_image/gauge_bar.png') # 750 x 46
        self.image_sparkle = load_image('UI_image/gauge_sparkle.png')  # 24 x 48
        self.image_icon = load_image('UI_image/icon_heartLife.png') # 54 x 54
        self.dx = 0
    def draw(self):
        self.image_empty.clip_draw(0, 0, 282, 42, 240, 550, 400, 40)
        self.image_bar.clip_draw(0, 0, 400 - int(self.dx), 46, 240 - int(self.dx/2), 550, 400 - int(self.dx), 40)
        self.image_sparkle.clip_draw(0, 0, 24, 48, 436 - int(self.dx), 550, 24, 42)
        self.image_icon.clip_draw(0, 0, 54, 54, 50, 550)
    def update(self):
        self.dx += 0.1
        pass

class ScoreUI:
    def __init__(self):
        self.image = load_image('object_image/jelly_and_items/jelly.png') # 55 x 52
        self.image_empty = load_image('UI_image/empty_gauge.png')  # 282 x 42
        self.dx = 0
    def draw(self):
        self.image_empty.clip_draw(0, 0, 282, 42, 680, 550, 150, 50)
        self.image.clip_draw(0, 0, 55, 52, 630, 550, 50, 50)
        font = load_font('Arial.ttf', 30)
        font.draw(660, 550, 'score', (255,255,255))
    def update(self):
        pass