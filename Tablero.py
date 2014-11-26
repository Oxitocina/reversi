
#Guarda la informacion sobre el tablero y hace la logica del juego
class Tablero:
	
	def __init__(self):
    	self.jugador = 1
    	self.tablero

    def play (self, x, y):
    	if canPlay(x,y):
    		avalancha(x,y)
    		tablero[x][y] = jugador
    		jugador *= -1

    #Comprueba si en esa casilla se puede colocar ficha =D
    def canPlay (self, x, y):	