import pgzrun , random

WIDTH=500
HEIGHT=500
TITLE="gem catcher"
gem=Actor("gemblue")
gem.x=random.randint(20,480)
gem.y=20
score=0
ship=Actor("ship")
ship.x=350
ship.y=450
gameover=False






def draw():
    screen.clear()
    screen.fill("pink")
    gem.draw()
    ship.draw()
    if gameover:
       screen.draw.text("Game over",(250,40),color=(255,255,255),fontsize=60)
    else:

        screen.draw.text("SCORE "+str(score),(250,40),color=(255,255,255),fontsize=60)
   


def update():
    global score
    if keyboard.left:
        ship.x=ship.x-5
    if keyboard.right:
        ship.x=ship.x+5
    gem.y=gem.y+1
    if gem.y > HEIGHT:
       gameover=True

    if gem.colliderect(ship):

        gem.x = random.randint(20, 600)

        gem.y = 0

        score = score + 1
  









pgzrun.go()