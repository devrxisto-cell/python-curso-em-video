import random

numero_pc = random.randint(0,5)
numero_usuario = int(input('Digite um numero entre 0 e 5 :'))

if numero_usuario == numero_pc:
    print('Voce acertou !')

else:
    print('Voce errou ! o numero era {}'.format(numero_pc))