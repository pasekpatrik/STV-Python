import pgzrun

TILE_SIZE = 32

WIDTH = TILE_SIZE * 20
HEIGHT = TILE_SIZE * 15

# Nahrání obrázku
player = Actor("player.png")

wall = Actor("wall.png")
wall.pos = TILE_SIZE * 3, TILE_SIZE * 3

def draw():
    screen.fill((200, 200, 200))

    for y in range(0, HEIGHT, 32):
        for x in range(0, WIDTH, 32):
            screen.blit("grass", (x, y))

    wall.draw()
    player.draw()

def update():
    collision = True

    new_x = player.x
    new_y = player.y 

    if keyboard.left:
        new_x = new_x - 5
    if keyboard.right:    
        new_x = new_x + 5
    if keyboard.up:
        new_y = new_y - 5
    if keyboard.down:
        new_y = new_y + 5

    if new_x > WIDTH - 32/2:
       collision = False
    if new_x < 0 + TILE_SIZE/2:
        collision = False

    if new_y > HEIGHT - TILE_SIZE/2:
        collision = False
    if new_y < 0 + TILE_SIZE/2:
        collision = False

    # if new_x + TILE_SIZE/2 > wall.x and new_y + TILE_SIZE/2 > wall.y:
    #     print(wall.x)
    #     collision = False

    if collision:
        player.x = new_x
        player.y = new_y

pgzrun.go()