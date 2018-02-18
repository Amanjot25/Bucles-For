#coding:utf -8
print("CONTADOR DE PARES E IMPARES")
num1 = int(input("¿Cuántos numeros va a introducir? "))
if num1 < 1:
    print("¡Imposible!")
else:
    pares = 0
    for i in range(1, num1 + 1):
        num2 = int(input("Escriba el valor (i): "))
        if num2 % 2 == 0:
            pares += 1
    print("Ha escrito i números pares y (num1-i) numeros impares")
    print("FIN")

