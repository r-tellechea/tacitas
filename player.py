class Player():
	def __init__(self, player_name : int = 1) -> None:
		if not player_name in (1,2):
			raise(Exception('O se llama Jugador 1 o se llama Jugador 2.'))
		self.player_name = player_name

	def __str__(self) -> str:
		return str(self.player_name)

	def __eq__(self, other) -> bool:
		return self.player_name == other.player_name

	def __invert__(self):
		return Player(1) if self.player_name == 2 else Player(2)

if __name__ == '__main__':
	p = Player(1)
	q = Player(2)
	print(~p == q)
	print(~ ~ Player() == Player())
