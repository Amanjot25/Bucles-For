#coding:utf -8
print("NÚMEROS NEGATIVOS")
num1 = int(input("¿Cuántos numeros va a introducir? "))

if num1 < 0:
    print("¡Imposible!")
else:
    cont = 0
    for i in range(1, num1 + 1):
        num2 = float(input("Escriba el numero (i): "))
        if num2 < 0:
            cont= cont + 1
    if cont == 0:
        print("No ha escrito ningún numero negativo")
    else:
        print("Ha escrito (i) numeros negativos")

