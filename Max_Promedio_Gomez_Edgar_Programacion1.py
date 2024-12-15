#Actividad Individual 3 - Ejercicio en Clase - Programación
#Nombre: Edgar Gomez - Fecha: 13 de diciembre de 2024
# EL usuario debe ingresar cuantos números desea digitar, de estos números ingresados se debe determinar el, mayor, menor y el promedio

numeros = []

while True:
    entrada = input("Por favor, ingrese un número (o 'SALIR' para terminar): ")
    if entrada.lower() == 'SALIR':
        break
    else:
        numero = float(entrada)
        numeros.append(numero)

if numeros:
    mayor = max(numeros)
    menor = min(numeros)
    promedio = sum(numeros) / len(numeros)
else:
    mayor = menor = promedio = None

print(f"El numero mayor ingresado es: [ {mayor} ]")
print(f"El numero menor ingresado es: [ {menor} ]")
print(f"El promedio calculado es: [ {promedio} ]")