#ciclo de repeticion while
contador = 0
while True:
    print("bucle infinito")
    contador += 1
    if contador >=5:
        break
    

#listas 
lista_frutas: list = []
lista_alterna: list = list()
#impresion de listas vacias
print(lista_frutas)
print(lista_alterna)
#impresion de tipo de dato
print(type(lista_frutas))
print(type(lista_alterna))
#funciones de las listas 
lista_frutas.append("manzana")
lista_frutas.append("mango")
lista_frutas.append("mandarina")
#contar elementos de una listacon la funcion len
print(len(lista_frutas))
#insercion de un nuevo elemento con la funcion insert()
#requiere una posicion y un valor
lista_frutas.insert(1,"pera")
#eliminia el ultimo registro de la lista con la funcion pop()
print(lista_frutas.pop())
#remover un elemento de una lista con la funcion remove()
lista_frutas.remove("manzana")
#limpiar una lista con la funcion clear()
#lista_frutas.clear()
#eliminar una lista con la funcion del
#del lista_frutas
print(lista_frutas)
for i in lista_frutas:
    print(i, end=",")
print("")
#recorrer una lista con for normal   
for i in range(len(lista_frutas)):
    print(lista_frutas[i])
#impresion de una posicin
print(lista_frutas[0])
#cambiar valor de una posicion 
lista_frutas[1] = "naranja"
lista_frutas.append("manzana")
lista_frutas.append("mango")
lista_frutas.append("mandarina")
print(lista_frutas[-2:])

#tuplas no son mutables (no se puden cambiar sus valores)
tupla_nombres =("Lorena","Isabel","Ana")
tupla_alterna = tuple()
#imprimir tipo de dato
print(type(tupla_nombres))
print(type(tupla_alterna))
#impresion total
print(tupla_nombres)
#impresion por posicion 
print(tupla_nombres[2])
#impresion total por iteracion
for nombre in tupla_nombres:
    print(nombre)
#borrado de una tupla
#del tupla_nombres
print(tupla_nombres)

#añadir los nuevos nombres a una lista desde una tuplaS
lista_nombres =[]
for i in tupla_nombres:
    lista_nombres.append(i)
print(lista_nombres)
lista_nombres.append("Jorge")
lista_nombres.append("karla")
print(lista_nombres)
tupla_nombres = tuple(lista_nombres)
print(tupla_nombres)

#coleccion set
colecion ={'tierra','marte','venus','jupiter','saturno'}
coleccion_alterna =set()
#impresion de tipo de dato
print(type(colecion))
print(type(coleccion_alterna))
#impresion de todos los datos
print(colecion)
#anadir nuevos elementos a una coleccion 
colecion.add('urano')
#update sirve para anadir elementos apartir de otras estructura de datos
colecion.update(lista_frutas)
colecion.update(tupla_nombres)
#descargar un elemento de una coleccion, no existe el elemento mandara un error 
colecion.remove('venus')
#descargar un elemento si no existe no manda error
colecion.discard('pluton')
#limpiar todo el contenido de una coleccion 
colecion.clear()
print(colecion)

#diccionarios
diccionario: dict = {"nombre":"Lorena","carrera":"sis"}
diccionario_alterno = dict()
#impresion de tipo de dato
print(type(diccionario))
print(type(diccionario_alterno))
#mostrar un elemento especifico por medio de su key
print(diccionario["carrera"])
#editar una key del diccionario
diccionario["nombre"] = "Diego"
#añadir un nuevo elemento 
diccionario["semestre"] = 8

print(diccionario.keys())   #impresion de llaves
print(diccionario.values()) #impresion de valores
print(diccionario.items())  #impresion de llaves y valores

for key, valor in diccionario.items():
    print(f"la key es: {key}, y el valor es: {valor}")
    
#impresion general
print(diccionario)

#definir o declarar una funcion 
def test():
    print("impresion desde funcion")
test()
#funcion con argumentos
def test2(nombre = "desconocido", carrera = "desconocida"):
    print(f"hola {nombre}, tu carrera es: {carrera}")
test2(carrera="sis")

#funcion con retorno de valor
def test3(valor1, valor2):
    return valor1 + valor2
print(f"el resultado es: {test3(24,10)}")

#capturar datos por terminal o teclado
numero = int(input("ingresa un numero: "))
print(type(numero))
numero = int(numero)
print(type(numero))
print(f"Tu numero es: {numero}")