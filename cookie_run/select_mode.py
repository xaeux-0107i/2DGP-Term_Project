from pico2d import load_image, get_events, clear_canvas, update_canvas, load_music,delay, load_font
import game_framework
from sdl2 import SDL_QUIT, SDLK_ESCAPE, SDL_KEYDOWN, SDLK_RETURN, SDL_MOUSEBUTTONDOWN
import play_mode

def init():
    global image
    global sound
    global box
    global brave, cherry, angel, kiwi
    global selectNum
    image = load_image('background_image/result_background.png')  # 844 x 315
    box = load_image('background_image/result_box.png')  # 758 x 528
    brave = load_image('cookie_image/brave_shop.png')
    kiwi = load_image('cookie_image/kiwi_shop.png')
    cherry = load_image('cookie_image/cherry_shop.png')
    angel = load_image('cookie_image/angel_shop.png')
    sound = load_music('sounds/game_start_sound.mp3')
    sound.set_volume(32)
    selectNum = 0

def finish():
    global image
    del image
    global box
    del box

def handle_events():
    global name
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RETURN): # 게임 시작
            global sound
            sound.play(1)
            delay(3)
            game_framework.change_mode(play_mode)
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == 1: # 마우스 클릭
            global selectNum
            if (event.x >= 50) and (event.x <= 150) and (600 - event.y <= 350) and (600 - event.y >= 250):
                selectNum = 1
            elif (event.x >= 250) and (event.x <= 350) and (600 - event.y <= 350) and (600 - event.y >= 250):
                selectNum = 2
            elif (event.x >= 450) and (event.x <= 550) and (600 - event.y <= 350) and (600 - event.y >= 250):
                selectNum = 3
            elif (event.x >= 650) and (event.x <= 750) and (600 - event.y <= 350) and (600 - event.y >= 250):
                selectNum = 4
        else:
            pass


def draw():
    clear_canvas()
    image.clip_draw(0, 0, 800, 315, 400, 300, 800, 600)
    box.opacify(150)
    box.clip_draw(0, 0, 500, 500, 200 * selectNum - 100, 300, 200, 300)
    brave.clip_draw(0, 0, 340, 340, 100, 300, 200, 200)
    angel.clip_draw(0, 0, 340, 338, 300, 300, 200, 200)
    cherry.clip_draw(0, 0, 340, 375,500, 300, 200, 200)
    kiwi.clip_draw(0, 0, 340, 340, 700, 300, 200, 200)
    #font = load_font('Arial.ttf', 50)
    #font.draw(50, 500 ,"Name", (255, 255, 255))
    update_canvas()

def update():
    pass