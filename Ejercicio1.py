import sys

print("Conversor de Medidas de Temperatura (°C a °F)")
print("_____________________________________________\n")
#Declaracion de Variables
Celcius = input("Ingrese Temperatura en °C : ")
Farenheit = int(Celcius) * 1.8 + 32
print("_____________________________________________\n")
print('Su Temperatura Ingresada es : ' + str(Farenheit) + ' °F')
print("_____________________________________________\n")
final = input('Presione Enter para Salir...')

