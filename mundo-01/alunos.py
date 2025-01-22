qnt_alunos = int(input("Quantos alunos tem na turma? "))
aluno = 0  
while True:
    if aluno != qnt_alunos:
        aluno = aluno + 1
        nota_aluno = int(input(f"Qual a nota do aluno {aluno}? "))

    elif aluno == qnt_alunos:
        break

print(f"O melhor aproveitamento foi de {aluno} com a nota de {nota_aluno}")