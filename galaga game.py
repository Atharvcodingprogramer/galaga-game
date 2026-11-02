import pgzrun
WIDTH = 600
HEIGHT = 600
TITLE = "galaga game"
import random

ship = Actor("galaga")
bug = Actor("bug")

bullets = []


ship.pos = (450,550)
bug.pos = (random.randint(0,600),0)



def draw() :
    screen.blit("bg",(0,0))
    ship.draw()
    bug.draw()
    for bullet in bullets :
        bullet.draw()


def update() :
    if keyboard.left :
        ship.x = ship.x-2
    if keyboard.right :
        ship.x = ship.x+2
    if keyboard.space :
        bullet = Actor("bullet")
        bullet.pos = (ship.pos)
        bullets.append(bullet)
    for bullet in bullets :
            
        bullet.y = bullet.y+2 
        if bullet.colliderect(bug) :
            bug.pos = (random.randint(0,600),0)
            bullets.remove(bullet)
    bug.y = bug.y+4
    if bug.y > 600 :
        bug.pos = (random.randint(0,600),0)
pass
pgzrun.go()
