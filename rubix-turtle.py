#-*- coding utf-8 -*-
# Nom : 80 lignes de code pour un Rubixcube
# Auteur : Sense

from turtle import * #Inclusion d'un module externe


def rubixcube():
	
	#Premier carre
	speed(5)
	forward(150)
	left(90)
	forward(150)
	left(90)
	forward(150)
	left(90)
	forward(150)
	left(90)
	forward(100)
	
	#Quadrillage du carre
	left(90)
	forward(150)
	left(90)
	forward(50)
	left(90)
	forward(150)
	right(90)
	forward(50)
	right(90)
	forward(100)
	right(90)
	forward(150)
	right(90)
	forward(50)
	right(90)
	forward(150)
	left(90)
	forward(50)
	left(90)
	forward(150)
	
	#Mise en place du volume
	left(45)
	forward(50)
	left(45)
	forward(50)
	left(135)
	forward(50)
	right(135)
	forward(50)
	right(45)
	forward(50)
	right(135)
	forward(50)
	left(180)
	forward(100)
	left(135)
	forward(50)
	right(45)
	forward(150)
	right(135)
	forward(50)
	right(45)
	forward(50)
	right(135)
	forward(50)
	left(135)
	forward(50)
	left(45)
	forward(50)
	right(45)
	forward(50)
	left(180)
	forward(100)
	
	up()
	right(135)
	forward(25)
	right(45)
	write("Rubix-cube 2D")
	
rubixcube()
input()


