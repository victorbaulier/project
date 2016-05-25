# Créé par victor, le 20/05/2016 en Python 3.2

import pygame
from pygame.locals import *
from constant import *
from random import randrange
from tkinter import *


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
        teleport=pygame.image.load(picture_teleport).convert()
        finish=pygame.image.load(picture_finish).convert()
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
                elif letter=="a":
                    window.blit(finish,(x,y))
                elif letter=='T' or letter=='S':
                    window.blit(teleport,(x,y))
                case_number+=1
            line_number+=1


class Player:

    def __init__(self,right,left,level):

        self.right=pygame.image.load(right).convert_alpha()
        self.left=pygame.image.load(left).convert_alpha()

        self.place_x=0
        self.place_y=0
        self.x=0
        self.y=0


        self.level=level
        self.direction=self.right

        self.counter=0

    def fall_until_wall(self):
        if(self.level.structure[self.place_y+1][self.place_x])!='w':
            while (self.level.structure[self.place_y+1][self.place_x]!='w'):
                self.place_y+=1
                self.y=self.place_y*sprite_size

    def fall_until_trolley(self):
        while (self.level.structure[self.place_y+2][self.place_x]!='w'):
            self.place_y+=1
            self.y=self.place_y*sprite_size


    def fall(self,trolley_position_x,trolley_position_y):
        if ((self.level.structure[self.place_y+1][self.place_x]!='w') and (self.place_y<trolley_position_y-1) and (self.place_x==trolley_position_x)) : #the worm doesn't fall through the trolley
            self.fall_until_trolley()
        elif(((self.level.structure[self.place_y+1][self.place_x]!='w') and not (self.place_y<trolley_position_y) and not (self.place_x==trolley_position_x))):
            self.fall_until_wall()
        elif(((self.level.structure[self.place_y+1][self.place_x]!='w') and (self.place_y==trolley_position_y) and not (self.place_x==trolley_position_x))):
            self.fall_until_wall()
        elif (((self.level.structure[self.place_y+1][self.place_x]!='w') and not (self.place_y<trolley_position_y-1) and not (self.place_x==trolley_position_x))):
            self.fall_until_wall()
        elif (((self.level.structure[self.place_y+1][self.place_x]!='w') and  (self.place_y>trolley_position_y) and (self.place_x==trolley_position_x))): #the worm can fall until a wall even if the worm has an Y higher than the trolley's one
            self.fall_until_wall()
        elif ((self.level.structure[self.place_y+1][self.place_x]!='w') and (self.place_y<trolley_position_y-1) and not (self.place_x==trolley_position_x)) :
            self.fall_until_wall()


    def teleport(self,position_out_x,position_out_y,direction): #when the worm goes in the in-door
        if direction=='right':                                              #it goes directly at the out-door
            if (self.level.structure[self.place_y][self.place_x]=='T'):

                self.place_x=position_out_x+1
                self.place_y=position_out_y

                self.x=self.place_x*sprite_size
                self.y=self.place_y*sprite_size

                self.direction=self.right

                self.counter+=1

    def death(self,ennemy_position_x,ennemy_position_y):
        if (ennemy_position_x==self.place_x) and (ennemy_position_y==self.place_y):
            return 0
        return 1


    def movements(self,trolley_position_x,trolley_position_y, direction):
        if direction=='right':

            if self.place_x<(sprite_number-1):      #checking if the next position isn't outside the window

                if (self.level.structure[self.place_y][self.place_x+1]!='w'):

                    if ((self.place_y==trolley_position_y) and (self.place_x+1 == trolley_position_x)):    #checking if there is no wall on the next position
                        if (self.level.structure[self.place_y][self.place_x+2]!='w'):
                            self.place_x+=1
                            self.x=self.place_x*sprite_size
                            self.direction=self.right
                            self.fall(trolley_position_x,trolley_position_y)
                            self.counter+=1
                    else:
                        self.place_x+=1
                        self.x=self.place_x*sprite_size
                        self.direction=self.right
                        self.fall(trolley_position_x,trolley_position_y)
                        self.counter+=1


        elif direction=='left':

            if self.place_x>0:

                if self.level.structure[self.place_y][self.place_x-1]!='w':

                     if ((self.place_y==trolley_position_y) and (self.place_x-1 == trolley_position_x)):    #checking if there is no wall on the next position
                        if (self.level.structure[self.place_y][self.place_x-2]!='w'):
                            self.place_x-=1
                            self.x=self.place_x*sprite_size
                            self.direction=self.left
                            self.fall(trolley_position_x,trolley_position_y)
                            self.counter+=1
                     else:
                        self.place_x-=1
                        self.x=self.place_x*sprite_size
                        self.direction=self.left
                        self.fall(trolley_position_x,trolley_position_y)
                        self.counter+=1



        elif direction=='up':
            if self.place_y>0:  #the worm can only jump if there is a wall under his "feet".   the worm can only jump once
                if ((self.level.structure[self.place_y-1][self.place_x]!='w' and self.level.structure[self.place_y+1][self.place_x]=='w' ) or (((self.place_y==trolley_position_y-1)) and (self.place_x==trolley_position_x))):
                    self.place_y-=1
                    self.y=self.place_y*sprite_size
                    self.direction=self.right

                    self.counter+=1




class Trolley:
    def __init__(self,level,structure):

        self.place_y=0
        self.place_x=0

        self.x=0
        self.y=0

        self.level=level
        self.trolley=pygame.image.load('pictures/trolley.jpg').convert_alpha()
        self.structure=structure


    def put_initial_position(self): #we read the entire file and find where at which coordonates is the trolley.
                                    #then the trolley is put at these coordonates
        for i in range (len(self.structure)):
            for j in range (len(self.structure[i])):
                if self.structure[i][j] == 'C':

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


class Teleport():
    def __init__(self,structure):
        self.position_out_x=0
        self.position_out_y=0

        self.structure=structure

    def find_position(self):
        for i in range (len(self.structure)):
            for j in range (len(self.structure[i])):
                if self.structure[i][j] == 'S':     #we find where is the out-door

                    self.position_out_x=j
                    self.position_out_y=i


class Ennemy():
    def __init__(self, structure,level):

        self.picture=pygame.image.load('pictures/bat.jpg').convert_alpha()

        self.place_x=0
        self.place_y=0
        self.random=0

        self.x=0
        self.y=0

        self.structure=structure


        self.level=level

    def find_position_init(self):
        for i in range (len(self.structure)):
            for j in range (len(self.structure[i])):
                if self.structure[i][j] == 'B':

                    self.place_x=j
                    self.place_y=i
                    self.x=j*sprite_size
                    self.y=i*sprite_size



    def find_direction(self,count):

        if count%30==0:            #this condition is to have a movement every seconds

            random=randrange(1,3)       #the movement is defined randomly


            if random==1:
                return('right')

            elif(random==2):
                return('left')





    def movement(self,trolley_position_x,trolley_position_y,direction):           #the same kind of movement than the worm's one, just the ennemy doesn't fell

        if direction=='right':
            if self.place_x<(sprite_number-1):
                if (self.level.structure[self.place_y][self.place_x+1]!='w'):
                    if not ((trolley_position_y==self.place_y)and (trolley_position_x==self.place_x+1)):

                        self.place_x+=1
                        self.x=self.place_x*sprite_size
                else:
                    self.movement(trolley_position_x,trolley_position_y,'left')   #this line is to make the movement more fluid. the ennemy won't stay at the same place if there is a wall in front of him

        elif direction=='left':
            if self.place_x>0:
                if (self.level.structure[self.place_y][self.place_x-1]!='w'):
                    if not ((trolley_position_y==self.place_y)and (trolley_position_x==self.place_x-1)):
                        self.place_x-=1
                        self.x=self.place_x*sprite_size
                else:
                    self.movement(trolley_position_x,trolley_position_y,'right') #simplement pour fluidifier le mouvement, le mechant ne peut pas rester  planté devant un mur




class Score:
    def __init__(self):
        self.score_time=0

    def score_timer(self,count):            #this is the timer to. every seconds exactly, the score increases by one
        if count%30 == 0:
            self.score_time=self.score_time + 1
            print(self.score_time)




    def display_score(self,highscore_mvt1,highscore_time1,death):


        root = Tk()
        root.title("--SCORE--")

        with open("save.txt", "r") as file:     #we read the file in which the scores are saved
            contents = file.read()
            contents=contents.split(',')
            timescore=int(contents[0])
            score_mvt=int(contents[1])
        #high score score

        if (score_mvt<=highscore_mvt1 and timescore<=highscore_time1 and death!=0): #check if the player did the BEST scores (time and moves)
            label = Label(root, text='Best time:')
            label.grid(column=0, row=0)
            label = Label(root, text=timescore)
            label.grid(column=1, row=0)
            #best movements
            label = Label(root, text='Best movements :')
            label.grid(column=0, row=1)
            label = Label(root, text=score_mvt)
            label.grid(column=1, row=1)

        elif ((timescore<=highscore_time1) and death!=0): #check if the player did the best score by time
            label = Label(root, text='best time :')
            label.grid(column=0, row=0)
            label = Label(root, text=timescore)
            label.grid(column=1, row=0)
            #movements
            label = Label(root, text='number of movements :')
            label.grid(column=0, row=1)
            label = Label(root, text=score_mvt)
            label.grid(column=1, row=1)

        elif((score_mvt<=highscore_mvt1) and death!=0): #check if the player did the best score bu moves
            label = Label(root, text='Best movements :')
            label.grid(column=0, row=0)
            label = Label(root, text=score_mvt)
            label.grid(column=1, row=0)

            label = Label(root, text='time (seconds) :')
            label.grid(column=0, row=1)
            label = Label(root, text=timescore)
            label.grid(column=1, row=1)

        elif(death!=0):                                 # basic score time and moves
            #time
            label = Label(root, text='time (seconds) :')
            label.grid(column=0, row=0)
            label = Label(root, text=timescore)
            label.grid(column=1, row=0)
            #movements
            label = Label(root, text='number of movements :')
            label.grid(column=0, row=1)
            label = Label(root, text=score_mvt)
            label.grid(column=1, row=1)
        else:
            label = Label(root, text='!!!! GAME OVER !!!!:')    #if the player get kiled by an ennemy, print Game Over
            label.grid(column=0, row=0)

        root.mainloop()



class Choose_level():

    def __init__(self):
        self.choice=0
        self.button=0

    def level1(self):
         continue_home=0
         self.choice='l1'
    def level2(self):
         continue_home=0
         self.choice='l2'
    def level3(self):
         continue_home=0
         self.choice='l3'
    def level4(self):
         continue_home=0
         self.choice='l4'
