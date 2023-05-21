import pygame
import random
pygame.init()

w, h = 800, 800

time = pygame.time.Clock()
FPS = w*w*5

zer = 10 #w / zer == 800 / zer <---> number of poles - 1

Steps = [Ra for Ra in range(0, int(w * (10 / zer) ) + 8, 8)]  #poles Steps

Ch = w
lines = []
while True:
    Cw = w / 100
    Ch = Ch - zer
    r = random.randint(0, len(Steps)-1)
    x = Steps[r]
    Steps.pop(r)
    lines.append(pygame.Rect(x, 0, Cw, Ch))
    if Ch <= 0:
        lines.pop()
        break

w = len(lines) * 8

random.shuffle(lines)


run = False
fh = 1

d= 0
ne = 3

is_end = False
RGB = [255, 255, 255]

dis = pygame.display.set_mode((w, h))
while True:
    dis.fill('white')

    for m in lines:
        m.x = lines.index(m) * 8
        if is_end:
            pygame.draw.rect(dis, RGB, m)
        pygame.draw.rect(dis, [0, 0, 0], m, ne)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        run = True
    if run:
        if lines[fh].h < lines[fh - 1].h:
            le = lines[fh]
            lines[fh] = lines[fh - 1]
            lines[fh - 1] = le
            d = 0
        else:
            fh += 1
            d += 1

    if fh == len(lines):
        fh = 1

    if d == len(lines):
        RGB = [0, 255, 0]
        run = False
        is_end = True

        
 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
    time.tick(FPS)
