soma = 0

for i in range (1, 7):
    num = int(input(f"Digite o {i}º número inteiro: "))
    if num % 2 == 0:
        soma += num

print(f"\nA soma dos números pares digitados é: {soma}")