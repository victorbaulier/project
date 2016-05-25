# Créé par victor, le 20/05/2016 en Python 3.2

from tkinter import *

import pygame
from pygame.locals import *

from classs import *
from constant import *

import time



pygame.init()

LV=Choose_level()

#principale loop

continu=1
while continu:
    continu_home=1
    while LV.choice==0:

        import tkinter as tk

        root=Tk()
        root.title=("---home---")

        level1=tk.PhotoImage(file="pictures/level_1.gif")
        level2=tk.PhotoImage(file="pictures/level_2.gif")
        level3=tk.PhotoImage(file="pictures/level_3.gif")
        level4=tk.PhotoImage(file="pictures/final_level.gif")
        #title

        w= Label(root,text="welcome into worms game",fg="blue",font="Verdana 15 bold").pack(side="top")
        w= Label(root,text="choose your level and click on quit button",fg="blue",font="Verdana 15 bold").pack(side="top")

        Button(root, text='LEVEL 1', command=LV.level1,borderwidth=10,font=10,image=level1).pack(side="left")
        Button(root, text='LEVEL 2', command=LV.level2,borderwidth=10,font=10,image=level2).pack(side="left")
        Button(root, text='LEVEL 3', command=LV.level3,borderwidth=10,font=10,image=level3).pack(side="left")
        Button(root, text='LEVEL 4', command=LV.level4,borderwidth=10,font=10,image=level4).pack(side="left")

        if LV.choice=='l1':
            root.quit()

        root.mainloop()

        choice=LV.choice

        continu_game=1
        continu_home=1

        if choice!=0:

            window=pygame.display.set_mode((window_width, window_width))

            background=pygame.image.load(picture_background).convert()
            level= Level(choice)
            level.create()
            level.print(window)


            worm=Player("pictures/worms-right.png","pictures/worms-left.png",level)
            trolley=Trolley(level,level.structure)
            teleport=Teleport(level.structure)
            bad=Ennemy(level.structure,level)
            US=Score()

            teleport.find_position()        #we collect the coordonates of the out-door of the teleport
            trolley.put_initial_position()  #we collect the initial coordonates of the trolley
            window.blit(worm.direction,(0,0))      #the worm is printed at the coordonates (0,0)
            bad.find_position_init()

            count=0                         # we create a counter to be able to create ennemy's movements.

            while(continu_game):
                pygame.time.Clock().tick(40)    #this is the playing loop

                count+=1

                US.score_timer(count)

                bad.movement(trolley.place_x, trolley.place_y, bad.find_direction(count)) #the ennemy moves end his movement depends on the direction defined by the function "find_direction"

                for event in pygame.event.get():
                    if event.type== KEYDOWN:
                        if event.key==K_RIGHT:
                            worm.movements(trolley.place_x,trolley.place_y,'right')
                            trolley.movement(worm.place_x,worm.place_y,'right')
                            worm.teleport(teleport.position_out_x,teleport.position_out_y,'right')
                        elif event.key==K_LEFT:
                            worm.movements(trolley.place_x,trolley.place_y,'left')
                            trolley.movement(worm.place_x,worm.place_y,'left')
                        elif event.key==K_UP:
                            worm.movements(trolley.place_x,trolley.place_y,'up')




                window.blit(background,(0,0))   #the background is printed again
                level.print(window)             #the environment is printed again
                window.blit(worm.direction,(worm.x,worm.y))    #the worm is printed at his new position
                window.blit(trolley.trolley,(trolley.x,trolley.y))
                window.blit(bad.picture,(bad.x,bad.y)) # the trolley is printed at its initial position
                pygame.display.flip()           #the page is refreshed


                death=worm.death(bad.place_x,bad.place_y)

                if level.structure[worm.place_y][worm.place_x]=='a' or death==0:
                    with open("save.txt", "w") as file:
                        file.write(str(US.score_time)+','+str(worm.counter))
                    if choice=='l1':
                        US.display_score(highscore_mvt1,highscore_time1,death)
                    elif choice=='l2':
                        US.display_score(highscore_mvt2,highscore_time2,death)
                    elif choice=='l3':
                        US.display_score(highscore_mvt3,highscore_time3,death)
                    elif choice=='l4':
                        US.display_score(highscore_mvt4,highscore_time4,death)

                    continu_game=0
                    LV.choice=0
