import pgzrun

WIDTH = 600
HEIGHT = 400

# Nahrání obrázku
player = Actor("player.png")

def draw():
    screen.fill((200, 200, 200))

    player.draw()

def update():
    
    if keyboard.left:
        player.x = player.x - 5
    elif keyboard.right:
        player.x = player.x + 5

pgzrun.go()