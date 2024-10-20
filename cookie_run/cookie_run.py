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

class Flame:
    def __init__(self):
        self.image = load_image('flame.png')
        if self.image is None:
            print("배경 이미지 로드 실패")
    def draw(self):
        self.image.clip_draw(0, 0, 860, 316, 400, 200, 800, 400)
    def update(self):
        pass

class Fence:
    def __init__(self):
        self.image = load_image('oven_fence.png')
        if self.image is None:
            print("배경 이미지 로드 실패")
    def draw(self):
        self.image.clip_draw(0, 0, 124, 120, 50, 40, 100, 80)
    def update(self):
        pass

class Cookie:
    def __init__(self):
        self.frame = 0
        self.jump_count = 0
        self.x = 170
        self.y = 180
        self.image_running = load_image('brave_cookie_running.png') # 칸 당 가로: 270  세로: 268
        self.image_sliding = load_image('brave_cookie_sliding.png')  # 칸 당 가로: 269  세로: 268
        self.image_jump = load_image('brave_cookie_jump.png') # 가로 270 세로 268
        self.state = 0 # 0 - 달리기, 1 - 점프, 2- 슬라이딩, 3 - 캐릭터 사망
    def draw(self):
        if self.state == 0: # 달리기
            self.image_running.clip_draw(self.frame + 2 + 270*self.frame, 0, 260, 268, self.x, self.y, 200, 200)
        if self.state == 1: # 점프
            self.image_jump.clip_draw(self.frame + 270*self.frame, 0, 265, 268, self.x, self.y, 200, 200)
        if self.state == 2: # 슬라이딩
            self.image_sliding.clip_draw(self.frame + 270*self.frame, 0, 265, 268, self.x, self.y, 200, 200)
    def update(self):
        if self.state == 0: # 달리기
            self.frame = (self.frame + 1) % 4
        if self.state == 1: # 점프
            if cookie.frame == 0:
                pass
            if cookie.frame == 1:
                pass
            if cookie.frame == 2:
                pass
            if cookie.frame == 4:
                pass
        if self.state == 2: # 슬라이딩
            self.frame = (self.frame + 1) % 2
        pass

def handle_events():
    global running
    global cookie
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            cookie.state = 1  # 점프
            if cookie.jump_count == 0: # 1단 점프
                cookie.frame = 0
                cookie.y += 10
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            cookie.state = 2 # 슬라이딩
        elif event.type == SDL_KEYUP and event.key == SDLK_DOWN:
            cookie.state = 0 # 달리기

def reset_world():
    global running
    global back_ground
    global world
    global flame
    global fence
    global cookie

    running = True
    world = []

    back_ground = Background()
    world.append(back_ground)
    flame = Flame()
    world.append(flame)
    fence = Fence()
    world.append(fence)
    cookie = Cookie()
    world.append(cookie)



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
    delay(0.05)

close_canvas()

