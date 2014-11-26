from Tablero import *
from graphics import *
class Partida():
	
	def __init__(self):
		self.ventana = GraphWin("Reversi", 555, 555)
		self.tablero = Image(Point(277.5,277.5), "tablero-ajedrez.png")
		self.tabl = Tablero()
		self.fichas = []
	def main():
		tablero.draw(ventana)
		ventana.getMouse() 
		ventana.close()

	def coloca_fichas(self):
		for i in self.tabl.tablero:
			for x in i:
				if x == 1:
					circulo = Circle(Point((i+1)*69-34.5, (j+1)*69-34.5), 34.5)
					circulo.setFill("red")
					self.fichas.append(deepcopy(circulo)) #Deep copy?
				elif x == -1:
					circulo = Circle(Point((i+1)*69-34.5, (j+1)*69-34.5), 34.5)
					circulo.setFill("green")
					self.fichas.append(deepcopy(circulo)) #Deep copy?
	def jugar(self):
		while len(self.fichas)<64:
			jugada = ventana.getMouse()
			if play(int(jugada.x/69)+1,int(jugada.y/69)+1):
				self.coloca_fichas()

