#type on keyboard :
# "s" for play/pause
# "up arrow" for volume increase
# "down arrow" for volume decrease
# "d" for rewind
# "p" for passing the parcel
# "a" for stopping the player

from pygame import mixer
from time import sleep
import button
import pygame
import sys
import random
pygame.init()
mixer.init()
mixer.music.load('Music\Otonoke-[HiyoriOST].mp3')
mixer.music.play()
display = pygame.display.set_mode((600,400))
playim  = pygame.image.load("pics\play.png").convert_alpha()
pauseim = pygame.image.load("pics\pause.png").convert_alpha()
rewim  = pygame.image.load(r"pics\rewind.png").convert_alpha()
stopim = pygame.image.load("pics\stop.png").convert_alpha()
ptpim = pygame.image.load("pics\prcl.png")
bg=pygame.image.load(r"pics\bg.jpg").convert_alpha()
pg=pygame.image.load("pics\disc.gif").convert_alpha()
pg=pygame.transform.scale(pg,(230,230))
br=pygame.image.load(r"pics\border.png").convert_alpha()
br=pygame.transform.scale(br,(600,400))
x=1
p=0
rewk = button.Button(95, 300, rewim)
playk = button.Button(235, 300, playim)
pausek = button.Button(345, 300, pauseim)
stopk = button.Button(445, 300, stopim)
ptpk = button.Button(445, 100, ptpim,1)

while True:
    display.blit(bg, (0,0))
    display.blit(br, (0, 0))
    display.blit(pg, (135,30))
    pygame.display.set_caption('Music Player')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s] or playk.draw(display," Play"):
        p+=1
        if p % 2 == 1:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
        sleep(0.5)
    if pausek.draw(display,"Pause"):
        p+=1
        pygame.mixer.music.pause()
        sleep(0.2)
    if keys[pygame.K_UP]:
        x+=0.1
        pygame.mixer.music.set_volume(x)
        sleep(0.05)
    if keys[pygame.K_DOWN]:
        x -= 0.1
        pygame.mixer.music.set_volume(x)
        sleep(0.05)
    if keys[pygame.K_d] or rewk.draw(display,"Rewind"):
        pygame.mixer.music.rewind()
    if keys[pygame.K_p] or ptpk.draw(display,"passing the parcel",1):
        p+=1
        a=random.randint(1,7)
        sleep(a)
        pygame.mixer.music.pause()
    if keys[pygame.K_a] or stopk.draw(display," Stop"):
        mixer.music.stop()
        print("The player has been stopped !")
        break
    pygame.display.update()
