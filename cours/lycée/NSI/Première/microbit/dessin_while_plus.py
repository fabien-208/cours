from microbit import *
x=0
y=2
b=0
a=2
while (x,y,9)<=(4,2,9):
    display.set_pixel(x,y,9)
    x=x+1
while (a,b,9)<=(2,4,9):
    display.set_pixel(a,b,9)
    b=b+1