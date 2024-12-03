from pico2d import load_image, draw_rectangle, get_time, delay, load_wav, load_music
from state_machine import *
import play_mode
import game_framework
import result_mode as next_mode

class Cookie:
    jump_sound = None
    hit_sound = None
    slide_sound = None

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
        self.unbeatable = 0
        self.hit_time = 0
        self.state_machine = StateMachine(self)
        self.state_machine.start(Run)
        self.state_machine.set_transitions(
            {
                Run: {down_down: Sliding, space_down: Jump1, dead: Death, fall:Fall},
                Sliding: {down_up: Run, dead: Death},
                Jump1: {down_down: Sliding, space_down: Jump2, change_state: Run, dead: Death, fall:Fall},
                Jump2: {down_down: Sliding, change_state: Run, dead: Death, fall:Fall},
                Death:{},
                Fall:{}
            }
        )
        self.image_running = load_image('cookie_image/brave_cookie_running.png') # 칸 당 가로: 270  세로: 268
        self.image_sliding = load_image('cookie_image/brave_cookie_sliding.png')  # 칸 당 가로: 269  세로: 268
        self.image_jump = load_image('cookie_image/brave_cookie_jump.png') # 가로 270 세로 268
        self.image_jump2 = load_image('cookie_image/brave_cookie_jump2.png')
        self.dash_effect = load_image('object_image/jelly_and_items/dash_effect.png') # 198 x 136
        self.hit_image = load_image('object_image/jelly_and_items/hit_image.png') # 758x528
        self.die_image = load_image('cookie_image/brave_cookie_die.png') # 270 x 267
        if not Cookie.jump_sound:
            Cookie.hit_sound = load_wav('sounds/crash_sound.wav')
            Cookie.hit_sound.set_volume(32)
            Cookie.jump_sound = load_wav('sounds/jump.wav')
            Cookie.jump_sound.set_volume(32)
            Cookie.slide_sound = load_wav('sounds/slide.wav')
            Cookie.slide_sound.set_volume(32)

    def draw(self):
        self.state_machine.draw()
        if play_mode.collision_box:
            draw_rectangle(*self.get_bb())
        if self.hit_time != 0: # 충돌 이펙트
            current_time = get_time()
            if current_time - self.hit_time < 0.3 and self.health > 0:
                self.hit_image.opacify(150)
                self.hit_image.clip_draw(0, 0, 758, 528, 400, 300, 800, 600)

    def update(self):
        self.state_machine.update()
        self.health -= 0.1
        current_time = get_time()
        if self.start_time != 0:
            if current_time - self.start_time > 3:
                self.mode = 0
                self.start_time = 0
        if self.hit_time != 0:
            if current_time - self.hit_time > 2:
                self.unbeatable = 0
                self.hit_time = 0
        if self.health <= 0:
            self.state_machine.add_event(('DEAD', 0))
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
            if self.state_machine.cur_state == Death:
                pass
            elif self.mode == 0 and self.unbeatable == 0:
                Cookie.hit_sound.play(1)
                self.health -= 30;
                if self.health < 0:
                    self.health = 0
                self.hit_time = get_time()
                self.unbeatable = 1
            else:
                self.score += 1
                Cookie.hit_sound.play(1)
        if group == 'cookie:energy':
            self.health += 30
        if group == 'cookie:giant':
            self.mode = 2
            self.start_time = get_time()
        if group == 'cookie:sprint':
            self.mode = 1
            self.start_time = get_time()
        if group == 'cookie:hole':
                self.y -= 20
                if self.y <= 50: # 낙사 처리
                    self.state_machine.add_event(('FALL', 0))
                print(self.y)


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
        Cookie.slide_sound.play(1)
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
        if cookie.mode == 1: # 질주화 이펙트 그리기
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
        Cookie.jump_sound.play(1)
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
        Cookie.jump_sound.play(1)
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

class Death:
    @staticmethod
    def enter(cookie, e):
        cookie.frame = 0
        cookie.y = 180
        pass

    @staticmethod
    def exit(cookie, e):
        pass

    @staticmethod
    def do(cookie):
        if cookie.frame != 4:
            cookie.frame = (cookie.frame + 1) % 5
            delay(0.3)
        if cookie.frame == 4:
            sound = load_music('sounds/game_end_sound.mp3')
            sound.set_volume(32)
            sound.play(1)
            delay(2.0)
            game_framework.change_mode(next_mode)
        pass

    @staticmethod
    def draw(cookie):
        cookie.die_image.clip_draw(cookie.frame + 270 * cookie.frame, 0, 265, 267, cookie.x, cookie.y, 200, 200)

class Fall:
    @staticmethod
    def enter(cookie, e):
        cookie.health = 0;
        pass

    @staticmethod
    def exit(cookie, e):
        pass

    @staticmethod
    def do(cookie):
        sound = load_music('sounds/game_end_sound.mp3')
        sound.set_volume(32)
        sound.play()
        delay(2.0)
        game_framework.change_mode(next_mode)
        pass

    @staticmethod
    def draw(cookie):
        pass


