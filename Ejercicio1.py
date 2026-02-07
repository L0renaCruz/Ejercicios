ventas = [
    ("Ana", "Enero", "Laptop", 2, 15000),
    ("Luis", "Enero", "Mouse", 10, 250),
    ("Ana", "Febrero", "Laptop", 1, 15000),
    ("Luis", "Febrero", "Teclado", 5, 800),
    ("Ana", "Enero", "Mouse", 3, 250)
]

ingre_emple = {}
ingre_mes = {}
produc_unicos = set()

for registro in ventas:
    empleado = registro[0]
    mes = registro[1]
    producto = registro[2]
    cantidad = registro[3]
    precio = registro[4]
    total_venta = cantidad * precio
    if empleado in ingre_emple:
        ingre_emple[empleado] += total_venta
    else:
        ingre_emple[empleado] = total_venta
    produc_unicos.add(producto)
    if mes in ingre_mes:
        ingre_mes[mes] += total_venta
    else:
        ingre_mes[mes] = total_venta
mejor_empleado = ""
max_ingreso = 0
for emp, monto in ingre_emple.items():
    if monto > max_ingreso:
        max_ingreso = monto
        mejor_empleado = emp

print(f"Ingresos por empleado: {ingre_emple}")
print(f"Productos únicos: {produc_unicos}")
print(f"Ingresos por mes: {ingre_mes}")
print(f"Mejor empleado: {mejor_empleado}")