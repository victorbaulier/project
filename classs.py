# Créé par victor, le 20/05/2016 en Python 3.2

import pygame
from pygame.locals import *
from constant import *


class Level:
    def __init__(self,file):
        self.file=file
        self.structure=0

    def create(self):
        #we create a structure which will contain all the datas from the file
        with open(self.file, "r") as file:
            level_structure = []
            for(line)in file:
                level_line=[]
        # each element from the structure is line
                for sprite in line:
                    if sprite!='\n':
                        #letters are add to the line's array
                        level_line.append(sprite)
                #we add the line to the array af the level
                level_structure.append(level_line)
            # we save this structure
            self.structure=level_structure

    def print(self, window):

        #images are loaded
        wall=pygame.image.load(picture_wall).convert()
        #the programm reads the structure and find the different letters.


        line_number=0
        for line in self.structure:
            case_number=0
            for letter in line:
                x=case_number*sprite_size
                y=line_number*sprite_size
        # x and y are used to find the exact place of the different letters in the structure
        # and the images corresponding to the letters are placed in the window at the right coordonates
                if letter=='w':
                    window.blit(wall,(x,y))
                case_number+=1
            line_number+=1


class Player:

    def __init__(self,level):

        self.place_x=0
        self.place_y=0
        self.x=0
        self.y=0

        self.level=level
        self.player=pygame.image.load('pictures/worms.png').convert_alpha()

    def fall(self):
        while (self.level.structure[self.place_y+1][self.place_x]!='w'):
            self.place_y+=1
            self.y=self.place_y*sprite_size


    def movements(self,direction):
        if direction=='right':
            if self.place_x<(sprite_number-1):      #checking if the next position isn't outside the window
                if self.level.structure[self.place_y][self.place_x+1]!='w':     #checking if there is no wall on the next position
                    self.place_x+=1
                    self.x=self.place_x*sprite_size
                self.fall()

        elif direction=='left':
            if self.place_x>0:
                if self.level.structure[self.place_y][self.place_x-1]!='w':
                    self.place_x-=1
                    self.x=self.place_x*sprite_size
                self.fall()

        elif direction=='up':
            if self.place_y>0:  #the worm can only jump if there is a wall under his "feet".   the worm can only jump once
                if self.level.structure[self.place_y-1][self.place_x]!='w' and self.level.structure[self.place_y+1][self.place_x]=='w':
                    self.place_y-=1
                    self.y=self.place_y*sprite_size




class Trolley:
    def __init__(self,level,structure):

        self.place_y=0
        self.place_x=0

        self.x=0
        self.y=0

        self.level=level
        self.trolley=pygame.image.load('pictures/trolley.png').convert_alpha()
        self.structure=structure


    def put_initial_position(self): #we read the entire file and find where at which coordonates is the trolley.
                                    #then the trolley is put at these coordonates
        for i in range (len(self.structure)):
            for j in range (len(self.structure[i])):
                if self.structure[i][j] == 'T':

                    self.place_x=j
                    self.place_y=i
                    self.x=j*sprite_size
                    self.y=i*sprite_size
    def fall(self):
        if(self.level.structure[self.place_y+1][self.place_x])!='w':
            while (self.level.structure[self.place_y+1][self.place_x]!='w'):
                self.place_y+=1
                self.y=self.place_y*sprite_size

    def movement(self,worm_position_x,worm_position_y,direction):
        if direction=='right':
            if self.place_x<(sprite_number -1):
                if (self.place_x==worm_position_x)and(self.place_y==worm_position_y):
                    if self.level.structure[self.place_y][self.place_x+1]!='w':
                        self.place_x+=1
                        self.x=self.place_x*sprite_size
                        self.fall()

        elif direction=='left':
            if self.place_x>0:
                if (self.place_x==worm_position_x)and(worm_position_y==self.place_y):
                    if self.level.structure[self.place_y][self.place_x-1]!='w':
                        self.place_x-=1
                        self.x=self.place_x*sprite_size
                        self.fall()












