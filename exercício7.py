#Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = float(input("Numero1"))
num2 = float(input("Numero2"))
num3 = float(input("Numero3"))

if num1 > num2 and num1 > num3:
    print(numero1)
elif num2 > num1 and num2 > num3:
    print(numero2)
elif num3 > num2 and num3 > num1:
    print(numero3)

if num1 < num2 and num1 < num3:
    print(numero1)
elif num2 < num1 and num2 < num3:
    print(numero2)
elif num3 < num2 and num3 < num1:
    print(numero3)

    #CÓDIGO MELHORADO:
   
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3

if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
else:
    menor = num3

print("O maior número é:", maior)
print("O menor número é:", menor)
