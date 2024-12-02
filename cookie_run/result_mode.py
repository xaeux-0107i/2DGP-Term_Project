from pico2d import load_image, get_events, clear_canvas, update_canvas, load_font
import game_framework
from sdl2 import SDL_QUIT, SDLK_ESCAPE, SDL_KEYDOWN, SDLK_SPACE
import play_mode

def init():
    global image, box, tropy, jelly
    global font
    font = load_font('Arial.ttf', 50)
    image = load_image('background_image/result_background.png') # 844 x 315
    tropy = load_image('background_image/tropy_icon.png') # 44 x 44
    box = load_image('background_image/result_box.png') # 758 x 528
    jelly = load_image('object_image/jelly_and_items/jelly.png') # 55 x 52

def finish():
    global image
    del image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()

def draw():
    clear_canvas()
    image.clip_draw(0, 0, 800, 315, 400, 300, 800, 600)
    box.opacify(150)
    box.clip_draw(0, 0, 500, 500, 400, 300, 400, 300)
    tropy.clip_draw(0, 0, 44, 44, 400 - 150, 400, 40, 40)
    tropy.clip_draw(0, 0, 44, 44, 400 + 150, 400, 40, 40)
    jelly.clip_draw(0, 0, 55, 52, 320, 300, 50, 50)
    font.draw(320, 400, 'SCORE', (255, 255, 255))
    font.draw(370, 300, str(play_mode.cookie.score), (255, 255, 255))
    update_canvas()

def update():
    pass