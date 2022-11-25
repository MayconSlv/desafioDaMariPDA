# - Maior que 25 graus ("Oba! A PDA pode marcar a data").
# - Menor ou igual a 25 graus ("Vamos! O que vale é a companhia").
# - Menor ou igual a 15 graus ("Estará muito frio, não podemos alugar nessa data")
temperatura = int(input('qual a temperatura?'))
if temperatura > 25:
    print('Oba! A PDA pode marcar a data')
elif temperatura <= 15:
    print('Estará muito frio, não podemos alugar nessa data')
elif temperatura <= 25:
    print('Vamos! O que vale é a companhia')