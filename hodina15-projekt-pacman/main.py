import pgzrun
import random

# výška a šířka okna
HEIGHT = 500
WIDTH = 500

speed = 2
score = 0
hearts = 3

# Nahrání obrázku
pacman = Actor("pacman.png")
pacman.pos = HEIGHT / 2, WIDTH / 2

ghost = Actor("ghost.png")
ghost.pos = random.randint(0, HEIGHT), random.randint(0, WIDTH)

knight = Actor("knight")
knight.pos = 0, WIDTH / 2

def draw():
    screen.fill((0, 0, 255))

    pacman.draw()
    ghost.draw()
    knight.draw()

    screen.draw.text(f"Skóre: {score} Životy: {hearts}", (10, 10), color="black")

def update():
    global score
    global hearts
    knight.x = knight.x + 2

    if knight.left > WIDTH:
        knight.x = 0 
    
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

    if pacman.collidepoint(knight.pos):
        hearts = hearts - 1


pgzrun.go()