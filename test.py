# Declaraciones de variables
#str = string
texto: str = ""    #Es una cadena de texto vacía
entero: int = 10    #Es un número entero
flotante: float = 1.5      #Es un número con decimales
booleano: bool = True     #Es un valor booleano (True o False)

#impresion de texto
print("Hola Mundo")
#impresion de variables
print(texto)
print(entero)
print(flotante)
print(booleano)

#impresion con escape de variables 
print(f"Este es el valor de una variable: {flotante}")
print("este es un texto", booleano)
#funciones adicionales de print
print("Menu de usuario".center(50,"*"))
print("texto de pruebas", end="\n\n") #elimina el salto de linea
print("texto de pruebas2", end="\n\n") #elimina el salto de linea

#impresion de tipo de dato
print(type(texto))
print(type(entero))
print(type(flotante))
print(type(booleano))

#impresion de direccion de memoria
print(id(texto))
print(id(entero))
print(id(flotante))
print(id(booleano))


#Estructura de control 
if entero > 0 and entero < 10:
    if entero < 100:
        print("Esta dentro del rango")
    else:
        print("Esta fuera del rango")
else:
    print("Es menor")
    
#ciclos de repeticion
#range(inicio, final, incremento) 
for i in range (5,31,5):
    print(i, end=",")

for letra in texto:
    print(letra, end=",")
