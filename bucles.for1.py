# coding: utf-8
print("PARES E IMPARES")
num1 = int(input("Escribe un numero entero: "))
num2 = int(input("Escribe un numero entero mayor o igual que (num1) : "))

if num2 < num1:
	print ("¡Le he pedido un numero entero mayor que (num1):!")

else: 

    for i in range(1,num2+ 1):
        if i % 2 == 0:
	   print i
