import pygame, sys
from pygame.locals import *

"""This is a Tetris style game that the ICS3U/4U 2016/2017 class in Huntsville High School is creating.
Teacher: I. McTavish
Date: Dec 1, 2016"""

#Global Variables

class Score:
    def __init__(self):
        self.score = 0
    def update_score(self):
        print("in update score")
    def draw(self):
        print("in draw method")
class Block:
    def __init__(self):
        print("initialize")
    def update(self):
        print("In block update")
    def draw(self):
        print("In block draw")
    def rotate(self):
        print("In block rotate")
    def check_collision(self):
        print("In check collision")
class Music:
    def __init__(self):
        self.Music = 0

    def play_music(self):
        print("in play music")

    def play_sound_right(self):
        print("in play soundright")

    def play_sound_left(self):
        print("in play sound left")

    def  play_sound_flip(self):
        print("in play sound flip")

    def play_sound_falling(self):
        print("in play sound falling")

class Game_Grid:
    def __init__(self):
        self.Game_Grid = 0

    def update(self):
        print("in update")

    def draw(self,DISPLAY):
        print("in draw")
        WHITE=(255,255,255)
        red = (255,0,0)
        blue=(155,255,255)
        black=(0,0,0)

        length = 33
        height = 33

        DISPLAY.fill(blue)
        pygame.draw.rect(DISPLAY,black, (9, 9, 352, 702))

        x=10
        y=11

        for nr in range(20):
            self.row(DISPLAY, WHITE,x,y,length,height)
            y=y+35
    def row(self,DISPLAY, colour,x,y, length, height):
        for i in range(10):
            if i % 2 == 0:
                pygame.draw.rect(DISPLAY,colour, (x+1, y, length, height))
                x = x + 35
            else:
                pygame.draw.rect(DISPLAY,colour, (x+1, y, length, height))
                x = x + 35

def main(winstyle = 0):
    print("in main method")
    pygame.init()

    DISPLAY=pygame.display.set_mode((370,720),0,32)
    game_grid = Game_Grid()
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        game_grid.draw(DISPLAY)

#call the "main" function if running this script
if __name__ == '__main__': main()
