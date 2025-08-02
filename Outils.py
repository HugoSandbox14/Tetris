import pygame
import random
from Parametres import *


def base(score):
    pygame.draw.rect(Screen,(255,255,255),(Padding[0],Padding[1],Case*9,Case*14))
    pygame.draw.rect(Screen,(255,255,255),(Width/20 + Width/2,Height/14,Case*8,Case*4))
    pygame.draw.rect(Screen,(255,255,255),(Width/20 + Width/2,Height/14 + Case*4 + 20,Case*5,Case))
    pygame.draw.rect(Screen,(255,0,0),(Padding[0],Padding[1]+Case,Case*9,5))
    font = pygame.font.SysFont(None, 40)    
    text = font.render(f"Score : {score.score}", True, (0, 0, 0))
    Screen.blit(text, (Width/20 + Width/2 + 10 ,Height/14 + Case*4 + 30))

def choix_forme():
    liste = ['T','I','L','C']
    # liste = ['T','T','T','T']
    # liste = ['I']*4
    rand = random.randint(0,3)
    return liste[rand]

def dessin_carre(x,y,ecran,size=50,couleur = Colors['green'], couleur2 = Colors['white']):
    pygame.draw.rect(ecran,couleur,(x,y,size,size))
    pygame.draw.rect(ecran,couleur2,(x,y,size,size),3)

def compute_prev(forme):
    forme_2 = [pos.copy() for pos in forme]
    for i in range(len(forme_2)):
        forme_2[i][1] -= 1
    return forme_2

def compute_next_bas(forme):
    forme_2 = [pos.copy() for pos in forme]
    for i in range(len(forme_2)):
        forme_2[i][1] += 1
    return forme_2

def compute_next_gauche(forme):
    forme_cp = [pos.copy() for pos in forme]
    forme_fin = []
    for el in forme_cp:
        forme_fin.append([el[0]-1,el[1]])
    return forme_fin

def compute_next_droite(forme):
    forme_cp = [pos.copy() for pos in forme]
    forme_fin = []
    for el in forme_cp:
        forme_fin.append([el[0]+1,el[1]])
    return forme_fin

def verif_y(block,tas):
    # print("verif_y")
    for el in block:
        if el in tas.liste:
            return True
    return False

def verif_x(block,tas,direction):
    if direction == "D":
        for el in block:
            if el[0] == 9 or el in tas:
                # print(f"bordure droite : block = {block}")
                return True
    elif direction == "G":
        for el in block:
            if el[0] == -1 or el in tas: 
                # print(f"bordure gauche !! --> block = {block}")
                return True
    return False

def verif_rotation(x,y,tas,position,nom):

    position = (position + 1) % 4

    if nom == "T":
        next = Liste_T[position]
    elif nom == "L":
        next = Liste_L[position]
    elif nom == "I":
        next = Liste_I[position]
    elif nom == "C":
        next = Liste_C[position]
    
    reelle = real_forme(next,x,y,False)

    for el in reelle:
        if el in tas:
            return False
        elif el[0] <= -1 or el[0] >= 9 or el[1] < 0:
            return False
    return True

def sort_list(liste):

    liste_calcul = []
    for el in liste:
        liste_calcul.append(el[1]*10+el[0])
    liste_calcul.sort()
    final_list = []

    for el in liste_calcul:
        if el <= 9:
            final_list.append([el,0])
        else :
            final_list.append([el%10,el//10])
    return final_list

def real_forme(forme,x,y,aff = True):
    forme_aff = []
    for el in forme:
        forme_aff.append([el[0]+x,el[1]+y])
    if aff:
        print("block = ",forme_aff)
    return forme_aff

def detect_line(tas):
    dico_line = {}
    for i in range(14):
        dico_line[f'{i}'] = []
        for el in tas:
            if el[1] == i:
                dico_line[f'{i}'].append(el)
    liste = []
    for i,value in dico_line.items():
        if len(value) == 9:
            liste.append(int(i))
    return liste

def plus_one(liste):
    new = []
    for x,y in liste:
        new.append([x,y+1])
    return new

def count_lines(lines,n):
    count = 0
    for l in lines:
        if l > n:
            count += 1
    return count


def chute_2(liste,lines):
    new_liste = []

    for x,y in liste:
        count = count_lines(lines,y)
        new_liste.append([x,y+count])
    return new_liste

    




    
    

