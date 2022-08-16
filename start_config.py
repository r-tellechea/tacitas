from piece import Piece

class StartConfig():
	def __init__(self, config : list[list[Piece]]) -> None:
		self.config = config
	
	def __str__(self) -> str:
		return_str = ''
		for line in self.config:
			for piece in line:
				return_str += f'{piece} '
			return_str += '\n'
		return return_str[:-1] 
