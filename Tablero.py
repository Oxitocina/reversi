#
#              .__....._             _.....__,
#                 .": o :':         ;': o :".
#                 `. `-' .'.       .'. `-' .'  
#                   `---'             `---' 
#
#         _...----...      ...   ...      ...----..._
#      .-'__..-""'----    `.  `"`  .'    ----'""-..__`-.
#     '.-'   _.--"""'       `-._.-'       '"""--._   `-.`
#     '  .-"'                  :                  `"-.  `
#       '   `.              _.'"'._              .'   `
#             `.       ,.-'"       "'-.,       .'
#               `.                           .'
#                 `-._                   _.-'
#                     `"'--...___...--'"`

#Guarda la informacion sobre el tablero y hace la logica del juego
class Tablero:
	
	def __init__(self):
		self.jugador = 1
		self.tablero=[]
		#Tablero de 8x8
		for i in range(8):
			self.tablero.append([0,0,0,0,0,0,0,0])
		#Estado inicial del tablero
		self.tablero[3][3]=1
		self.tablero[4][4]=1
		self.tablero[3][4]=-1
		self.tablero[4][3]=-1

	def draw(self):
		for i in self.tablero:
			for x in i:
				print(x, end = " ")
			print("\n")

	#Recibe una jugada
	def play (self, x, y):
		#Intenta jugar, si el movimiento es valido añade la ficha y cambia de jugador
		if self.canPlay(x,y):
			self.tablero[x][y] = self.jugador
			self.jugador *= -1

	#Comprueba si en esa casilla se puede colocar ficha =D
	def canPlay (self, x, y):
		#Solo se puede jugar si la casilla estaba vacia
		if self.tablero[x][y] == 0:
			
			#Solo puede jugar si come en alguna direccion, por lo que comprueba todas las direcciones
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

	#Cambia el valor de una linea al del jugador actual(Ha comido fichas)
	def swapRow(self, x0, y0, x1, y1):
		#Separo la menor de cada coordenada para poder recorrerlas facilmente
		xworth = min(x0,x1)
		x = max(x0,x1)
		yworth=min(y0,y1)
		y=max(y0,y1)

		#Bucle que va desde las coordenadas inferiores a las superiores, aumentando mientras sea aun menor, por tanto, recorre filas y columnas sumando solo en una variable
		#y las diagonales sumando en ambas variables, recorriendo cualquier asi cualquier direccion.
		while xworth != x or yworth != y:
			self.tablero[xworth][yworth] = self.jugador
			if xworth != x:
				xworth+=1
			if yworth != y:
				yworth+=1

	#Cuenta el numero de fichas del jugador uno
	def count(self):
		counter = 0
		for i in self.tablero:
			for x in i:
				if x==1:
					counter += 1 
		return counter

if __name__ == "__main__":
	culo = Tablero()
	print(culo.play(5,3))
	culo.draw()
	#print(culo.count())