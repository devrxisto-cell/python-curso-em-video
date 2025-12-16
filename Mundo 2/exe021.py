soma_idade = 0
maior_idade_homen = 0
nome_homen_mais_velho = ''
mulheres_menor_20 = 0

for i in range(1, 5):
    print(f"\n--- {i}ª PESSOA ---")
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()

    soma_idade += idade

    if sexo == 'M':
        if idade > maior_idade_homen:
            maior_idade_homen = idade
            nome_homen_mais_velho = nome
    elif sexo == 'F':
        if idade < 20:
            mulheres_menor_20 += 1

media = soma_idade / 4

print(f"A média de idade do grupo é: {media:.1f} anos.")
print(f"O homen mais velho é: {nome_homen_mais_velho} com {maior_idade_homen} anos.")
print(f"Mulheres com menos de 20 anos: {mulheres_menor_20} .")
