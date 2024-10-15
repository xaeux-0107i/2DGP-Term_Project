from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('Background1.png')
        if self.image is None:
            print("배경 이미지 로드 실패")
    def draw(self):
        self.image.clip_draw(0, 0, 567, 320, 400, 300, 800, 600)
    def update(self):
        pass

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global back_ground
    global world

    running = True
    world = []

    back_ground = Background()
    world.append(back_ground)

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

close_canvas()

