import pgzrun
import random

WIDTH = 500
HEIGHT = 500

speed = 2

knights = []
pacman = Actor("pacman.png")
pacman.pos = 100, 100

for i in range(50):
    knights.append(Actor("knight.png", topleft=(random.randint(0, WIDTH), random.randint(0, HEIGHT))))

def update():
    if keyboard.left:
        pacman.x -= speed
    elif keyboard.right:
        pacman.x += speed
    elif keyboard.up:
        pacman.y -= speed
    elif keyboard.down:
        pacman.y += speed

def draw():
    screen.fill((0, 255, 0))
    pacman.draw()
    
    for knight in knights:
        knight.draw()

pgzrun.go()