from cercle import Cercle
from math import pi

cercle1 = Cercle(8)
print("perimetre : ",cercle1 .perimetre)  
print("surface",cercle1 .surface)    

try:
    cercle1 .rayon = -2
except ValueError as e:
    print("erreur : ", e)

cercle1 .agrandir(15)
print("nv rayon après agrandissement de 15 % :", cercle1.rayon)
print("nv surface :", cercle1 .surface)
