def mover_coordenadas(coordenadas_originales : tuple[int, int], direccion : int):
	i = coordenadas_originales[0]
	j = coordenadas_originales[1]
	if direccion == 0:
		return (i - 1, j)
	elif direccion == 1:
		return (i, j + 1)
	elif direccion == 2:
		return (i + 1, j)
	elif direccion == 3:
		return (i, j - 1)
