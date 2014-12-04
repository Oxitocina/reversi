from Tablero import *
from graphics import *
from copy import deepcopy
class Partida():
	
	def __init__(self):
		self.ventana = GraphWin("Reversi", 555, 555)
		self.tablero = Image(Point(277.5,277.5), "tablero-ajedrez.png")
		self.tabl = Tablero()
		self.fichas = 4
		self.main()
	def main(self):
		self.tablero.draw(self.ventana)
		self.coloca_fichas()
		self.jugar()
		#self.ventana.close()

	def coloca_fichas(self):
		lol = 0
		for i in range(8):
			for j in range(8):
				circulo = Circle(Point((i+1)*69-34.5, (j+1)*69-34.5), 34.5)
				if self.tabl.tablero[i][j] ==1:
					circulo.setFill("#FF66FF")	
					lol += 1
					circulo.draw(self.ventana)
				if self.tabl.tablero[i][j] ==-1:
					circulo.setFill("#00FFFF")
					lol+=1
					circulo.draw(self.ventana)
		print (lol)

	def jugar(self):
		while self.fichas<64:
			jugada = self.ventana.getMouse()
			if self.tabl.play(int(jugada.x/69),int(jugada.y/69)):
				self.fichas += 1
				print (self.fichas)
				self.coloca_fichas()
		if self.tabl.count() < 32:
			print("Gana el azul")
		elif self.tabl.count() > 32:
			print("Gana el rosa")
		else:
			print("Empate")

if __name__ == "__main__":
	culo = Partida()
	culo.jugar()
