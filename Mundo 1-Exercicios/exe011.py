l = float(input("Digite a largura da sua parede : "))
v = float(input("Digite a atura da sua parede : "))
a = l * v
t = a / 2

print("Sua parede tem a dimensão de {} x {} e sua área é de {} m².".format(l, v, a))
print("Para pintar essa parede, você precisará de {} litros de tinta.".format(t))