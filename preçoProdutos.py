#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
sabendo que a decisão é sempre pelo mais barato.

pro1 = float(input("Informe o preço da opção um:"))
pro2 = float(input("Informe o preço da opção dois:"))
pro3 = float(input("Informe o preço da opção tres:"))

if pro1 < pro2 and pro1 < pro3:
    print("Você deve comprar a opção um, ela está mais barata!")
if pro2 < pro1 and pro2 < pro3:
    print("Você deve comprar a opção dois, ela está a mais barata!")
if pro3 < pro1 and pro3 < pro2:
    print("Você deve comprar a opção três, ela está mais barata!")
