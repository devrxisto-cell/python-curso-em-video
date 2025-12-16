d = int(input("Quantos dias alugados? "))
km = float(input("Quantos Km rodados? "))
vk = km * 0.15
vd = d * 60
t = vd + vk
print("O total a pagar é de R${:.2f}.".format(t))