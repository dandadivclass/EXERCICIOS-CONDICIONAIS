#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
  A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
  A mensagem "Reprovado", se a média for menor do que sete;
  A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota_parcial1 = float(input("Qual foi sua nota nesse semestre?"))
nota_parcial2 = float(input("Qual foi sua nota nesse segundo semestre?"))
media = (nota_parcial1 + nota_parcial2) / 2

if media >= 7:
    print("Aprovado")
elif media < 7:
    print("Reprovado")
elif media == 10:
    print('Aprovado com distinção')
