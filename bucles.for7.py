#coding:utf -8
print("SUMA ENTRE VALORES")
num1 = int(input("Escribe un numero entero: "))
num2= int(input(f"Escribe un numero entero mayor que (num1): "))

if num2 < num1:
    print("¡Le he pedido un numero entero mayor o igual que (num1)!")
else:
    suma = 0
    for i in range(num1, num2 + 1):
        suma = suma + i
    print("La suma desde (num1) hasta (num2) es (suma)")
    print("FIN")
