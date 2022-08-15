class Piece():
	def __init__(self, color : str, jugador : int):
		self.color = color
		self.jugador = jugador

	def __str__(self):
		return str(self.jugador)
