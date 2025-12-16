pr = float(input('Digite o comprimento da primeira reta: '))
sr = float(input('Digite o compriemto da segunda reta: '))
tr = float(input('Digite o comprimento da terceira reta: '))

if pr + sr > tr and tr + sr > pr and pr + sr > tr:

    print('Elas podem formar um triangulo!')

else:

    print('Elas nao podem formar um triangulo!')

