casa = float(input("Qual o valor da casa: "))
salario = float(input("Qual seu sálario: "))
anos = int(input("Em quantos anos voce quer pagar: "))

prestacao = casa / (anos * 12)
limite = salario * 0.30

print(f"Para pagar uma casa de R${casa:.3f} em {anos} anos, a prestação será de R${prestacao:.2f}")

if prestacao <= limite:
    print("Empréstimo APROVADO!!!")
else:
    print("Empréstio NEGADO, A prestação excede 30% do seu sálario. Trabalha mais fudido! XXXXXXXXX")