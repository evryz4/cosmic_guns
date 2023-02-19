import pygame
from random import randint
from os.path import abspath
import maxscore
path = abspath(__file__)
pathfile = path.split("\\")[0:len(path.split("\\"))-1]
pathfile.append(r"maxscore.py")
pathfile = "\\".join(pathfile)
pygame.init()
dis = pygame.display.set_mode((500,500))
quit = False
pygame.display.set_caption("game")
X = 240
Yadd = 0
Yadd2 = 250
clock = pygame.time.Clock()
bulX = 240
bul2X = 240
targetX = range(0,480,10)[randint(0,47)]
target2X = range(0,480,10)[randint(0,47)]
score = 0
targetY = 90
target2Y = 90
file = open(pathfile,"w")
max_score = maxscore.SCORE
def draw_gun(X):
    pygame.draw.rect(dis, (255, 255, 255), [X, 400, 10, 10])
    pygame.draw.rect(dis, (255, 255, 255), [X, 410, 10, 10])
    pygame.draw.rect(dis, (255, 255, 255), [X - 10, 410, 10, 10])
    pygame.draw.rect(dis, (255, 255, 255), [X + 10, 410, 10, 10])
    pygame.draw.rect(dis, (255, 255, 255), [X - 10, 420, 10, 10])
    pygame.draw.rect(dis, (255, 255, 255), [X + 10, 420, 10, 10])
while not quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
        if event.type == 771:
            if event.text == "a":
                X -= 10
            if event.text == "d":
                X += 10
    dis.fill((0,0,0))
    draw_gun(X)
    Yadd += 10
    Yadd2 += 10
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render(str(score), 1, (255, 255, 255))
    text2 = f1.render("max: "+str(max_score), 1, (255, 255, 255))
    dis.blit(text1, (1, 3))
    dis.blit(text2, (400, 3))
    if 500 - Yadd < 90:
        bulX = X
        Yadd = 0
    if 500 - Yadd2 < 90:
        bul2X = X
        Yadd2 = 0
    if bul2X == targetX and 420-Yadd2 == targetY-targetY%10:
        targetX = range(0, 490, 10)[randint(0, 48)]
        score += 1
        targetY = 0
    else:
        pygame.draw.rect(dis, (0, 255, 0), [targetX, targetY, 10, 10])
        pygame.draw.rect(dis, (0, 255, 0), [targetX, targetY-10, 10, 10])
    if bul2X == targetX and 420-Yadd2 == targetY-targetY%10 - 10:
        targetX = range(0, 490, 10)[randint(0, 48)]
        score += 1
        targetY = 0
    else:
        pygame.draw.rect(dis, (0, 255, 0), [targetX, targetY, 10, 10])
        pygame.draw.rect(dis, (0, 255, 0), [targetX, targetY - 10, 10, 10])
    if targetY > 500:
        quit = True

    if bul2X == target2X and 420-Yadd2 == target2Y-target2Y%10:
        target2X = range(0, 490, 10)[randint(0, 48)]
        score += 1
        target2Y = 0
    else:
        pygame.draw.rect(dis, (0, 255, 0), [target2X, target2Y, 10, 10])
        pygame.draw.rect(dis, (0, 255, 0), [target2X, target2Y-10, 10, 10])
    if bul2X == target2X and 420 - Yadd2 == target2Y - target2Y % 10-10:
        target2X = range(0, 490, 10)[randint(0, 48)]
        score += 1
        target2Y = 0
    else:
        pygame.draw.rect(dis, (0, 255, 0), [target2X, target2Y, 10, 10])
        pygame.draw.rect(dis, (0, 255, 0), [target2X, target2Y - 10, 10, 10])
    if target2Y > 500:
        quit = True
    if bulX == targetX and 420-Yadd == targetY-targetY%10:
        targetX = range(0, 490, 10)[randint(0, 48)]
        score += 1
        targetY = 0
    else:
        pygame.draw.rect(dis, (0, 255, 0), [targetX, targetY, 10, 10])
        pygame.draw.rect(dis, (0, 255, 0), [targetX, targetY-10, 10, 10])
    if bulX == targetX and 420-Yadd == targetY-targetY%10 - 10:
        targetX = range(0, 490, 10)[randint(0, 48)]
        score += 1
        targetY = 0
    else:
        pygame.draw.rect(dis, (0, 255, 0), [targetX, targetY, 10, 10])
        pygame.draw.rect(dis, (0, 255, 0), [targetX, targetY - 10, 10, 10])
    if targetY > 500:
        quit = True

    if bulX == target2X and 420-Yadd == target2Y-target2Y%10:
        target2X = range(0, 490, 10)[randint(0, 48)]
        score += 1
        target2Y = 0
    else:
        pygame.draw.rect(dis, (0, 255, 0), [target2X, target2Y, 10, 10])
        pygame.draw.rect(dis, (0, 255, 0), [target2X, target2Y-10, 10, 10])
    if bulX == target2X and 420 - Yadd == target2Y - target2Y % 10-10:
        target2X = range(0, 490, 10)[randint(0, 48)]
        score += 1
        target2Y = 0
    else:
        pygame.draw.rect(dis, (0, 255, 0), [target2X, target2Y, 10, 10])
        pygame.draw.rect(dis, (0, 255, 0), [target2X, target2Y - 10, 10, 10])
    if target2Y > 500:
        quit = True
    targetY+=3
    target2Y += 3
    if score > max_score:
        max_score = score
    pygame.draw.rect(dis, (255, 255, 255), [bulX, 410-Yadd, 10, 10])
    pygame.draw.rect(dis, (255, 255, 255), [bul2X, 410 - Yadd2, 10, 10])
    pygame.display.update()
    clock.tick(20)
pygame.quit()
file.truncate()
file.write("SCORE = " + str(max_score)+"\n#do you want to change your max score? ok. but playing honestly is better than cheating!")
file.close()