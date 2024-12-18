from pico2d import load_image, get_events, clear_canvas, update_canvas, load_music,delay, load_font
import game_framework
from sdl2 import SDL_QUIT, SDLK_ESCAPE, SDL_KEYDOWN, SDLK_SPACE
import play_mode

def init():
    global image
    global sound
    image = load_image('background_image/title.png')
    sound = load_music('sounds/game_start_sound.mp3')
    sound.set_volume(32)

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
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            global sound
            sound.play(1)
            delay(3)
            game_framework.change_mode(play_mode)

def draw():
    clear_canvas()
    image.clip_draw(0, 0, 910, 512, 400, 300, 800, 600)
    font = load_font('Arial.ttf', 50)
    font.draw(150, 50, "Press space bar to start", (255, 255, 255))
    update_canvas()

def update():
    pass