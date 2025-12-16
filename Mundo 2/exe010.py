import random

import ramdom
import time

print("=========JOKENPÔ=========")
itens = ['Pedra', 'Papel', 'Tesoura']

computador = random.randint(0, 2)

print("""
Esolha ua opção:
[0] Pedra
[1] Papel
[2] Tesoura
""")

jogador = int(input("Qual é a sua jogada? "))

print("\nJOOOOOOOO...")
time.sleep(1)
print("KEEEN...")
time.sleep(1)
print("PÔÔÔ...\n")
time.sleep(0.5)

print(f"Computador jogou {itens[computador]}")
print(f"Jogador jogou {itens[jogador]}")

if jogador < 0 or jogador > 2:
    print("\nJogada inválida! Tente novamente.")
elif computador == jogador:
    print("EMPATE!")
elif (computador == 0 and jogador == 2) or \
     (computador == 1 and jogador == 0) or \
     (computador == 2 and jogador == 1):
    print("\nCOMPUTADOR VENCEU!")
else:
    print("\nVOCÊ VENCE!!!")