import sys
import ctypes
from sdl2 import *
window=None
renderer=None

def Bresenhamsan_line_algorithm(x0, y0,xn, yn):
    dx=abs(xn-x0)
    dy=abs(yn-y0)
    if xn>x0:
        lx=1
    else:
        lx=-1
    if yn>y0:
        ly=1
    else:
        ly=-1
    print(x0,y0)
    SDL_RenderDrawPoint(renderer, int(x0), int(y0))

    if dx>dy:
        pk=2*dy-dx
        for i in range (0,dx):
            if pk<0:
                x0=x0+lx
                y0=y0
                pk=pk+2*dy
            else:
                x0=x0+lx
                y0=y0+ly
                pk=pk+2*dy-2*dx
            print(pk,x0,y0)
            SDL_RenderDrawPoint(renderer, int(x0), int(y0))
    else:
        pk=2*dx-dy
        for i in range(0,dy):
            if pk<0:
                x0=x0
                y0=y0+ly
                pk=pk+2*dx
            else:
                x0=x0+lx
                y0=y0+ly
                pk=pk+2*dx-2*dy
            print(pk,x0,y0)
            SDL_RenderDrawPoint(renderer, int(x0), int(y0))






def main():
    global window, renderer
    print("Enter values")
    x0=int(input())
    y0=int(input())
    xn=int(input())
    yn=int(input())
    
    SDL_Init(SDL_INIT_VIDEO)
    window = SDL_CreateWindow(b"Bresenhamsan's Line Drawing Algorithm",
                              SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
                              592, 460, SDL_WINDOW_SHOWN)
    
    renderer = SDL_CreateRenderer(window,-1,0)

    # set background color and clear to apply it
    SDL_SetRenderDrawColor(renderer,0,0,0,255)
    SDL_RenderClear(renderer)

    # set line color
    SDL_SetRenderDrawColor(renderer,169,78,56,255)

    # draw line
    Bresenhamsan_line_algorithm(x0,y0,xn,yn)

    # render to the window
    SDL_RenderPresent(renderer)

    # run the window
    running = True
    event = SDL_Event()
    while running:
        while SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == SDL_QUIT:
                running = False
                break

    # destroy the window
    SDL_DestroyWindow(window)
    SDL_Quit()
    return 0

if __name__ == "__main__":
    sys.exit(main())