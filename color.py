class Color():
	def __init__(self, color : str) -> None:
		self.color = color
	
	def __str__(self) -> str:
		return self.color

	def __eq__(self, other: object) -> bool:
		return self.color == other.color
