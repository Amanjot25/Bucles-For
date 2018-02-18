#coding:utf -8
print("MAYORES QUE EL PRIMERO")

num1 = int(input("¿Cuántos valores va a introducir? "))
while num1 < 1:
  print("¡Imposible!")
  
num2 = int(input("Escriba un número: "))
for i in range(1,num1 - 1):
        num3 = int(input("Escriba un número más grande que (num2): "))
        if num3 <= num2:
            print("(num3) no es mayor que (num2)")
            print("Fin")

