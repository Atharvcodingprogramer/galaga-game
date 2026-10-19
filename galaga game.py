import pgzrun
WIDTH = 600
HEIGHT = 600
TITLE = "galaga game"


ship = Actor("galaga")
bug = Actor("bug")




ship.pos = (450,450)



def draw() :
    screen.blit("bg",(0,0))
    ship.draw()
    bug.draw()


def update() :
    if keyboard.left :
            ship.x = ship.x-2
    if keyboard.right :
            ship.x = ship.x+2
    pass
pgzrun.go()