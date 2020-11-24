import pygame
import random
import time

WIDTH = 800
HEIGHT = 800
FPS = 30

# initialize Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grid")
clock = pygame.time.Clock()
white = [255, 255, 255]
black = [0,0,0]
screen.fill(white)
pygame.display.update()
n = int(input("nxn matrix dimension = "))
x = 0
y = 0
#Starting Coordinates
visited = []
stack = []
grid = []
#Dimensions of Box
h = HEIGHT/n
w = WIDTH/n

#Draws out a grid with a specified dimension
def drawGrid(w, h, x , y):
    for i in range(n):
        x= w
        y=y + h
        pygame.draw.line(screen, black, ((w/n)*i,0), ((w/n)*i,h) ,1)
        for j in range(n):
            pygame.draw.line(screen, black, (0,(h/n)*j), (w,(h/n)*j) ,1)
            grid.append((x,y))
            x = x + w

#Draws a cell from a starting coordinate
def makeCell(x, y):
    pygame.draw.rect(screen, white, (x, y, w+1, h+1))

#Moves up from the starting coordinate and draws cell
def up(x, y):
    pygame.draw.rect(screen, white, (x+1, y-h+1, w-2, h+1))
    pygame.display.update()

#Moves down from starting coordinate and draws cell
def down(x, y):
    pygame.draw.rect(screen, white, (x+1, y+h, w-2, h))
    pygame.display.update()

#Moves right from the starting coordinate and draws cell
def right(x, y):
    pygame.draw.rect(screen, white, (x+w, y+1, w-1, h-2))
    pygame.display.update()

#Moves left from the starting coordinate and draws cell
def left(x, y):
    pygame.draw.rect(screen, white, (x-w+1, y+1, w, h-2))
    pygame.display.update()

def makeMaze(x,y):
    makeCell(x,y)
    stack.append((x,y))
    visited.append((x,y))
    print(len(stack))
    print(len(grid))
    while len(stack) > 0:
        time.sleep(.007)
        cell = []
        if (x+w,y) not in visited and (x+w,y) in grid: #Check if right cell is available
            cell.append("right")                        #If available then add to the instructions
        if (x-w,y) not in visited and (x-w,y) in grid:
            cell.append("left")
        if (x,y+h) not in visited and (x,y+h) in grid:
            cell.append("down")
        if (x,y-h) not in visited and (x,y-h) in grid:
            cell.append("up")

        print(len(cell))
        if len(cell) > 0:
            action = (random.choice(cell))

            if action == "right":
                right(x, y)
                x = x + w
                visited.append((x,y))
                stack.append((x,y))
            elif action == "left":
                left(x, y)
                x = x-w
                visited.append((x,y))
                stack.append((x,y))
            elif action == "up":
                up(x, y)
                y = y - h
                visited.append((x,y))
                stack.append((x,y))
            elif action == "down":
                down(x, y)
                y = y + h
                visited.append((x,y))
                stack.append((x,y))
        else:
            x, y = stack.pop()

drawGrid(WIDTH, HEIGHT, x, y)
makeMaze(x,y) 


pygame.display.update()
running = True
while running:
    # keep running at the at the right speed
    clock.tick(FPS)
    # process input (events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False


