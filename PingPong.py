import time
import random
import os


bola = 0
jugador1 = 0
jugador2 = 0

while (bola < 3):

	b=0
	c=0
	alefil1 = 0
	alecol2 = 0 
	
	
	print("Juego numero "+str(bola+1))
	
	matriz=[['-','-','-','-','-','-','-','-','-','-']
		,['|','','','X','X','X','','','','|'],['|','','','','','','','','','|'],['|','','','','','','','','','|']
		,['|','','','','','','','','','|'],['|','','','','','','','','','|'],['|','','','','','','','','','|']
		,['|','','','','','','','','','|'],['|','','','','','','','','','|'],['|','','','','','','','','','|']
		,['|','','','','','','','','','|'],['|','','','','','','','','','|'],['|','','','','','','','','','|']
		,['|','','','','','','','','','|'],['|','','','','','','','','','|'],['|','','','','','','','','','|']
		,['|','','','','','','','','','|'],['|','','','','','','','','','|'],['|','','','','','','','','','|']
		,['|','','','','','','','','','|'],['|','','','','','','','','','|'],['|','','','','','','','','','|']
		,['|','','','','','','','','','|'],['|','','','','','','','','','|'],['|','','','','','','','','','|']
		,['|','','','','','','','','','|'],['|','','','','','','','','','|'],['|','','','','','','','','','|']
		,['|','','','','','','','','','|'],['|','','','','','','','','','|'],['|','','','X','X','X','','','','|']
		,['-','-','-','-','-','-','-','-','-','-'] ]
		
	ale1= random.randrange(11,20,1) #fila de la 11 a la 20 que aparezca la bola
	ale2= random.randrange(3,6,1)   #columna de la 3 a la 6 que aparezca la bola
	matriz[ale1][ale2]='O'	
	
	
	for j in range(10):            # paleta en la fila 1
			if(matriz[1][j]=='X'):
				b = j		       # b = posicion de la primer x en la paleta 1
			
	for j in range(10):            # paleta en la fila 30
			if(matriz[30][j]=='X'): 
				c = j			   # c = posicion de la primer x en la paleta 2

	bola = bola+1	

if(jugador1 > jugador2):
	print("Jugador uno Gano")
else:
	print("Jugador dos Gano")