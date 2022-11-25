#se nota 7 ou maior = aprovado
#se nota 6 e participativo = recuperação
#senão reprovado
notaAluno = int(input('qual a nota do aluno?'))

if notaAluno >= 7:
    print('Parabéns, você foi aprovado!')
elif notaAluno == 6:
    participaivo = input('O aluno é participativo?')
    if participaivo == 'sim':
        print('Recuperação')
    elif participaivo == 'não':
        print('Reprovado')
else:
    print('Reprovado')