from piece import Piece
from functools import reduce

class StartConfiguration():
	def __init__(self, config : list[list[Piece]]) -> None:
		self.config = config
	
	def __str__(self) -> str:
		return_str = ''
		for line in self.config:
			for piece in line:
				return_str += f'{piece} '
			return_str += '\n'
		return return_str[:-1] 

	def line_pieces(self):
		return reduce(lambda line_1, line_2 : line_1 + line_2, self.config)