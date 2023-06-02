#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, 
e calcule a sua média

nota = float(input("Digite sua nota aqui:"))
nota2 = float(input("Digite sua segunda nota aqui:"))
media = (nota + nota2) / 2

if media == 9 and media == 10:
    print("VOCÊ TIROU A E FOI APROVADO")
elif media >= 7.5 and media <= 9:
    print("VOCÊ TIROU B E FOI APROVADO")
elif media >= 6 and media <= 7.5:
    print("VOCÊ TIROU C E FOI APROVADO")
elif media >= 4 and media >= 6:
    print("VOCÊ TIROU D E FOI REPROVADO")
elif media >= 4 and media == 0:
    print("VOCÊ TIROU E E FOI REPROVADO")
