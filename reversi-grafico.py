from Tablero import *
from graphics import *

def main():
	ventana = GraphWin("Reversi", 555, 555)
	tablero = Image(Point(277.5,277.5), "tablero-ajedrez.png")
	tablero.draw(ventana)
	tabl = Tablero()
	fichas = []
	ventana.getMouse() 
	ventana.close()

def repintar(tablero, fichas):
	for i in tablero.tablero:
		for x in i:
			if x == 1:
				circulo = Circle(Point((i+1)*69-34.5, (j+1)*69-34.5), 34.5)
				circulo.setFill("red")
				fichas.append(circulo) #Deep copy?
			elif x == -1:
				circulo = Circle(Point((i+1)*69-34.5, (j+1)*69-34.5), 34.5)
				circulo.setFill("green")
				fichas.append(circulo) #Deep copy?
main()
