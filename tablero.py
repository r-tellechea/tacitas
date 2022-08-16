from piece import Piece
from player import Player
from coordinates import Coordinates, Direction
from start_config import StartConfiguration

class Board ():
	def __init__(self, limit_i : int = 6, limit_j : int = 6):
		self.cells = [[None for _ in range(6)] for _ in range(6)]

		self.limit_i = limit_i
		self.limit_j = limit_j

		self.player_top = Player()
		self.player_bot = ~self.player_top
		# TO DO: Que quede tan chulo como arriba.
		self.color_blue = Color('blue')
		self.color_red  = Color('red')

	def __str__(self):
		return_string = ''
		for line in self.cells:
			for element in line:
				return_string += '0 ' if element == None else f'{element} '
			return_string += '\n'
		return return_string[:-1]

	def correct_coordinates(self, coordinates : Coordinates) -> bool:
		return 0 <= coordinates.i < self.limit_i and 0 <= coordinates.j < self.limit_j

	def check_correct_coordinates(self, coordinates : Coordinates) -> None:
		if not self.correct_coordinates(coordinates):
			raise(Exception('Las coordinates introducidas no son válidas.'))
	
	def is_piece(self, coordinates : Coordinates) -> bool:
		self.check_correct_coordinates(coordinates)
		return isinstance(self.cells[coordinates.i][coordinates.j], Piece)

	def check_is_piece(self, coordinates : Coordinates) -> None:
		if not self.is_piece(coordinates):
			raise(Exception('No hay una pieza en las coordenadas introducidas.'))	
	
	def correct_movement(self, coordinates : Coordinates, direction : Direction) -> bool:
		return direction in self.available_movements(coordinates)

	def check_correct_movement(self, coordinates : Coordinates, direction : Direction) -> None:
		if not self.correct_movement(coordinates, direction):
			raise(Exception('No se puede mover a esa casilla.'))

	def set_piece(self, coordinates : Coordinates, piece : Piece) -> None:
		self.check_correct_coordinates(coordinates)
		self.cells[coordinates.i][coordinates.j] = piece
	
	def get_piece(self, coordinates : Coordinates) -> Piece:
		self.check_correct_coordinates(coordinates)
		return self.cells[coordinates.i][coordinates.j]

	def available_movements(self, coordinates : Coordinates):
		self.check_is_piece(coordinates)
		
		set_directions = Direction.get_all_directions()
		# Quitamos de todas las posibles direcciones las que no son posibles por:
		# 1) La dirección choca con una pared.
		set_directions &= self.movements_wall(coordinates)
		# 2) La dirección choca con una esquina.
		set_directions &= self.movements_corner(coordinates)
		# 3) La dirección señala una pieza propia.
		set_directions &= self.movements_self_pieces(coordinates)

		return set_directions

	def movements_wall(self, coordinates : Coordinates) -> set[Direction]:
		directions = Direction.get_all_directions()
		if coordinates.i == 0:
			directions - {Direction(0)}
		if coordinates.i == 5:
			directions - {Direction(2)}
		if coordinates.j == 0:
			directions - {Direction(3)}
		if coordinates.j == 5:
			directions - {Direction(1)}
		return directions
		
	def movements_corner(self, coordinates : Coordinates) -> set[Direction]:
		restricted_corner_top = {
			Coordinates(0, 1) : Direction(3),
			Coordinates(1, 0) : Direction(0),
			Coordinates(0, 4) : Direction(1),
			Coordinates(1, 5) : Direction(0)
		}

		restricted_corner_bot = {
			Coordinates(4, 0) : Direction(2),
			Coordinates(5, 1) : Direction(3),
			Coordinates(4, 5) : Direction(2),
			Coordinates(5, 4) : Direction(1)
		}

		restricted_corner = restricted_corner_top | restricted_corner_bot

		piece = self.get_piece(coordinates)
		directions = Direction.get_all_directions()

		if piece.color == self.color_red:
			return directions - {
				restricted_corner[coordinates] 
					if coordinates in restricted_corner else None
			}
		else:
			if piece.player == self.player_top:
				return directions - {
					restricted_corner_top[coordinates] 
						if coordinates in restricted_corner_top else None
				}
			else:
				return directions - {
					restricted_corner_bot[coordinates] 
						if coordinates in restricted_corner_bot else None
				}

	def movements_self_pieces(self, coordinates : Coordinates) -> set[Direction]:
		set_directions = Direction.get_all_directions()
		set_directions = {
			direction 
				for direction in set_directions 
					if self.correct_coordinates(coordinates + direction)
		}
		set_directions = {
			direction
				for direction in set_directions
					if not (
						self.is_piece(coordinates + direction) and 
						self.get_piece(coordinates).player == 
						self.get_piece(coordinates + direction).player
					)
		}
		return set_directions
	
	def move_piece(self, coordinates : Coordinates, direction : Direction) -> None:
		self.check_is_piece(coordinates)
		self.check_correct_movement(coordinates, direction)
		# TO DO determinar los movimientos disponibles.
		available_movements = self.available_movements(coordinates)
		pass

	def get_initial_positions(self, player : Player):
		if player == self.player_bot:
			return [
				Coordinates(i, j)
					for i in (4, 5)
						for j in (1,2,3,4)
			]
		else:
			return [
				Coordinates(i, j)
					for i in (1, 0)
						for j in (4,3,2,1)
			]

	def set_start_configuration(self, player : Player, start_configuration : StartConfiguration) -> None:
		list_coordinates = self.get_initial_positions(player)
		list_pieces = start_configuration.line_pieces()
		for coordinates, piece in zip(list_coordinates, list_pieces):
			self.set_piece(coordinates, piece)

if __name__ == '__main__':
	from color import Color
	from player import Player
	cords = Coordinates(0,1)
	piece_1 = Piece(Color('blue'), Player(2))
	piece_2 = Piece(Color('blue'), Player(2))
	board = Board()

	s_config = StartConfiguration([[Piece(Color('red'), Player(1))] * 4, [Piece(Color('blue'), Player(1))] * 4])
	print(s_config)
	board.set_start_configuration(Player(2), s_config)
	board.set_start_configuration(Player(1), s_config)
	print(board)
	