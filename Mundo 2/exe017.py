num = int(input("Digite um número: "))
tot = 0  #contador de divisores

for i in range(1, num + 1):
    if num % i == 0:
        tot += 1
        print(f"\033[32m{i}\033[m", end=' ')
    else:
        print(f"\033[31m{i}\033[m", end=' ')

print(f"\n\nO número {num} foi divisível {tot} vezes.")

if tot == 2:
    print("Por isso, ele é PRIMO.")
else:
    print("Por isso, ele NÃO É PRIMO!")