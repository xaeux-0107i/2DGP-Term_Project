from pico2d import load_image
from state_machine import *

class Cookie:
    def __init__(self):
        self.frame = 0
        self.jump_count = 0
        self.x = 170
        self.y = 180
        self.dy = 0
        self.health = 90
        self.state_machine = StateMachine(self)
        self.state_machine.start(Jump2)
        self.state_machine.set_transitions(
            {
                Run: {down_down: Sliding},
                Sliding: {down_up: Run},
                Jump1: {down_down: Sliding, space_down: Jump2},
                Jump2: {down_down: Sliding}
            }
        )
        self.image_running = load_image('cookie_image/brave_cookie_running.png') # 칸 당 가로: 270  세로: 268
        self.image_sliding = load_image('cookie_image/brave_cookie_sliding.png')  # 칸 당 가로: 269  세로: 268
        self.image_jump = load_image('cookie_image/brave_cookie_jump.png') # 가로 270 세로 268
        self.image_jump2 = load_image('cookie_image/brave_cookie_jump2.png')
        self.state = 0 # 0 - 달리기, 1 - 점프, 2- 슬라이딩, 3 - 2단 점프 4 - 캐릭터 사망
    def draw(self):
        self.state_machine.draw()

    def update(self):
        # if self.state == 0: # 달리기
        #     self.frame = (self.frame + 1) % 4
        # if self.state == 1: # 1단 점프
        #     if self.jump_count < 5:
        #         self.frame = 0
        #         self.y += self.dy
        #         self.dy -= 1
        #     elif self.jump_count < 10:
        #         self.y += self.dy
        #         self.dy -= 1
        #         self.frame = 1
        #     elif self.jump_count < 20:
        #         self.y -= self.dy
        #         self.dy += 1
        #         self.frame = 1
        #     elif self.jump_count < 22:
        #         self.y -= self.dy
        #         self.frame = 3
        #     else:
        #         self.state = 0  # 점프가 끝나면 달리기 상태로 돌아감
        #         self.jump_count = 0  # 점프 카운트 초기화
        #         self.y = 180
        #     self.jump_count += 1
        # if self.state == 3: # 2단 점프
        #     if self.jump_count < 10:
        #         self.frame = 0
        #         self.y += self.dy
        #         self.dy -= 1
        #     elif self.jump_count < 12:
        #         self.y += self.dy
        #         self.dy -= 1
        #         self.frame = 1
        #     elif self.jump_count < 15:
        #         self.y += self.dy
        #         self.dy -= 1
        #         self.frame = 2
        #     elif self.jump_count < 18:
        #         self.y -= self.dy
        #         self.dy += 1
        #         self.frame = 3
        #     elif self.jump_count < 21:
        #         self.y -= self.dy
        #         self.dy += 1
        #         self.frame = 4
        #     else:
        #         self.y -= self.dy
        #         self.dy += 1
        #         self.frame = 5
        #
        #     if self.y <= 180:
        #         self.state = 0  # 점프가 끝나면 달리기 상태로 돌아감
        #         self.jump_count = 0  # 점프 카운트 초기화
        #         self.y = 180
        #     elif self.y <= 220:
        #         self.y -= self.dy
        #         self.dy += 1
        #         self.frame = 6
        #
        #     self.jump_count += 1
        # if self.state == 2: # 슬라이딩
        #     self.frame = (self.frame + 1) % 2
        #     self.y = 180
        # if self.health > 0:
        #     self.health -= 1
        # if self.health == 0:
        #     # 쿠키 사망 상태
        #     pass
        self.state_machine.update()
        pass

    def handle_event(self, event):
        self.state_machine.add_event(('INPUT', event))
        pass


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
        cookie.image_running.clip_draw(cookie.frame + 2 + 270 * cookie.frame, 0, 260, 268, cookie.x, cookie.y, 200, 200)

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
        cookie.image_sliding.clip_draw(cookie.frame + 270 * cookie.frame, 0, 265, 268, cookie.x, cookie.y, 200, 200)

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
        elif cookie.jump_count < 22:
                cookie.y -= cookie.dy
                cookie.frame = 3
        else:
            cookie.jump_count = 0  # 점프 카운트 초기화
            cookie.y = 180
        cookie.jump_count += 1
        pass

    @staticmethod
    def draw(cookie):
        cookie.image_jump.clip_draw(cookie.frame + 270 * cookie.frame, 0, 265, 268, cookie.x, cookie.y, 200, 200)


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

        cookie.jump_count += 1
        pass

    @staticmethod
    def draw(cookie):
        cookie.image_jump2.clip_draw(cookie.frame + 3 + 270 * cookie.frame, 0, 263, 268, cookie.x, cookie.y, 200, 200)

