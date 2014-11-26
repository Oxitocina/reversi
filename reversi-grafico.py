from Tablero import *
from graphics import *

def main():
	ventana = GraphWin("Reversi", 555, 555)
	tablero = Image(Point(277.5,277.5), "tablero-ajedrez.png")
	tablero.draw(ventana)
	
	ventana.getMouse() 
	ventana.close() 
main()
