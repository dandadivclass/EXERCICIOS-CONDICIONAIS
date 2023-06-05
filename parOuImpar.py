#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

#1. par ou ímpar;
#2. positivo ou negativo;
#3. inteiro ou decimal.

numberOne = int(input("Choose a number:"))
numberTwo = int(input("Choose a second number:"))

print("Wich mathematical operation do you want to do?")
print("-EVEN OR ODD \n-POSITIVE OR NEGATIVE")

question = input("Operation choosen:")

if question == "EVEN OR ODD" and numberOne %2 == 0:
    print("Your first number is Even!")
elif numberOne %2 != 0:
    print("Your first number is Odd!")

if question == "EVEN OR ODD" and numberTwo %2 == 0:
    print("Your second number is Even!")
elif numberTwo % 2 != 0:
    print("Your second number is Odd!")


if question == "POSITIVE OR NEGATIVE" and numberOne >= 1:
    print("Your first number is Positive!")
elif numberOne < 0:
    print("Your first number is Negative!")

if question == "POSITIVE OR NEGATIVE" and numberTwo >= 1:
    print("Your number is Positive!")
elif numberTwo < 0:
    print("Your first number is Negative!")
