import pygame
# Definimos algunos colores
NEGRO = ( 0, 0, 0)
BLANCO = ( 255, 255, 255)
VERDE = ( 0, 255, 0)
ROJO = ( 255, 0, 0)
VIOLETA=(98,0,255)
largo = 20
alto = 20
# Establecemos el margen entre las celdas.
margen = 5
# Creamos un array bidimensional. Un array bidimensional

grid = []
for fila in range(10):

	grid.append([])
	for columna in range(10):
		grid[fila].append(0) 

grid[1][5] = 1
# Inicializamos pygame
pygame.init()
# Establecemos el alto y largo de la pantalla
dimensiones = [255, 255]
pantalla = pygame.display.set_mode(dimensiones)

pygame.display.set_caption("Reticulas y Matrices")

hecho = False

reloj = pygame.time.Clock()
# -------- Bucle Principal del Programa-----------
while hecho == False:
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			hecho = True
		elif evento.type == pygame.MOUSEBUTTONDOWN:

			pos = pygame.mouse.get_pos()

			columna = pos[0] // (largo + margen)
			fila = pos[1] // (alto + margen)

			grid[fila][columna] = grid[fila][columna]+1
			print("Click ", pos, "Coordenadas de la reticula: ", fila, columna)

	pantalla.fill(NEGRO)

	for fila in range(10):
		for columna in range(10):
			color = BLANCO
			if grid[fila][columna] == 1:
				color = VERDE
			elif grid[fila][columna] == 2:
				color = ROJO
			elif grid[fila][columna] == 0:
				color = BLANCO
			elif grid[fila][columna] == 3:
				color = VIOLETA
			elif grid[fila][columna] > 3:
				grid[fila][columna]==0
			pygame.draw.rect(pantalla,color,[(margen+largo)*columna+margen,(margen+alto)*fila+margen,largo,alto])
# Limitamos a 20 fotogramas por segundo.
	reloj.tick(60)
# Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
	pygame.display.flip()

pygame.quit()
