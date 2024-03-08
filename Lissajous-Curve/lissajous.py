import pygame as pg
import numpy as np


if (__name__ == "__main__"):
    pg.init()
    screen_size = (300,300)
    screen = pg.display.set_mode(screen_size)

    N = 1000 # Number of sample points for drawing the lines

    # Lissajous curve parameters 
    a = 2
    b = 1
    phi = 0
    A = 110
    B = 110

    while True:
        screen.fill((0,0,0))

        # Animate
        phi = (phi+0.005)%(np.pi*2)

        x_vals = np.linspace(0,np.pi*2,N)
        y_vals = x_vals.copy()

        x_vals = list(map(lambda t: A*np.sin(a*t+phi) +screen_size[0]/2, x_vals))
        y_vals = list(map(lambda t: B*np.sin(b*t) +screen_size[1]/2, y_vals))
        
        pg.draw.aalines(screen, (255,255,255), True, list(zip(x_vals,y_vals)))
        pg.display.update()