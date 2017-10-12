from flask import Flask
import time
import jsonify
import os
import random

app = Flask(__name__)

bola = 0
jugador1 = 0
jugador2 = 0

@app.route('/iniciaJuego', methods= ['GET'])
def iniciaJuego():
    global bola, jugador1,jugador2
    while (bola < 3):
        string = ""
        b = 0
        c = 0
        alefil1 = 0
        alecol2 = 0
        flagp = False  # bandera que se usa para saber que ninguno de los dos jugadores a ganado, se vuelve true cuando se toca un borde.
        flagb = False  # bandera que se usa como condicion para encontrar la bola.
        flagmb = 0  # bandera para saber hacia donde mover la bola.
        cont = 0

        print("Juego numero " + str(bola + 1))
        time.sleep(2)
        os.system('cls')

        matriz = [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
            , ['|', '', '', 'X', 'X', 'X', '', '', '', '|'], ['|', '', '', '', '', '', '', '', '', '|'],
                  ['|', '', '', '', '', '', '', '', '', '|']
            , ['|', '', '', '', '', '', '', '', '', '|'], ['|', '', '', '', '', '', '', '', '', '|'],
                  ['|', '', '', '', '', '', '', '', '', '|']
            , ['|', '', '', '', '', '', '', '', '', '|'], ['|', '', '', '', '', '', '', '', '', '|'],
                  ['|', '', '', '', '', '', '', '', '', '|']
            , ['|', '', '', '', '', '', '', '', '', '|'], ['|', '', '', '', '', '', '', '', '', '|'],
                  ['|', '', '', '', '', '', '', '', '', '|']
            , ['|', '', '', '', '', '', '', '', '', '|'], ['|', '', '', '', '', '', '', '', '', '|'],
                  ['|', '', '', '', '', '', '', '', '', '|']
            , ['|', '', '', '', '', '', '', '', '', '|'], ['|', '', '', '', '', '', '', '', '', '|'],
                  ['|', '', '', '', '', '', '', '', '', '|']
            , ['|', '', '', '', '', '', '', '', '', '|'], ['|', '', '', '', '', '', '', '', '', '|'],
                  ['|', '', '', '', '', '', '', '', '', '|']
            , ['|', '', '', '', '', '', '', '', '', '|'], ['|', '', '', '', '', '', '', '', '', '|'],
                  ['|', '', '', '', '', '', '', '', '', '|']
            , ['|', '', '', '', '', '', '', '', '', '|'], ['|', '', '', '', '', '', '', '', '', '|'],
                  ['|', '', '', '', '', '', '', '', '', '|']
            , ['|', '', '', '', '', '', '', '', '', '|'], ['|', '', '', '', '', '', '', '', '', '|'],
                  ['|', '', '', 'X', 'X', 'X', '', '', '', '|']
            , ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]

        alefil1 = random.randrange(11, 20, 1)  # fila de la 11 a la 20 que aparezca la bola
        alecol2 = random.randrange(3, 6, 1)  # columna de la 3 a la 6 que aparezca la bola
        matriz[alefil1][alecol2] = 'O'
        while (flagp == False):

            for j in range(10):  # paleta en la fila 1
                if (matriz[1][j] == 'X'):
                    b = j  # b = posicion de la primer x en la paleta 1

            for j in range(10):  # paleta en la fila 30
                if (matriz[30][j] == 'X'):
                    c = j  # c = posicion de la primer x en la paleta 2

            for i in range(32):
                for j in range(10):  # El siguiente codigo es para mover la bola una vez encontrada
                    if (matriz[i][j] == 'O' and flagb == False):
                        matriz[i][j] = ''  # Elimina la bola de la posicion actual

                        if (matriz[i + 1][j + 1] == '|' and flagmb == 0):
                            flagmb = 1
                        elif (matriz[i + 1][j + 1] == 'X' and flagmb == 0):
                            flagmb = 3

                        elif (matriz[i + 1][j - 1] == '|' and flagmb == 1):
                            flagmb = 0
                        elif (matriz[i + 1][j - 1] == 'X' and flagmb == 1):
                            flagmb = 2

                        elif (matriz[i - 1][j - 1] == '|' and flagmb == 2):
                            flagmb = 3
                        elif (matriz[i - 1][j - 1] == 'X' and flagmb == 2):
                            flagmb = 1

                        elif (matriz[i - 1][j + 1] == '|' and flagmb == 3):
                            flagmb = 2
                        elif (matriz[i - 1][j + 1] == 'X' and flagmb == 3):
                            flagmb = 0

                        # Dependiendo del numero que tenga la bandera se realizara el movimiento de la bola
                        # 0 se mueve de izquierda a derecha de arriba hacia abajo
                        # 1 se mueve de derecha a izquierda de arriba hacia abajo
                        # 2 se mueve de derecha a izquierda de abajo hacia arriba
                        # 3 se mueve de izquierda a derecha de abajo hacia arriba

                        if (flagmb == 0):
                            matriz[i + 1][j + 1] = 'O'
                        elif (flagmb == 1):
                            matriz[i + 1][j - 1] = 'O'
                        elif (flagmb == 2):
                            matriz[i - 1][j - 1] = 'O'
                        elif (flagmb == 3):
                            matriz[i - 1][j + 1] = 'O'
                        else:
                            matriz[i][j] = 'O'

                        if (cont % 2 == 0):
                            if (flagmb == 0 and matriz[30][c + 1] == ''):

                                matriz[30][c + 1] = 'X'
                                matriz[30][c] = 'X'
                                matriz[30][c - 1] = 'X'
                                matriz[30][c - 2] = ''

                            elif (flagmb == 1 and matriz[30][c - 3] == ''):
                                matriz[30][c - 3] = 'X'
                                matriz[30][c - 2] = 'X'
                                matriz[30][c - 1] = 'X'
                                matriz[30][c] = ''

                            elif (flagmb == 2 and matriz[1][b - 3] == ''):
                                matriz[1][b - 3] = 'X'
                                matriz[1][b - 2] = 'X'
                                matriz[1][b - 1] = 'X'
                                matriz[1][b] = ''

                            elif (flagmb == 3 and matriz[1][b + 1] == ''):
                                matriz[1][b + 1] = 'X'
                                matriz[1][b] = 'X'
                                matriz[1][b - 1] = 'X'
                                matriz[1][b - 2] = ''

                        flagb = True
                        cont = cont + 1
                        if (matriz[i + 1][j - 1] == '-' or matriz[i + 1][j + 1] == '-' or matriz[i - 1][j + 1] == '-' or
                                    matriz[i - 1][j - 1] == '-'):  # alguien gano
                            flagp = True

            flagb = False

            # El siguiente codigo es usado para concatenar la matriz y mostrarla sin corchetes
            for i in range(32):
                for j in range(10):
                    string += str(matriz[i][j]) + '\t'

                print(string)
                string = ""

            time.sleep(0.10000)
            os.system('cls')

        if (flagmb == 0 or flagmb == 1):
            jugador1 = jugador1 + 1
            print("Jugador uno gano 1 punto")
        elif (flagmb == 2 or flagmb == 3):
            jugador2 = jugador2 + 1
            print("Jugador dos gano 1 punto")

            # Detiene el codigo para leer el mensaje del ganador por 2 segundos para luego borrarlo y seguir
            time.sleep(2)
            os.system('cls')

        bola = bola + 1

        if (jugador1 > jugador2):
            print("Jugador uno Gano la partida")
        else:
            print("Jugador dos Gano la partida")

    return jsonify(matriz)




if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')