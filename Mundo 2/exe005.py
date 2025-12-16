nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = (nota1 + nota2) / 2

print(f"Se você tirou {nota1} e {nota2} vamos ver como ficou sua média: {media:.2f}")

if media >= 7:
    print("Você foi APROVADO !!!")
elif media >= 5 and media < 7:
    print("Você está de recuperação, Estude MAIS...")
else:
    print("Você está REPROVADO !!! MULA ...")