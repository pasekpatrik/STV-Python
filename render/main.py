import pgzrun

TILE_SIZE = 32

HEIGHT = TILE_SIZE * 15
WIDTH = TILE_SIZE * 20

def draw():
    y = 0
    x = 0

    with open("level1.txt", "r") as reader:
        for radek in reader.readlines():
            x = 0

            for char in radek.strip():

                if char == "0":
                    screen.blit("grass", (x, y))
                if char == "1":
                    screen.blit("wall", (x, y))

                x += TILE_SIZE
                
            y += TILE_SIZE

def update():
    pass

pgzrun.go()