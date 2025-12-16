nome = input('Digite seu nome completo : ').strip()

print('Analisando seu nome...')

# maiúsculas e minúsculas

print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))

# Contar letras sem espaço

total_letras = len(nome) - nome.count(' ')
print('Seu nome tem {} letras' .format(total_letras))

# Contar letras do primeiro nome

primeiro_nome = nome.split()[0]
print('Seu primeiro nome é {} e ele tem {} letras.'.format(primeiro_nome, len(primeiro_nome)))