class Direction():
	def __init__(self, direction_code : int) -> None:
		self.direction_code = direction_code
	
	def __str__(self) -> str:
		if   self.direction_code == 0:
			return 'Arriba'
		elif self.direction_code == 1:
			return 'Derecha'
		elif self.direction_code == 2:
			return 'Abajo'
		elif self.direction_code == 3:
			return 'Izquierda'
	
	def get_all_directions() -> set:
		return {Direction(index) for index in range(4)}
		
class Coordinates():
	def __init__(self, i : int, j : int, limit_i : int = 6, limit_j : int = 6) -> None:
		self.i = i
		self.j = j
		self.limit_i = limit_i
		self.limit_j = limit_j
	
	def __str__(self) -> str:
		return f'({self.i}, {self.j})'
	
	def __add__(self, other : Direction):
		if   other.direction_code == 0:
			return (self.i - 1, self.j)
		elif other.direction_code == 1:
			return (self.i, self.j + 1)
		elif other.direction_code == 2:
			return (self.i + 1, self.j)
		elif other.direction_code == 3:
			return (self.i, self.j - 1)
		
	def valid(self) -> bool:
		return 0 <= self.i < self.limit_i and 0 <= self.j < self.limit_j

if __name__ == '__main__':
	coordenadas = Coordinates(3,5)
	direccion = Direction(1)
	print(coordenadas)
	print(direccion)
	print(coordenadas + direccion)
	for dir in Direction.get_all_directions():
		print(dir)
