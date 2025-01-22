import pgzrun
import random

# výška a šířka okna
HEIGHT = 500
WIDTH = 500

speed = 2
score = 0
hearts = 100
speed_knight = 2
game_over = False

# Nahrání obrázku
pacman = Actor("pacman.png")
pacman.pos = HEIGHT / 2, WIDTH / 2

ghost = Actor("ghost.png")
ghost.pos = random.randint(0, HEIGHT), random.randint(0, WIDTH)

knights = []

for i in range(5):
    knights.append(Actor("knight.png", topleft=(0, 100 * i + 20)))

def draw():
    screen.fill((0, 0, 255))

    if game_over:
        screen.draw.text(f"Konec hry! Vaše skóre je: {score}", (10, 10), color="black")
    else:
        pacman.draw()
        ghost.draw()

        for knight in knights:
            knight.draw()

        screen.draw.text(f"Skóre: {score} Životy: {hearts}", (10, 10), color="black")

def update():
    global score, hearts, speed_knight, game_over

    for knight in knights:
        knight.x += speed_knight

        if knight.x >= WIDTH:
            knight.x = 0

        if pacman.collidepoint(knight.pos):
            hearts -= 1

    if keyboard.left:
        pacman.x = pacman.x - speed
    elif keyboard.right:
        pacman.x = pacman.x + speed
    elif keyboard.up:
        pacman.y = pacman.y - speed
    elif keyboard.down:
        pacman.y = pacman.y + speed

    if pacman.collidepoint(ghost.pos):
        ghost.pos = random.randint(0, HEIGHT), random.randint(0, WIDTH)
        score = score + 1
        speed_knight += 1

    if hearts <= 0:
        game_over = True

pgzrun.go()