#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores 
e lhe contraram para desenvolver o programa que calculará os reajustes

colab = float(input("Informe aqui o seu salário"))

if colab <= 280:
    aumento = 0.2
elif colab >= 280 and colab <= 700:
    aumento = 0.15
elif colab >= 700 and colab <= 1500:
    aumento = 0.1
elif colab >= 1500:
    aumento = 0.05

reajuste = colab * aumento
aumento = colab + reajuste

print("O seu salário é no valor de R${}" .format(colab))
print("O seu salário é no valor de R${} e teve um reajuste de R${}" .format(colab, reajuste))
print("Então, o aumento foi de R${}" .format(aumento))
