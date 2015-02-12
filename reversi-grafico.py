from Tablero import *
from graphics import *
from sys import *

from socket import *

class Partida():	
	def __init__(self):
		print("¿Quieres jugar online o en local?")
		a = input()
		if a == "0" or a == "online" or a == "o":
			self.online = True
			print("¿Quieres ser el host o unirte a una partida?")
			a = input()
			if a == "host" or a == "0":
				self.host()
			else:
				self.client()
		else:
			self.online = False


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
			#EN el caso de jugar online y si no toca al local
			if self.online and self.tabl.jugador != self.yo:
				jugada = self.recvMessage()
				jugadaX,jugadaY = jugada.split('/')
				if self.tabl.play(int(float(jugadaX)/69),int(float(jugadaY)/69)):
					self.dibuja_fichas()
				else:
					print ("Error en la comunicacion")
					sys.exit(-1)
			#Toca jugar al local o no hay online
			else:
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
					#ENVIAR MENSAJE
					if self.online:
						self.sendMessage(str(jugada.x) + "/" + str(jugada.y))


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

	def host(self):
		HOST = ''                 # Symbolic name meaning all available interfaces
		PORT = 50007              # Arbitrary non-privileged port
		s = socket(AF_INET, SOCK_STREAM)
		s.bind((HOST, PORT))
		s.listen(1)
		print("esperando conexion del contrincante")
		self.socketin, addr = s.accept()
		print ('Connected by', addr)
		self.yo = 1

	def client(self):
		print("Cual es la ip de tu contrincante? : ")
		ip = input()
		HOST = ip    # The remote host
		PORT = 50007              # The same port as used by the server
		self.socketin = socket(AF_INET, SOCK_STREAM)
		self.socketin.connect((HOST, PORT))
		self.yo = -1

	def sendMessage(self,string):
		self.socketin.send(bytes(string,'UTF-8'))
	
	def recvMessage(self):
		data = self.socketin.recv(1024)
		return data.decode('UTF-8')

	def closeConn(self):
		self.socketin.close()
if __name__ == "__main__":
	
	game = Partida()
