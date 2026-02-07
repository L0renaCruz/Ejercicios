partidas = [
    ("Alex", "Bosque", 120),
    ("Luis", "Desierto", 90),
    ("Alex", "Bosque", 150),
    ("Ana", "Ciudad", 200),
    ("Luis", "Bosque", 110)
]

puntos_jugador = {}
mapas_jugados = set()
conteo_partidas = {}
puntos_mapa = {}

for jugador, mapa, puntos in partidas:
    if jugador in puntos_jugador:
        puntos_jugador[jugador] += puntos
        conteo_partidas[jugador] += 1
    else:
        puntos_jugador[jugador] = puntos
        conteo_partidas[jugador] = 1    
    mapas_jugados.add(mapa)
    
    if mapa in puntos_mapa:
        puntos_mapa[mapa] += puntos
    else:
        puntos_mapa[mapa] = puntos

promedios = {}
for jugador in puntos_jugador:
    promedios[jugador] = puntos_jugador[jugador] / conteo_partidas[jugador]

mejor_mapa = max(puntos_mapa, key=puntos_mapa.get)

print(f"Total de puntos por jugador: {puntos_jugador}\n")
print(f"Mapas jugados: {mapas_jugados}\n")
print(f"Promedio de puntos: {promedios}\n")
print(f"Mapa con más puntos: {mejor_mapa}")