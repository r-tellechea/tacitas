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
	
	def __eq__(self, other: object) -> bool:
		return self.direction_code == other.direction_code
	
	def __hash__(self) -> int:
		return hash(self.direction_code)
	
	def get_all_directions() -> set:
		return {Direction(index) for index in range(4)}
		
class Coordinates():
	def __init__(self, i : int, j : int) -> None:
		self.i = i
		self.j = j
		self.limit_i = limit_i
		self.limit_j = limit_j
	
	def __str__(self) -> str:
		return f'({self.i}, {self.j})'
	
	def __add__(self, other : Direction):
		if   other.direction_code == 0:
			return Coordinates(self.i - 1, self.j)
		elif other.direction_code == 1:
			return Coordinates(self.i, self.j + 1)
		elif other.direction_code == 2:
			return Coordinates(self.i + 1, self.j)
		elif other.direction_code == 3:
			return Coordinates(self.i, self.j - 1)

	def __eq__(self, other) -> bool:
		return self.i == other.i and self.j == other.j
	
	def __hash__(self) -> int:
		return hash((self.i, self.j))
	
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
