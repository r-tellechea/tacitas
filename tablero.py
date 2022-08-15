from pieza import Pieza
from coordenadas import mover_coordenadas

class Tablero ():
	def __init__(self):
		self.casillas = [[None for _ in range(6)] for _ in range(6)]

	def __str__(self):
		return_string = ''
		for line in self.casillas:
			for element in line:
				return_string += '0 ' if element == None else f'{element} '
			return_string += '\n'
		return return_string

	def set_pieza(self, i : int, j : int, pieza : Pieza) -> None:
		if not (0 <= i < 6 and 0 <= j < 6):
			raise(Exception('Las coordenadas introducidas no son válidas.'))
		self.casillas[i][j] = pieza
	
	def get_pieza(self, coordenadas : tuple[int, int]) -> Pieza:
		return self.casillas[coordenadas[0]][coordenadas[1]]

	def is_pieza(self, coordenadas : tuple[int, int]) -> bool:
		return isinstance(self.casillas[coordenadas[0]][coordenadas[1]], Pieza)

	def movimientos_pieza(self, i : int, j : int):
		if self.casillas[i][j] == None:
			raise(Exception('No hay una pieza en esa casilla'))
		# Me queda comprobar las restricciones de las propias piezas.
		direcciones = self.movimientos_paredes(i, j) & self.movimientos_esquinas(i, j)

		direcciones_casilla_vacia = {
			direccion
				for direccion in direcciones
					if not self.is_pieza(mover_coordenadas((i,j), direccion))
		}

		direcciones_casilla_ocupada = {
			direccion
				for direccion in direcciones
					if (
						self.is_pieza(mover_coordenadas((i,j), direccion))
						and 
						(
							self.get_pieza((i,j)).jugador != 
							self.get_pieza(mover_coordenadas((i,j), direccion)).jugador
						)
					)
		}

		return direcciones_casilla_vacia | direcciones_casilla_ocupada

	def movimientos_paredes(self, i : int, j : int):
		direcciones = {0, 1, 2, 3}
		if i == 0:
			direcciones - {0}
		if i == 5:
			direcciones - {2}
		if j == 0:
			direcciones - {3}
		if j == 5:
			direcciones - {1}
		return direcciones
		
	def movimientos_esquinas(self, i : int, j : int):
		direcciones_restringidas = {
			(0, 1) : 3,
			(1, 0) : 0,
			(0, 4) : 1,
			(1, 5) : 0,
			(4, 0) : 2,
			(5, 1) : 3,
			(4, 5) : 2,
			(5, 4) : 1
		}
		return {0, 1, 2, 3} - {direcciones_restringidas[(i, j)]}
	
	
	def mover_pieza(self, i : int, j : int, direccion : int) -> None:
		if self.casillas[i][j] == None:
			raise(Exception('No hay una pieza en esa casilla'))
		if not direccion in self.movimientos_pieza(i, j):
			raise(Exception('No se puede mover a esa casilla.'))
