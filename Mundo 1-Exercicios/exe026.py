frase = str(input("Digite uma frase : ")).strip().upper()

quantidade = frase.count('A')

primeira = frase.find('A') + 1

ultima = frase.rfind('A') + 1

print(f"A letra A aparece {quantidade} vezes na frase.")
print(f"A primeira letra A aparece na posição {primeira}.")
print(f"A última letra A aparece na posição {ultima}.")
