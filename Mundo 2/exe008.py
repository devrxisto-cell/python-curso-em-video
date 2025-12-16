peso = float(input("Digite seu peso (KG): "))
altura = float(input("Digite sua altura (M): "))

imc = peso / (altura ** 2)
print(f"Seu IMC é {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso, Tem que comer mais!")
elif 18.5 <= imc < 25:
    print("Peso Ideal, Você é um atleta!")
elif 25 <= imc < 30:
    print("Você está com Sobrepeso, ta gordão!")
elif 30 <= imc < 40:
    print("Você está Obeso, Ta igual uma BALEIA!!!")
else:
    print("Você nem consegue andar mais, ta com OBESIDADE MÓRBIDA...")