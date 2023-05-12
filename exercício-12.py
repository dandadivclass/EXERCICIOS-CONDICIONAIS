#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda...

horasTrabalhadas = float(input("Informe aqui quantas horas você trabalha por mês:"))
quantoMes = float(input("Digite também quanto você ganha por hora trabalhada:"))
salarioBruto = horasTrabalhadas * quantoMes
print("Você ganha um total de R${}" .format(salarioBruto))

if salarioBruto <= 900:
    print("Logo, você está isento das taxas do INSS, FGTS e Imposto de Renda!")

if salarioBruto > 900 and salarioBruto <= 1500:
    INSS = salarioBruto * 0.1
    print("Ao INSS você paga R${}".format(INSS)
    IR = salarioBruto * 0.05
    print("Você paga R${} de IMPOSTO DE RENDA!" .format(IR))
    SIND = salarioBruto * 0.03
    print("Ao SINDICATO você paga R${}." .format(SIND))

if salarioBruto > 1500 and salarioBruto <= 2500:
    INSS = salarioBruto * 0.1
    print("Ao INSS você paga R${}".format(INSS)
    IR = salarioBruto * 0.10
    print("Você paga R${} de IMPOSTO DE RENDA!".format(IR))
    SIND = salarioBruto * 00.4
    print("Ao SINDICATO você paga R${}".format(IR))
else:
    print("Seu salário é maior que R$2500. Consulte um contador para obter informações sobre as taxas e deduções aplicáveis.")
