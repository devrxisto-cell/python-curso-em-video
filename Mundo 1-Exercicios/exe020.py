import random

p = input("Primeiro aluno : ")
s = input("Segundo aluno : ")
t = input("Terceiro aluno : ")
f = input("Quarto aluno : ")

lista = [p, s, t, f]

ordem = random.sample(lista, len(lista))

print("Ordem de apresentação dos trabalhos começando pelo aluno(a) : {} segundo {} terceiro {} e por ultimo {}. ".format(*ordem))