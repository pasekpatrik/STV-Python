import pgzrun
import random

# Nahrání obrázku a pozice
ghost = Actor("ghost.png")
ghost.pos = 100, 200

# Šířka a Výška okna
WIDTH = 500
HEIGHT = 500

# Vykreslení obrazovky
def draw():
    screen.fill((255, 255, 255))
    ghost.draw()

# def update():
#     ghost.left = ghost.left + 2

#     if ghost.left > WIDTH:
#         ghost.left = 0

# Kliknutí myší na okno
def on_mouse_down(pos):
    if ghost.collidepoint(pos):
        ghost.pos = random.randint(0, WIDTH), random.randint(0, HEIGHT)

pgzrun.go()