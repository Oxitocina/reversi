
#Guarda la informacion sobre el tablero y hace la logica del juego
class Tablero:
	
	def __init__(self):
		self.jugador = 1
		self.tablero=[]
		fila = []
		for i in range(8):
			fila.append(0)
		for i in range(8):
			self.tablero.append(fila)

	def play (self, x, y):
		if canPlay(x,y):
			avalancha(x,y)
			tablero[x][y] = jugador
			jugador *= -1

	#Comprueba si en esa casilla se puede colocar ficha =D
	def canPlay (self, x, y):
		if tablero[x][y] == 0:
			
			resultado = 0
			#Comprobacion izquierda
			validMove = False
			for i in range(x):
				if tablero[x-i-1][y] == jugador*-1:
					validMove = True
				if tablero[x-i-1][y] == jugador:
					break
				if tablero[x-i-1][y] == 0
					validMove = False
			if validMove:
				swapRow(x,y,x-i-1,y)
				resultado ==1

			#Comprobacion derecha
			validMove = False
			for i in range(8-x):
				if tablero[x+i+1][y] == jugador*-1:
					validMove = True
				if tablero[x+i+1][y] == jugador:
					break
				if tablero[x+i+1][y] == 0
					validMove = False
			if validMove:
				swapRow(x,y,x+i+1,y)
				resultado ==1

			#Comprobacion arriba
			validMove = False
			for i in range(y):
				if tablero[x][y-i-1] == jugador*-1:
					validMove = True
				if tablero[x][y-i-1] == jugador:
					break
				if tablero[x][y-i-1] == 0
					validMove = False
			if validMove:
				swapRow(x,y,x,y-i-1)
				resultado ==1

			#Comprobacion abajo
			validMove = False
			for i in range(8-y):
				if tablero[x][y+i+1] == jugador*-1:
					validMove = True
				if tablero[x][y+i+1] == jugador:
					break
				if tablero[x][y+i+1] == 0
					validMove = False
			if validMove:
				swapRow(x,y,x,y+i+1)
				resultado ==1

	#DEPRECATED
	def avalancha(self, x, y):
	
	def swapRow(self, x, y):
