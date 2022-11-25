mesesTrabalhados = int(input('Quantos meses completos o Tiago trabalhou?'))

if mesesTrabalhados >= 12:
    disponFerias = input('Tem disponibilidade entre Dezembro e Janeiro?')
    if disponFerias == 'sim':
        print('O Tiago pode tirar férias!')
else:
    print('Sem férias, sem ilhas maldivas, VAI TRABALHAR!!!')