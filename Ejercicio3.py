import sys

print('Calcular la nota final de presentacion')
print('_______________________________________\n')

lab1 = input('Ingrese Nota Laboratorio 1 : ')
lab2 = input('Ingrese Nota Laboratorio 2 : ')
lab3 = input('Ingrese Nota Laboratorio 3 : ')
suma = float(lab1) + float(lab2) + float(lab3)
promlab = suma /3
pondLab = round(promlab, 1) * 0.15

tarea1 = input('Ingrese Nota Tarea 1 : ')
tarea2 = input('Ingrese Nota Tarea 2 : ')
tarea3 = input('Ingrese Nota Tarea 3 : ')
suma = float(tarea1) + float(tarea2) + float(tarea3)
promtarea = suma /3
pondTarea = round(promtarea, 1) * 0.15

sol1 = input('Solemne 1 : ')
pondSol1 = float(sol1) * 0.35
sol2 = input('Solemne 2 : ')
pondSol2 = float(sol2) * 0.35

sumas = float(pondLab) + float(pondTarea) + float(pondSol1) + float(pondSol2)
total = round(sumas, 1)
print('___________________________')
print('Nota de Presentación : ' + str(total))
print('Presiona Enter para Salir')
