import pygame
from Parametres import *
from Outils import *
import Parametres

class Block :
    
    def __init__(self,forme,nom):
        self.forme = forme
        self.nom = nom
        self.position = 0
        self.y = 0
        self.x = 0

    def get_position(self):
        print("position = ",self.position)

    def droite(self,tas):
        forme = real_forme(self.forme,self.x,self.y,False)
        next = compute_next_droite(forme)
        if verif_x(next,tas.liste,"D") == False:
            self.x += 1

    def gauche(self,tas):
        forme = real_forme(self.forme,self.x,self.y,False)
        next = compute_next_gauche(forme)
        if verif_x(next,tas.liste,"G") == False:
            self.x -= 1

    def chute(self,count,tas,speed):
        count += 1
        forme = real_forme(self.forme,self.x,self.y,False)
        next = compute_next_bas(forme)
        if count >= 30 or (count >= 15 and speed):
            count = 0
            self.y += 1
            if verif_y(next,tas):
                return -1
        self.forme_reelle = forme
        return count
    
    def dessin_block(self):  
        for i in range(len(self.forme)):
           dessin_carre(Padding[0] + (self.forme[i][0] + self.x)*Case, Padding[1] + (self.forme[i][1] +self.y) *Case, Screen,couleur = Colors['blue'])

    def rotation(self,tas):
        reelle = real_forme(self.forme,self.x,self.y,False)
        if verif_rotation(self.x,self.y,tas.liste,self.position,self.nom) == False:
            return
        
        self.position = (self.position + 1) % 4
        
        if self.nom == "T":
            self.forme = Liste_T[self.position]
        elif self.nom == "L":
            self.forme = Liste_L[self.position]
        elif self.nom == "I":
            self.forme = Liste_I[self.position]
        else : 
            self.forme = Liste_C[self.position]


class Tas:
    def __init__(self):
        self.liste = [[0,14],[1,14],[2,14],[3,14],[4,14],[5,14],[6,14],[7,14],[8,14]]
    
    def add(self,forme,x,y):
        for el in forme:
            self.liste.append([el[0]+x,el[1]+y-1])

    def dessin_tas(self):
        for i in range(len(self.liste)):
           dessin_carre(Padding[0] + self.liste[i][0] *Case, Padding[1] + self.liste[i][1]*Case, Screen,couleur=Colors['red'],couleur2 = 'black')

    def destruct(self):
        liste = detect_line(self.liste)
        print(liste)
        if len(liste) == 0:
            return
        new_tas = []
        for el in self.liste:
            if el[1] not in liste:
                new_tas.append(el)
        print(f"nb de ligne = {len(liste)} | ligne max = {max(liste)}")
        self.liste = sort_list(chute_2(new_tas,liste))
        return liste

    def lose(self):
        for el in self.liste :
            if el[1] < 2 :
                
                return True
        return False

class next_block:

    def __init__(self):
        nom = choix_forme()
        self.forme = [pos.copy() for pos in Dico_forme[nom]]
        self.nom = nom
    
    def new_block(self):
        block = Block(self.forme,self.nom) 
        return block
    
    def dessin(self):
        for i in range(len(self.forme)):
           dessin_carre(Width/2 + 80 + self.forme[i][0]*Case2 ,Height/15 + 40 + self.forme[i][1]*Case2, Screen,couleur = Colors['green'],size = Case2)

class Score : 
    def __init__(self):
        self.score = 0

    def add(self,liste):
        if not liste:
            return
        else :
            multiplicateur = [1,1.5,2,2.5]
            nb = len(liste)
            self.score += nb * 10 * multiplicateur[nb-1]
            print("score = ",self.score)
    

    

        
    

                