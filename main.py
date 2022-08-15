from tablero import Tablero
from pieza import Pieza

pieza_roja_1 = Pieza(color='rojo', jugador=1)
pieza_azul_1 = Pieza(color='azul', jugador=1)
pieza_roja_2 = Pieza(color='rojo', jugador=2)
pieza_azul_2 = Pieza(color='azul', jugador=2)


tab = Tablero()
tab.set_pieza(0,1, pieza_azul_1)
tab.set_pieza(1,1, pieza_roja_1)
tab.set_pieza(0,4, pieza_azul_2)
tab.set_pieza(1,4, pieza_roja_2)


print(tab)
tab.mover_pieza(1,1,0)
print(tab)



