import sys

print('Calcular el promedio de 3 numeros enteros')
print('_________________________________________\n')

n1 = input('Ingrese N1 : ')
n2 = input('Ingrese N2 : ')
n3 = input('Ingrese N3 : ')

valores = int(n1) + int(n2) + int(n3)
promedio = round(valores /3, 1)

print('_________________________________________\n')
print('El Promedio de los tres numeros es : ' + str(promedio))
print('_________________________________________\n')
input('Presione Enter para salir...')
