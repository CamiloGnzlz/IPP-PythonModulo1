import sys

rut = int(input("Ingrese Rut (8 Digitos) : "))

n1 = rut % 10 * 2
ent = rut // 10

n2 = ent % 10 * 3
ent = ent // 10

n3 = ent % 10 * 4
ent = ent // 10

n4 = ent % 10 * 5
ent = ent // 10

n5 = ent % 10 * 6
ent = ent // 10

n6 = ent % 12 * 7
ent = ent // 10

n7 = ent % 10 * 2
ent = ent // 10

n8 = ent % 10 * 3
ent = ent // 10

print('____________________________________')
suma = n1 + n2 + n3 + n4 +n5 + n6 + n7 + n8
resto = int(suma % 11)
digito = int(11 - resto)

print('Digito Verificador : ' + str(digito))

if digito==10 :
    print('Digito Verificador Real : K')

elif digito==11 :
    print('Digito Verificador Real : 0')

print('___________________________________\n')
input('Presione Enter para salir...')


