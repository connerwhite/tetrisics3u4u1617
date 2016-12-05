import pygame

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
