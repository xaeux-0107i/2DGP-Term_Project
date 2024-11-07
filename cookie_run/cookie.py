from pico2d import load_image
from state_machine import StateMachine
class Cookie:
    def __init__(self):
        self.frame = 0
        self.jump_count = 0
        self.x = 170
        self.y = 180
        self.dy = 0
        self.health = 90
        self.state_machine = StateMachine(self)
        self.state_machine.start(Run)
        self.image_running = load_image('cookie_image/brave_cookie_running.png') # 칸 당 가로: 270  세로: 268
        self.image_sliding = load_image('cookie_image/brave_cookie_sliding.png')  # 칸 당 가로: 269  세로: 268
        self.image_jump = load_image('cookie_image/brave_cookie_jump.png') # 가로 270 세로 268
        self.image_jump2 = load_image('cookie_image/brave_cookie_jump2.png')
        self.state = 0 # 0 - 달리기, 1 - 점프, 2- 슬라이딩, 3 - 2단 점프 4 - 캐릭터 사망
    def draw(self):
        # if self.state == 0: # 달리기
        #     self.image_running.clip_draw(self.frame + 2 + 270*self.frame, 0, 260, 268, self.x, self.y, 200, 200)
        # if self.state == 1: # 점프
        #     self.image_jump.clip_draw(self.frame + 270*self.frame, 0, 265, 268, self.x, self.y, 200, 200)
        # if self.state == 2: # 슬라이딩
        #     self.image_sliding.clip_draw(self.frame + 270*self.frame, 0, 265, 268, self.x, self.y, 200, 200)
        # if self.state == 3: # 2단 점프
        #     self.image_jump2.clip_draw(self.frame + 3 + 270 * self.frame, 0, 263, 268, self.x, self.y, 200, 200)
        self.state_machine.draw()
        pass

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