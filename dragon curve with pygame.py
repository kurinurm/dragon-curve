# Draw a dragon curve fractal
# https://en.wikipedia.org/wiki/Dragon_curve

import pygame

MAXLEVEL = 15  # recursion max depth

# Define the shape of the curve
# Those divisors offset the new point from the current segment
# Both 1: standard dragon curve with new line segments built at right angles
# Values < 1 : expand the curve in x or y direction
# Values > 1 : compress the curve
shapex = 1.0    
shapey = 1.0    

offsetx = 400   # shift curve from (0,0) to visible display area
offsety = 500

pygame.init()
screen = pygame.display.set_mode((1500,800))
pygame.display.set_caption("Dragon curve")      
clock = pygame.time.Clock()                     

# split line into two, or draw it if at max depth
def evolve(level, x1,y1, x2, y2):
    if level >= MAXLEVEL:
        pygame.draw.line(screen, [255]*3, (x1+offsetx,y1+offsety), (x2+offsetx,y2+offsety))
    else:
        # calculate x,y for the new "middle" point, replace the line by two new segments
        xnew = (x1+x2)/2.0 + (y2-y1)/2.0/shapex    
        ynew = (y1+y2)/2.0 - (x2-x1)/2.0/shapey 
        evolve(level+1, x1,y1, xnew, ynew)  # first new half-line segment
        evolve(level+1, x2,y2, xnew, ynew)  # second new half-line segment
    return

screen.fill([10]*3)     # dark canvas
evolve(0, 0,0, 700,0)   # kickoff!!!
pygame.display.flip()   # show the results

done = False
while not done:
    for event in pygame.event.get():
        done = done or event.type == pygame.QUIT
    clock.tick(10)

pygame.quit()

