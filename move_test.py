from pico2d import *
import random

randX = random.randrange(1, 1281)
randY = random.randrange(1, 1025)

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_Quit:
            running = False
        # elif event.type == SDL_MOUSEMOTION:
        #     x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

running = True
x = 100
y = 100
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    arrow.draw(randX, randY)
    if x < randX and y < randY:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8

        if x < randX:
            x += 5
        elif x == randX:
            x = randX
        elif y < randY:
            y += 5
        elif y == randY:
            y = randY

        delay(0.01)
        get_events()


    handle_events()

close_canvas()