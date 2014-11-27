
#Guarda la informacion sobre el tablero y hace la logica del juego
class Tablero:
	
	def __init__(self):
		self.jugador = 1
		self.tablero=[]
		for i in range(8):
			self.tablero.append([0,0,0,0,0,0,0,0])
		self.tablero[3][3]=1
		self.tablero[4][4]=1
		self.tablero[3][4]=-1
		self.tablero[4][3]=-1

	def draw(self):
		for i in self.tablero:
			for x in i:
				print(x, end = " ")
			print("\n")

	def play (self, x, y):
		if self.canPlay(x,y):
			print("intenta")
			self.tablero[x][y] = self.jugador
			self.jugador *= -1

	#Comprueba si en esa casilla se puede colocar ficha =D
	def canPlay (self, x, y):
		if self.tablero[x][y] == 0:
			
			resultado = False
			#Comprobacion izquierda
			validMove = False
			for i in range(x):
				if self.tablero[x-i-1][y] == self.jugador*-1:
					validMove = True
				if self.tablero[x-i-1][y] == self.jugador:
					break
				if self.tablero[x-i-1][y] == 0:
					validMove = False
					break
			if validMove:
				self.swapRow(x,y,x-i-1,y)
				resultado =True

			#Comprobacion derecha
			validMove = False
			for i in range(8-x-1):
				if self.tablero[x+i+1][y] == self.jugador*-1:
					validMove = True
				if self.tablero[x+i+1][y] == self.jugador:
					break
				if self.tablero[x+i+1][y] == 0:
					validMove = False
					break
			if validMove:
				self.swapRow(x,y,x+i+1,y)
				resultado =True

			#Comprobacion arriba
			validMove = False
			for i in range(y):
				if self.tablero[x][y-i-1] == self.jugador*-1:
					validMove = True
				if self.tablero[x][y-i-1] == self.jugador:
					break
				if self.tablero[x][y-i-1] == 0:
					validMove = False
					break
			if validMove:
				self.swapRow(x,y,x,y-i-1)
				resultado =True

			#Comprobacion abajo
			validMove = False
			for i in range(8-y-1):
				if self.tablero[x][y+i+1] == self.jugador*-1:
					validMove = True
				if self.tablero[x][y+i+1] == self.jugador:
					break
				if self.tablero[x][y+i+1] == 0:
					validMove = False
					break
			if validMove:
				self.swapRow(x,y,x,y+i+1)
				resultado = True

			#Comprobacion diagonal negativa superior (\)
			validMove = False
			for i in range(min(x,y)):
				if self.tablero[x-i-1][y-i-1] == self.jugador*-1:
					validMove = True
				if self.tablero[x-i-1][y-i-1] == self.jugador:
					break
				if self.tablero[x-i-1][y-i-1] == 0:
					validMove = False
					break
			if validMove:
				self.swapRow(x,y,x-i-1,y-i-1)
				resultado =True

			#Comprobacion diagonal negativa inferior (\)
			validMove = False
			for i in range(min(8-x-1,8-y-1)):
				if self.tablero[x+i+1][y+i+1] == self.jugador*-1:
					validMove = True
				if self.tablero[x+i+1][y+i+1] == self.jugador:
					break
				if self.tablero[x+i+1][y+i+1] == 0:
					validMove = False
					break
			if validMove:

				self.swapRow(x,y,x+i+1,y+i+1)
				resultado =True

			#Comprobacion diagonal positiva superior (/)
			validMove = False
			for i in range(min(8-x-1,y)):
				if self.tablero[x+i+1][y-i-1] == self.jugador*-1:
					validMove = True
				if self.tablero[x+i+1][y-i-1] == self.jugador:
					break
				if self.tablero[x+i+1][y-i-1] == 0:
					validMove = False
					break
			if validMove:

				self.swapRow(x,y,x+i+1,y-i-1)
				resultado =True

			#Comprobacion diagonal positiva inferior (/)
			validMove = False
			for i in range(min(x,8-y-1)):
				if self.tablero[x-i-1][y+i+1] == self.jugador*-1:
					validMove = True
				if self.tablero[x-i-1][y+i+1] == self.jugador:
					break
				if self.tablero[x-i-1][y+i+1] == 0:
					validMove = False
					break
			if validMove:
				self.swapRow(x,y,x-i-1,y+i+1)
				resultado =True

			#Si una vez llegado aqui el resultado es 1, el movimiento ha sido valido
			return resultado
	#DEPRECATED
	def avalancha(self, x, y):
		pass
	def swapRow(self, x0, y0, x1, y1):
		xworth = min(x0,x1)
		x = max(x0,x1)
		yworth=min(y0,y1)
		y=max(y0,y1)
		while xworth != x or yworth != y:
			#print(xworth)
			#print(yworth)
			self.tablero[xworth][yworth] = self.jugador
			if xworth != x:
				xworth+=1
			if yworth != y:
				yworth+=1
		return True

if __name__ == "__main__":
	culo = Tablero()
	print(culo.play(5,3))
	culo.draw()
