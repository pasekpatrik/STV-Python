import pgzrun
import library

TILE_SIZE = 32
WIDTH = 20 * TILE_SIZE
HEIGHT = 15 * TILE_SIZE
speed = 5

player = Actor("player")

def draw():
    screen.clear()

    library.render(screen, 32, Actor)
    player.draw()

def update():
    collision = True

    new_x = player.x
    new_y = player.y

    if keyboard.right:
        new_x += speed
    if keyboard.left:
        new_x -= speed
    if keyboard.down:
        new_y += speed
    if keyboard.up:
        new_y -= speed

    if new_x < 0 + TILE_SIZE / 2:
        collision = False
    if new_y < 0 + TILE_SIZE / 2:
        collision = False

    if new_x > WIDTH - TILE_SIZE / 2:
        collision = False
    if new_y > HEIGHT - TILE_SIZE / 2:
        collision = False

    if library.handleCollisonWall(new_x, new_y, TILE_SIZE) == False:
        collision = False

    if collision:
        player.x = new_x
        player.y = new_y

pgzrun.go()