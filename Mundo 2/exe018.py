frase = input("Digite uma frase: ").strip().lower()

# remove os espaços e junta tudo em uma string só
frase_sem_espaco = ''.join(frase.split())

# Inverte a frase
frase_invertida = frase_sem_espaco[::-1]

print(f"\nFrase original (sem espaços): {frase_sem_espaco}")
print(f"Frase invertida:                {frase_invertida}")

if frase_sem_espaco == frase_invertida:
    print("\n É um palíndromo!")
else:
    print("\n Não é um palíndromo.")
