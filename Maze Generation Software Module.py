import pygame
import random

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

#Initializing dimension VIA user input
n = int(input("nxn matrix dimension = "))
#Initial starting coordinates
x = 0
y = 0
#Dimensions of Cell
h = HEIGHT/n
w = WIDTH/n

#Draws out a grid with a specified dimension
def drawGrid(w, h):
    for i in range(n):
        pygame.draw.line(screen, black, ((w/n)*i,0), ((w/n)*i,h) ,1)
        for j in range(n):
            pygame.draw.line(screen, black, (0,(h/n)*j), (w,(h/n)*j) ,1)


#Moves down from starting coordinate and draws cell
    #Starting coordinate scales with cell dimensions
def down(x, y):
    pygame.draw.rect(screen, white, (x*w+1, h*y-1, w-1, h+1))
    pygame.display.update()

#Moves right from the starting coordinate and draws cell
    #Starting coordinate scales with cell dimensions
def right(x, y):
    pygame.draw.rect(screen, white, (x*w, h*y+1, w, h-1))
    pygame.display.update()

#Generate maze VIA binary tree algorithm
def makeMaze():
    for i in range(n):
        right(i,0)                  #makes the first column and row empty otherwise there will be a roadblock
        down(0,i)
        for j in range(n):
            t=random.randint(1,2)   #Randomly chooses to take out a wall on the right or bottom
            if t==1:
                down(i,j)
            else:
                right(i,j)


drawGrid(WIDTH, HEIGHT)
makeMaze()

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


