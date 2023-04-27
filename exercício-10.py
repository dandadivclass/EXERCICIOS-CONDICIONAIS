#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

aluno = input("EM QUAL TURNO VOCÊ ESTUDA? M-Matutino V-Vespertino ou N-Noturno")

if aluno == "M":
    print("Bom dia!")
elif aluno == "V":
    print("Boa tarde!")
else:
    print("Boa noite!")
