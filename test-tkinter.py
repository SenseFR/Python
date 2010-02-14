#-*- coding utf-8 -*-
# Nom : Spam window
# Auteur : Sense

from Tkinter import *

def ouverture():
	fenetre = Tk()
	text1 = Label(fenetre, text=' \o/', fg='green')
	text1.pack()
	bout1 = Button(fenetre, text='Quitter', command = fenetre.destroy)
	bout1.pack()
	fenetre.mainloop()
	
while 1 != 0:
	ouverture()
