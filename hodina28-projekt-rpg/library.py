walls = []

def render(sc, size, Actor):
    walls.clear()
    x = 0
    y = 0

    with open("lvl1.txt", "r") as reader:
        for radek in reader.readlines():
            x = 0

            for char in radek.strip():

                if char == "0":
                    sc.blit("grass", (x, y))
                if char == "1":
                    wall = Actor("wall", topleft=(x, y))
                    wall.draw()
                    walls.append(wall)

                x += size
                
            y += size

def handleCollisonWall(new_x, new_y, TILE_SIZE):
    collision = True

    for wall in walls:
        if new_x > wall.x - TILE_SIZE and new_x - TILE_SIZE < wall.x and new_y > wall.y - TILE_SIZE and new_y - TILE_SIZE < wall.y:
            collision = False

    return collision