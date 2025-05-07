import pgzrun
import library

TILE_SIZE = 32
WIDTH = 20 * TILE_SIZE
HEIGHT = 15 * TILE_SIZE
speed = 5

player = Actor("player")

def draw():
    library.render(screen, 32)
    player.draw()

def update():
    if keyboard.right:
        player.x = player.x + speed
    if keyboard.left:
        player.x = player.x - speed
    if keyboard.down:
        player.y = player.y + speed
    if keyboard.up:
        player.y = player.y - speed

pgzrun.go()