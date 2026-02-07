inventario = [
    {"producto": "Laptop", "categoria": "Electrónica", "stock": 5},
    {"producto": "Mouse", "categoria": "Electrónica", "stock": 25},
    {"producto": "Silla", "categoria": "Muebles", "stock": 2},
    {"producto": "Escritorio", "categoria": "Muebles", "stock": 0}
]

por_cat = {}
agotados = set()
lista_bajo_stock = []

for item in inventario:
    cat = item["categoria"]
    prod = item["producto"]
    stock = item["stock"]
    if cat not in por_cat:
        por_cat[cat] = []
    por_cat[cat].append(prod)
    if stock == 0:
        agotados.add(prod)
    if stock < 5:
        lista_bajo_stock.append(prod)
tupla_stock = tuple(lista_bajo_stock)

print(f"Categorías: {por_cat}")
print(f"Agotados: {agotados}")
print(f"Bajo stock (tupla): {tupla_stock}")