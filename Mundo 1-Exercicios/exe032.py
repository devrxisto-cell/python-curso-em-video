ano = int(input('Digite o ano de seu nascimento: '))

if (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0):
    print('o ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))