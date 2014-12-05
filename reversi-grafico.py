from Tablero import *
from graphics import *
from sys import *

class Partida():	
	def __init__(self):
		self.ventana = GraphWin("Reversi", 555, 555)
		self.tablero = Image(Point(277.5,277.5), "tablero-ajedrez.png")
		self.tabl = Tablero()
		#Esta linea es necesaria por algun motivo o.O
		self.fichaGhost = Circle(Point(0, 0), 0)
		self.lastGhostX = -1
		self.lastGhostY = -1

		#Prepara el handler del movimiento del raton
		self.ventana.asignarDragg(self.mouseDragged)
		#Comienza a dibujar
		self.tablero.draw(self.ventana)
		self.dibuja_fichas()
		#Comienza el juego
		self.jugar()

	#Llamada cada vez que se arrastra el raton
	def mouseDragged(self, event):
		i = int(event.x / 69)
		j = int(event.y / 69)

		#Solo actualiza si ha cambiado de casilla
		if self.lastGhostX != i or self.lastGhostX != j:
			#Intenta desdibujar la ficha
			try:
				self.fichaGhost.undraw()

				#Si se podria colocar ahi la ficha, la dibuja con un color mas claro del que usa el jugador
				if self.tabl.canPlay(i,j,True):
					self.fichaGhost = Circle(Point((i+1)*69-34.5, (j+1)*69-34.5), 34.5)
					if self.tabl.jugador ==1:
						self.fichaGhost.setFill("#FF99FF")
					else:
						self.fichaGhost.setFill("#99FFFF")
					self.fichaGhost.draw(self.ventana)
			except :
				pass


	#Dibuja el estado actual del tablero
	def dibuja_fichas(self): 
		for i in range(8):
			for j in range(8):
				#Dibuja el circulo con el color del jugador al que pertenece la casilla
				circulo = Circle(Point((i+1)*69-34.5, (j+1)*69-34.5), 34.5)
				if self.tabl.tablero[i][j] ==1:
					circulo.setFill("#FF66FF")
					circulo.draw(self.ventana)
				if self.tabl.tablero[i][j] ==-1:
					circulo.setFill("#00FFFF")
					circulo.draw(self.ventana)

	def jugar(self):
		#self.ventana.printText("hola","Mundo")
		endGame = False
		while self.tabl.fichas<64:
			if not self.tabl.checkJugadaPosible():
				if endGame:
					self.calcularPunt() 
				self.ventana.printText("Aviso","Tienes que pasar tu turno")
				endGame = True
				continue
			endGame = False
			jugada = self.ventana.getMouse()
			if self.tabl.play(int(jugada.x/69),int(jugada.y/69)):
				self.dibuja_fichas()
		self.calcularPunt()

	def calcularPunt(self):
		resultado = self.tabl.count()
		if resultado[0]< resultado[1]:
			self.ventana.printText("Ganador","Jugador azul")
		elif resultado[0] > resultado[1]:
			self.ventana.printText("Ganador","Jugador rosa")
		else:
			self.ventana.printText("Ganador","Empate, no hay ganador")
		self.ventana.close()
		sys.exit(0)

if __name__ == "__main__":
	game = Partida()
	game.jugar()
