soma = cont = 0
while True:
    num = int(input('Digite um valor (999 é o comando de STOP) : '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma entre eles foi {soma} e eu digitei {cont} vezes.')
