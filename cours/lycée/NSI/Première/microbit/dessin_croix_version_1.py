from microbit import *
def affiche_croix():
    affiche_slash()
    affiche_antislash()
def affiche_slash():
    x=0
    y=4
    for i in range(0,5,1):
        display.set_pixel(x,y,9)
        x=x+1
        y=y-1
def affiche_antislash():
    a=0
    b=0
    for e in range(0,5,1):
        display.set_pixel(a,b,9)
        a=a+1
        b=b+1
print(affiche_croix())
