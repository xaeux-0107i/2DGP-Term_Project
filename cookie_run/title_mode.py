from pico2d import load_image, get_events, clear_canvas, update_canvas, load_music,delay, load_font
import game_framework
from sdl2 import SDL_QUIT, SDLK_ESCAPE, SDL_KEYDOWN, SDLK_BACKSPACE, SDLK_RETURN, SDL_GetKeyboardState, SDLK_LSHIFT, SDLK_RSHIFT
import play_mode

def init():
    global image
    global sound
    global name
    global gaugeBar
    image = load_image('background_image/title.png')
    gaugeBar = load_image('UI_image/empty_gauge.png')
    sound = load_music('sounds/game_start_sound.mp3')
    sound.set_volume(32)
    name = ""

def finish():
    global image
    del image

def handle_events():
    global name
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RETURN):
            global sound
            sound.play(1)
            delay(3)
            game_framework.change_mode(play_mode)
        elif event.key == SDLK_BACKSPACE and len(name) > 0:
            name = name[:-1]  # 이름에서 마지막 글자
        elif event.type == SDL_KEYDOWN:
            if len(name) < 10:  # 이름 최대 길이 제한
                char = chr(event.key)  # 키 값을 문자로 변환
                if char.isalnum():
                    name += char
        else:
            pass


def draw():
    clear_canvas()
    image.clip_draw(0, 0, 910, 512, 400, 300, 800, 600)
    gaugeBar.clip_draw(0, 0, 282, 42, 400, 50, 600, 100)
    font = load_font('Arial.ttf', 50)
    font.draw(150, 50 ,"Name : ", (255, 255, 255))
    font.draw(350, 50, str(name), (255, 255, 255))
    update_canvas()

def update():
    pass