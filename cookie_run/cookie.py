from pico2d import load_image, draw_rectangle, get_time
from state_machine import *
import play_mode

class Cookie:
    def __init__(self):
        self.frame = 0
        self.jump_count = 0
        self.x = 170
        self.y = 180
        self.dy = 0
        self.health = 400
        self.score = 0
        self.mode = 0
        self.start_time = 0
        self.state_machine = StateMachine(self)
        self.state_machine.start(Run)
        self.state_machine.set_transitions(
            {
                Run: {down_down: Sliding, space_down: Jump1},
                Sliding: {down_up: Run},
                Jump1: {down_down: Sliding, space_down: Jump2, change_state: Run},
                Jump2: {down_down: Sliding, change_state: Run}
            }
        )
        self.image_running = load_image('cookie_image/brave_cookie_running.png') # 칸 당 가로: 270  세로: 268
        self.image_sliding = load_image('cookie_image/brave_cookie_sliding.png')  # 칸 당 가로: 269  세로: 268
        self.image_jump = load_image('cookie_image/brave_cookie_jump.png') # 가로 270 세로 268
        self.image_jump2 = load_image('cookie_image/brave_cookie_jump2.png')
        self.dash_effect = load_image('object_image/jelly_and_items/dash_effect.png') # 198 x 136
        self.state = 0 # 0 - 달리기, 1 - 점프, 2- 슬라이딩, 3 - 2단 점프 4 - 캐릭터 사망
    def draw(self):
        self.state_machine.draw()
        if play_mode.collision_box:
            draw_rectangle(*self.get_bb())

    def update(self):
        self.state_machine.update()
        self.health -= 0.1
        if self.start_time != 0:
            current_time = get_time()
            if current_time - self.start_time > 3:
                self.mode = 0
                self.start_time = 0
        pass

    def handle_event(self, event):
        self.state_machine.add_event(('INPUT', event))
        pass
    def get_bb(self):
        if self.mode != 2:
            if self.state_machine.cur_state == Sliding:
                return self.x - 30, self.y - 100, self.x + 50, self.y - 60
            else:
                return self.x - 15, self.y - 80, self.x + 35, self.y - 20
        else:
            if self.state_machine.cur_state == Sliding:
                return self.x - 50, self.y - 100, self.x + 70, self.y - 45
            else:
                return self.x - 10, self.y - 70, self.x + 50, self.y + 30

    def handle_collision(self, group, other):
        # fill here
        if group == 'cookie:jelly':
            self.score += 1
        if group == 'cookie:obstacle':
            if self.mode == 0:
                self.health -= 5;
        if group == 'cookie:energy':
            self.health += 10
        if group == 'cookie:giant':
            self.mode = 2
            self.start_time = get_time()
        if group == 'cookie:sprint':
            self.mode = 1
            self.start_time = get_time()


class Run:
    @staticmethod
    def enter(cookie, e):
        pass

    @staticmethod
    def exit(cookie, e):
        pass

    @staticmethod
    def do(cookie):
        cookie.frame = (cookie.frame + 1) % 4
        pass

    @staticmethod
    def draw(cookie):
        if cookie.mode == 1:
            cookie.dash_effect.clip_draw(0, 0, 198, 136, cookie.x - 50, cookie.y - 50, 200, 150)
        if cookie.mode != 2:
            cookie.image_running.clip_draw(cookie.frame + 2 + 270 * cookie.frame, 0, 260, 268, cookie.x, cookie.y, 200, 200)
        else:
            cookie.image_running.clip_draw(cookie.frame + 2 + 270 * cookie.frame, 0, 260, 268, cookie.x, cookie.y + 50, 300, 300)

class Sliding:
    @staticmethod
    def enter(cookie, e):
        cookie.y = 180
        pass

    @staticmethod
    def exit(cookie, e):
        pass

    @staticmethod
    def do(cookie):
        cookie.frame = (cookie.frame + 1) % 2
        pass

    @staticmethod
    def draw(cookie):
        if cookie.mode == 1:
            cookie.dash_effect.clip_draw(0, 0, 198, 136, cookie.x - 50, cookie.y - 75, 250, 100)
        if cookie.mode != 2:
            cookie.image_sliding.clip_draw(cookie.frame + 270 * cookie.frame, 0, 265, 268, cookie.x, cookie.y, 200, 200)
        else:
            cookie.image_sliding.clip_draw(cookie.frame + 270 * cookie.frame, 0, 265, 268, cookie.x, cookie.y + 50, 300, 300)

class Jump1:
    @staticmethod
    def enter(cookie, e):
        cookie.jump_count = 0
        cookie.frame = 0
        cookie.dy = 15
        pass

    @staticmethod
    def exit(cookie, e):
        pass

    @staticmethod
    def do(cookie):
        cookie.frame = (cookie.frame + 1) % 2
        if cookie.jump_count < 5:
            cookie.frame = 0
            cookie.y += cookie.dy
            cookie.dy -= 1
        elif cookie.jump_count < 10:
             cookie.y += cookie.dy
             cookie.dy -= 1
             cookie.frame = 1
        elif cookie.jump_count < 20:
            cookie.y -= cookie.dy
            cookie.dy += 1
            cookie.frame = 1
        else:
            cookie.jump_count = 0  # 점프 카운트 초기화
            cookie.y = 180
            cookie.state_machine.add_event(('CHANGE', 0))
        cookie.jump_count += 1
        pass

    @staticmethod
    def draw(cookie):
        if cookie.mode == 1:
            cookie.dash_effect.clip_draw(0, 0, 198, 136, cookie.x - 50, cookie.y - 50, 200, 150)
        if cookie.mode != 2:
            cookie.image_jump.clip_draw(cookie.frame + 270 * cookie.frame, 0, 265, 268, cookie.x, cookie.y, 200, 200)
        else:
            cookie.image_jump.clip_draw(cookie.frame + 270 * cookie.frame, 0, 265, 268, cookie.x, cookie.y + 50, 300, 300)

class Jump2:
    @staticmethod
    def enter(cookie, e):
        cookie.jump_count = 0
        cookie.frame = 0
        cookie.dy = 15
        pass

    @staticmethod
    def exit(cookie, e):
        pass

    @staticmethod
    def do(cookie):
        if cookie.jump_count < 10:
            cookie.frame = 0
            cookie.y += cookie.dy
            cookie.dy -= 1
        elif cookie.jump_count < 12:
            cookie.y += cookie.dy
            cookie.dy -= 1
            cookie.frame = 1
        elif cookie.jump_count < 15:
            cookie.y += cookie.dy
            cookie.dy -= 1
            cookie.frame = 2
        elif cookie.jump_count < 18:
            cookie.y -= cookie.dy
            cookie.dy += 1
            cookie.frame = 3
        elif cookie.jump_count < 21:
            cookie.y -= cookie.dy
            cookie.dy += 1
            cookie.frame = 4
        else:
            cookie.y -= cookie.dy
            cookie.dy += 1
            cookie.frame = 5

        if cookie.y <= 180:
            # 점프가 끝나면 달리기 상태로 돌아감
            cookie.jump_count = 0  # 점프 카운트 초기화
            cookie.y = 180
            cookie.state_machine.add_event(('CHANGE', 0))

        cookie.jump_count += 1
        pass

    @staticmethod
    def draw(cookie):
        if cookie.mode == 1:
            cookie.dash_effect.clip_draw(0, 0, 198, 136, cookie.x - 50, cookie.y - 50, 200, 150)
        if cookie.mode != 2:
            cookie.image_jump2.clip_draw(cookie.frame + 3 + 270 * cookie.frame, 0, 263, 268, cookie.x, cookie.y, 200, 200)
        else :
            cookie.image_jump2.clip_draw(cookie.frame + 3 + 270 * cookie.frame, 0, 263, 268, cookie.x, cookie.y + 50, 300,
                                         300)

