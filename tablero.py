from piece import Piece
from coordinates import Coordinates, Direction

class Board ():
	def __init__(self):
		self.cells = [[None for _ in range(6)] for _ in range(6)]

	def __str__(self):
		return_string = ''
		for line in self.cells:
			for element in line:
				return_string += '0 ' if element == None else f'{element} '
			return_string += '\n'
		return return_string

	def set_piece(self, coordinates : Coordinates, piece : Piece) -> None:
		if not coordinates.valid():
			raise(Exception('Las coordinates introducidas no son válidas.'))
		self.cells[coordinates.i][coordinates.j] = piece
	
	def get_piece(self, coordinates : Coordinates) -> Piece:
		if not coordinates.valid():
			raise(Exception('Las coordinates introducidas no son válidas.'))
		return self.cells[coordinates.i][coordinates.j]

	def is_piece(self, coordinates : Coordinates) -> bool:
		if not coordinates.valid():
			raise(Exception('Las coordinates introducidas no son válidas.'))
		return isinstance(self.cells[coordinates.i][coordinates.j], Piece)

	def movimientos_disponibles(self, coordinates : Coordinates):
		if not self.is_piece(coordinates):
			raise(Exception('No hay una piece en esa casilla'))
		
		# Quitamos de todas las posibles direcciones las que no son posibles por:
		# 1) La dirección choca con una pared.
		# 2) La dirección choca con una esquina.
		# TO DO: Que la esquina dependa del jugador.
		set_directions = self.movimientos_paredes(coordinates) & self.movimientos_esquinas(coordinates)

		## NOS HEMOS QUEDADO AQUI.

		# Quitamos de todas las posibles direcciones las que no son posibles por:
		# 3) La dirección choca con una pieza del propio jugador.
		# TO DO: Mirar si la pieza es propia o contraria.
		set_directions = {
			direction for direction in set_directions
				if not self.is_piece(coordinates + direction)
		}

		direcciones_casilla_ocupada = {
			direction
				for direction in set_directions
					if (
						self.is_piece(coordinates + direction)
						and 
						(
							self.get_piece(coordinates).jugador != 
							self.get_piece(coordinates + direction).jugador
						)
					)
		}

		return set_directions | direcciones_casilla_ocupada

	def movimientos_paredes(self, coordinates : Coordinates) -> set[Direction]:
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
		
	def movimientos_esquinas(self, coordinates : Coordinates) -> set[Direction]:
		direcciones_restringidas = {
			Coordinates(0, 1) : Direction(3),
			Coordinates(1, 0) : Direction(0),
			Coordinates(0, 4) : Direction(1),
			Coordinates(1, 5) : Direction(0),
			Coordinates(4, 0) : Direction(2),
			Coordinates(5, 1) : Direction(3),
			Coordinates(4, 5) : Direction(2),
			Coordinates(5, 4) : Direction(1)
		}
		return Direction.get_all_directions() - {direcciones_restringidas[coordinates]}
	
	def mover_piece(self, coordinates : Coordinates, direction : Direction) -> None:
		if not self.is_piece(coordinates):
			raise(Exception('No hay una pieza en esa casilla'))
		if not direction in self.movimientos_disponibles(coordinates):
			raise(Exception('No se puede mover a esa casilla.'))
		# TO DO determinar los movimientos disponibles.
