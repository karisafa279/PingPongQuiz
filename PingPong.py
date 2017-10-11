import time
import random
import os


bola = 0
jugador1 = 0
jugador2 = 0

while (bola < 3):

	b=0
	c=0
	string = ""
	alefil1 = 0
	alecol2 = 0 
	flagp = False  #bandera que se usa para saber que ninguno de los dos jugadores a ganado, se vuelve true cuando se toca un borde.
	flagb = False  #bandera que se usa como condicion para encontrar la bola.
	
	
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
	
	#while (flagp == False):
	
	
	for j in range(10):            # paleta en la fila 1
			if(matriz[1][j]=='X'):
				b = j		       # b = posicion de la primer x en la paleta 1
				
	for j in range(10):            # paleta en la fila 30
			if(matriz[30][j]=='X'): 
				c = j			   # c = posicion de la primer x en la paleta 2

		#for i in range(32):
		#	for j in range(10):
				#El siguiente codigo es para mover la bola una vez encontrada 
		#		if(matriz[i][j]=='O' and flagb == False ):
		#			matriz[i][j]=''#Elimina la bola de la posicion actual
			
				#	if(matriz[i+1][j+1]=='|'
				
	

	#El siguiente codigo es usado para concatenar la matriz y mostrarla sin corchetes 
	for i in range(32):
		for j in range(10):
			string+=str(matriz[i][j])+'\t'
		
		print (string)
		string=""

	
	bola = bola+1	


#if(jugador1 > jugador2):
#	print("Jugador uno Gano")
#else:
#	print("Jugador dos Gano")