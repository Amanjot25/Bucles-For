# coding: utf-8
print("DIVISORES")
num1 = int(input("Escribe un numero mayor que cero: "))

if num1<=0:
	print("¡Le he pedido un numero entero mayor que cero!")
else:
	for i in range(1,(num1/2)+1):
	    if num1 % i ==0 :
		print(i)

print("FIN")
