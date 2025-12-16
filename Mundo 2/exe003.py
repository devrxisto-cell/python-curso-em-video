print("Comparando os valores para saber o maior, o menor ou se são iguais!")

num1 = int(input("Esreva um número: "))
num2 = int(input("Escreva outro número: "))

if num1 > num2:
    print(f"O primeiro número: {num1} é maior que o segundo número: {num2}!")
elif num2 > num1:
    print(f"O segundo número: {num2} é maior que o primeiro número: {num1}!")
elif num1 == num2:
    print(f"Os números {num1} e {num2} são iguais!")