import random
p = input("Primeiro aluno : ")
s = input("Segundo aluno : ")
t = input("Terceiro aluno : ")
f = input("Quarto aluno : ")
lista = [p, s, t, f]
print("O aluno sorteado para apagar o quadro foi o {}!".format(random.choice(lista)))