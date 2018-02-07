# coding: utf-8

num1 = int(input("Escribe un numero entero: "))
num2 = int(input("Escribe un numero entero mayor o igual que (num1): "))

if num2 > num1:
	print ("Le he pedido un numero entero mayor que: ")
else: 
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
	    print("El numero {i} es par")
        else:
	    print("El numero {i} es impar")
