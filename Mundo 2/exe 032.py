while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('_' * 30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('_' * 30)
print('PROGRAMA ENCERRADO. Volte sempre!')
