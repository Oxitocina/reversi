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
		for i in self.tabl.tablero:
			for x in i:
				if x == 1:
					circulo = Circle(Point((i+1)*69-34.5, (j+1)*69-34.5), 34.5)
					circulo.setFill("red")
					circulo.draw(self.ventana)
				elif x == -1:
					circulo = Circle(Point((i+1)*69-34.5, (j+1)*69-34.5), 34.5)
					circulo.setFill("green")
					circulo.draw(self.ventana)
	def jugar(self):
		while self.fichas<64:
			jugada = self.ventana.getMouse()
			if self.tabl.play(int(jugada.x/69)+1,int(jugada.y/69)+1):
				self.fichas += 1
				self.coloca_fichas

if __name__ == "__main__":
	culo = Partida()
