print("_" * 15)
print("\nGERADOR DE PA")
print("_" * 15)

primeiro = int(input("\nDigite o primeiro termo: "))
razao = int(input("Digite a razão da PA: "))

print("\nOs 10 primeiros termos da PA são:")

for i in range(0, 10):
    termo = primeiro + i * razao
    print(termo, end=' → ')

print("\n\nFIM...")