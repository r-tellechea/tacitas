from player import Player
from color import Color

class Piece():
	def __init__(self, color : Color, player : Player):
		self.color = color
		self.player = player

	def __str__(self):
		return str(self.color + self.player)
