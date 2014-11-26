
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
				resultado =True

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
				resultado =True

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
				resultado =True

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
				resultado = True

			#Comprobacion diagonal negativa superior (\)
			validMove = False
			for i in range(min(x,y)):
				if tablero[x-i-1][y-i-1] == jugador*-1:
					validMove = True
				if tablero[x-i-1][y-i-1] == jugador:
					break
				if tablero[x-i-1][y-i-1] == 0
					validMove = False
			if validMove:
				swapRow(x,y,x-i-1,y-i-1)
				resultado =True

			#Comprobacion diagonal negativa inferior (\)
			validMove = False
			for i in range(min(8-x,8-y):
				if tablero[x+i+1][y+i+1] == jugador*-1:
					validMove = True
				if tablero[x+i+1][y+i+1] == jugador:
					break
				if tablero[x+i+1][y+i+1] == 0
					validMove = False
			if validMove:
				swapRow(x,y,x+i+1,y+i+1)
				resultado =True

			#Comprobacion diagonal positiva superior (/)
			validMove = False
			for i in range(min(8-x,y)):
				if tablero[x+i+1][y-i-1] == jugador*-1:
					validMove = True
				if tablero[x+i+1][y-i-1] == jugador:
					break
				if tablero[x+i+1][y-i-1] == 0
					validMove = False
			if validMove:
				swapRow(x,y,x+i+1,y-i-1)
				resultado =True

			#Comprobacion diagonal positiva inferior (/)
			validMove = False
			for i in range(min(x,8-y):
				if tablero[x-i-1][y+i+1] == jugador*-1:
					validMove = True
				if tablero[x-i-1][y+i+1] == jugador:
					break
				if tablero[x-i-1][y+i+1] == 0
					validMove = False
			if validMove:
				swapRow(x,y,x-i-1,y+i+1)
				resultado =True

			#Si una vez llegado aqui el resultado es 1, el movimiento ha sido valido
			return resultado
	#DEPRECATED
	def avalancha(self, x, y):
	
	def swapRow(self, x, y):
		return True
